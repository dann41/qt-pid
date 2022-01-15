import sys
import qasync
from PyQt5 import QtCore, QtGui, QtWidgets

from pidgui import *
from serial_port import *

class ComboSlider(QtCore.QObject):
    def __init__(self, slider: QtWidgets.QSlider, editText: QtWidgets.QLineEdit):
        super(ComboSlider, self).__init__()
        self.slider = slider
        self.editText = editText
        self.setup()

    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() in [QtCore.QEvent.Type.FocusAboutToChange] and type(object) in [QtWidgets.QLineEdit]:
            if (object == self.editText):
                self.__onEditValueChanged()
                return True
        return False

    def value(self) -> float:
        return float(self.editText.text())

    def setup(self):
        self.slider.valueChanged.connect(lambda: self.__onSliderValueChanged())
        self.editText.setValidator(QtGui.QDoubleValidator(0, 10, 3))
        self.editText.installEventFilter(self)

    def __onSliderValueChanged(self):
        value = str(self.slider.value() / 1000)
        self.editText.setText(value)

    def __onEditValueChanged(self):
        self.slider.setValue(int(float(self.editText.text()) * 1000))
    

class EventHandler(QtCore.QObject):
    def __init__(self, ui: Ui_MainWindow): 
        super(EventHandler, self).__init__()      
        self.kpSlider = ComboSlider(ui.kpSlider, ui.kpEdit)
        self.kiSlider = ComboSlider(ui.kiSlider, ui.kiEdit)
        self.kdSlider = ComboSlider(ui.kdSlider, ui.kdEdit)

        self.baudRateCombo = ui.baudRateCombo
        self.serialPortCombo = ui.serialPortCombo

        self.sendPidToSerialButton = ui.sendPidToSerialButton
        self.serialToggleButton = ui.serialToggleButton

        self.consoleScroll = ui.consoleArea
        self.consoleText = ui.consoleText

        self.serial = SerialDevice()
        
    def setup(self):
        self.baudRateCombo.setCurrentIndex(4)
        self.serialPortCombo.addItems(serial_ports())

        self.sendPidToSerialButton.setEnabled(False)
        self.sendPidToSerialButton.clicked.connect(lambda: self.sendViaSerialPort())

        self.serialToggleButton.clicked.connect(lambda: self.toggleSerial())

        self.kpSlider.setup()
        self.kiSlider.setup()
        self.kdSlider.setup()
        
    def toggleSerial(self):
        if (self.serial.isStarted()):
            self.serial.stop()
            self.serialToggleButton.setText("Start listening")
            self.sendPidToSerialButton.setEnabled(False)
        else:
            baudRate = int(self.baudRateCombo.currentText())
            serialPortDevice = self.serialPortCombo.currentText()
            self.consoleText.setText("")
            self.serial.start(serialPortDevice, baudRate, self.printSerialMessage)
            self.serialToggleButton.setText("Stop listening")
            self.sendPidToSerialButton.setEnabled(True)

    def sendViaSerialPort(self):
        kpPir = self.kpSlider.value()
        kiPir = self.kiSlider.value()
        kdPir = self.kdSlider.value()

        self.serial.send_pid(kp = kpPir, ki = kiPir, kd = kdPir)

    def printSerialMessage(self, line):
        print(f"rcv> {line}")
        message = self.consoleText.text()
        message += line + "\n"
        self.consoleText.setText(message)
        self.consoleScroll.verticalScrollBar().setSliderPosition(self.consoleText.height())

async def run_async():
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()

    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = qasync.QApplication.instance()
    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(
            qasync.functools.partial(close_future, future, loop)
        )

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    EventHandler(ui).setup()

    await future
    return True

def run():
    loop = asyncio.get_event_loop()
    try:
        qasync.run(run_async())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)

if __name__ == '__main__':
    run()