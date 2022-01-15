# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pidgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.console = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QtCore.QSize(700, 300))
        self.console.setObjectName("console")
        self.gridLayout = QtWidgets.QGridLayout(self.console)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.consoleArea = QtWidgets.QScrollArea(self.console)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleArea.sizePolicy().hasHeightForWidth())
        self.consoleArea.setSizePolicy(sizePolicy)
        self.consoleArea.setMinimumSize(QtCore.QSize(200, 200))
        self.consoleArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.consoleArea.setWidgetResizable(True)
        self.consoleArea.setObjectName("consoleArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 650, 249))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(200, 200))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.consoleText = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consoleText.sizePolicy().hasHeightForWidth())
        self.consoleText.setSizePolicy(sizePolicy)
        self.consoleText.setMinimumSize(QtCore.QSize(200, 200))
        self.consoleText.setStyleSheet("background-color: rgb(235,235,235);\n"
"color: rgb(0, 0, 0);")
        self.consoleText.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.consoleText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.consoleText.setWordWrap(True)
        self.consoleText.setIndent(0)
        self.consoleText.setObjectName("consoleText")
        self.horizontalLayout_9.addWidget(self.consoleText)
        self.consoleArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.consoleArea)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.console, 2, 0, 1, 1)
        self.serialConfig = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialConfig.sizePolicy().hasHeightForWidth())
        self.serialConfig.setSizePolicy(sizePolicy)
        self.serialConfig.setMinimumSize(QtCore.QSize(250, 130))
        self.serialConfig.setObjectName("serialConfig")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.serialConfig)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.baudRatelabel = QtWidgets.QLabel(self.serialConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baudRatelabel.sizePolicy().hasHeightForWidth())
        self.baudRatelabel.setSizePolicy(sizePolicy)
        self.baudRatelabel.setObjectName("baudRatelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.baudRatelabel)
        self.baudRateCombo = QtWidgets.QComboBox(self.serialConfig)
        self.baudRateCombo.setCurrentText("300")
        self.baudRateCombo.setMaxVisibleItems(20)
        self.baudRateCombo.setObjectName("baudRateCombo")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.baudRateCombo.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.baudRateCombo)
        self.serialPortLabel = QtWidgets.QLabel(self.serialConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialPortLabel.sizePolicy().hasHeightForWidth())
        self.serialPortLabel.setSizePolicy(sizePolicy)
        self.serialPortLabel.setObjectName("serialPortLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.serialPortLabel)
        self.serialPortCombo = QtWidgets.QComboBox(self.serialConfig)
        self.serialPortCombo.setObjectName("serialPortCombo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.serialPortCombo)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.serialToggleButton = QtWidgets.QPushButton(self.serialConfig)
        self.serialToggleButton.setObjectName("serialToggleButton")
        self.horizontalLayout_11.addWidget(self.serialToggleButton)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.serialConfig, 0, 0, 1, 1)
        self.pid = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pid.sizePolicy().hasHeightForWidth())
        self.pid.setSizePolicy(sizePolicy)
        self.pid.setMinimumSize(QtCore.QSize(300, 200))
        self.pid.setObjectName("pid")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pid)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kpLabel = QtWidgets.QLabel(self.pid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kpLabel.sizePolicy().hasHeightForWidth())
        self.kpLabel.setSizePolicy(sizePolicy)
        self.kpLabel.setObjectName("kpLabel")
        self.horizontalLayout_3.addWidget(self.kpLabel)
        self.kpSlider = QtWidgets.QSlider(self.pid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kpSlider.sizePolicy().hasHeightForWidth())
        self.kpSlider.setSizePolicy(sizePolicy)
        self.kpSlider.setMinimumSize(QtCore.QSize(64, 0))
        self.kpSlider.setMaximum(5000)
        self.kpSlider.setSingleStep(10)
        self.kpSlider.setPageStep(100)
        self.kpSlider.setProperty("value", 3550)
        self.kpSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kpSlider.setObjectName("kpSlider")
        self.horizontalLayout_3.addWidget(self.kpSlider)
        self.kpEdit = QtWidgets.QLineEdit(self.pid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kpEdit.sizePolicy().hasHeightForWidth())
        self.kpEdit.setSizePolicy(sizePolicy)
        self.kpEdit.setMinimumSize(QtCore.QSize(80, 30))
        self.kpEdit.setMaximumSize(QtCore.QSize(80, 30))
        self.kpEdit.setObjectName("kpEdit")
        self.horizontalLayout_3.addWidget(self.kpEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.kiLabel = QtWidgets.QLabel(self.pid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kiLabel.sizePolicy().hasHeightForWidth())
        self.kiLabel.setSizePolicy(sizePolicy)
        self.kiLabel.setObjectName("kiLabel")
        self.horizontalLayout_5.addWidget(self.kiLabel)
        self.kiSlider = QtWidgets.QSlider(self.pid)
        self.kiSlider.setMaximum(1000)
        self.kiSlider.setPageStep(100)
        self.kiSlider.setProperty("value", 48)
        self.kiSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kiSlider.setObjectName("kiSlider")
        self.horizontalLayout_5.addWidget(self.kiSlider)
        self.kiEdit = QtWidgets.QLineEdit(self.pid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kiEdit.sizePolicy().hasHeightForWidth())
        self.kiEdit.setSizePolicy(sizePolicy)
        self.kiEdit.setMinimumSize(QtCore.QSize(80, 30))
        self.kiEdit.setMaximumSize(QtCore.QSize(80, 30))
        self.kiEdit.setObjectName("kiEdit")
        self.horizontalLayout_5.addWidget(self.kiEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.kdLabel = QtWidgets.QLabel(self.pid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kdLabel.sizePolicy().hasHeightForWidth())
        self.kdLabel.setSizePolicy(sizePolicy)
        self.kdLabel.setObjectName("kdLabel")
        self.horizontalLayout_4.addWidget(self.kdLabel)
        self.kdSlider = QtWidgets.QSlider(self.pid)
        self.kdSlider.setMaximum(5000)
        self.kdSlider.setSingleStep(10)
        self.kdSlider.setPageStep(100)
        self.kdSlider.setProperty("value", 2050)
        self.kdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kdSlider.setObjectName("kdSlider")
        self.horizontalLayout_4.addWidget(self.kdSlider)
        self.kdEdit = QtWidgets.QLineEdit(self.pid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kdEdit.sizePolicy().hasHeightForWidth())
        self.kdEdit.setSizePolicy(sizePolicy)
        self.kdEdit.setMinimumSize(QtCore.QSize(80, 30))
        self.kdEdit.setMaximumSize(QtCore.QSize(80, 30))
        self.kdEdit.setObjectName("kdEdit")
        self.horizontalLayout_4.addWidget(self.kdEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sendPidToSerialButton = QtWidgets.QPushButton(self.pid)
        self.sendPidToSerialButton.setObjectName("sendPidToSerialButton")
        self.horizontalLayout_6.addWidget(self.sendPidToSerialButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.pid, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PID to Serial"))
        self.console.setTitle(_translate("MainWindow", "Serial console"))
        self.consoleText.setText(_translate("MainWindow", "Press start to see here the messages received from serial device.\n"
"Make sure to adjust baud rate and serial port accordingly"))
        self.serialConfig.setTitle(_translate("MainWindow", "Serial port"))
        self.baudRatelabel.setText(_translate("MainWindow", "Baud rate"))
        self.baudRateCombo.setItemText(0, _translate("MainWindow", "300"))
        self.baudRateCombo.setItemText(1, _translate("MainWindow", "1200"))
        self.baudRateCombo.setItemText(2, _translate("MainWindow", "2400"))
        self.baudRateCombo.setItemText(3, _translate("MainWindow", "4800"))
        self.baudRateCombo.setItemText(4, _translate("MainWindow", "9600"))
        self.baudRateCombo.setItemText(5, _translate("MainWindow", "19200"))
        self.baudRateCombo.setItemText(6, _translate("MainWindow", "28800"))
        self.baudRateCombo.setItemText(7, _translate("MainWindow", "38400"))
        self.baudRateCombo.setItemText(8, _translate("MainWindow", "57600"))
        self.baudRateCombo.setItemText(9, _translate("MainWindow", "74880"))
        self.baudRateCombo.setItemText(10, _translate("MainWindow", "115200"))
        self.baudRateCombo.setItemText(11, _translate("MainWindow", "230400"))
        self.baudRateCombo.setItemText(12, _translate("MainWindow", "250000"))
        self.baudRateCombo.setItemText(13, _translate("MainWindow", "500000"))
        self.baudRateCombo.setItemText(14, _translate("MainWindow", "1000000"))
        self.baudRateCombo.setItemText(15, _translate("MainWindow", "2000000"))
        self.serialPortLabel.setText(_translate("MainWindow", "Serial port"))
        self.serialToggleButton.setText(_translate("MainWindow", "Start listening"))
        self.pid.setTitle(_translate("MainWindow", "PID constants"))
        self.kpLabel.setText(_translate("MainWindow", "kp"))
        self.kpEdit.setText(_translate("MainWindow", "3.55"))
        self.kiLabel.setText(_translate("MainWindow", "ki"))
        self.kiEdit.setText(_translate("MainWindow", "0.048"))
        self.kdLabel.setText(_translate("MainWindow", "kd"))
        self.kdEdit.setText(_translate("MainWindow", "2.05"))
        self.sendPidToSerialButton.setText(_translate("MainWindow", "Send PID to Arduino"))
