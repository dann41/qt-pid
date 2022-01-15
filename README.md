# Generate pidgui.py from pidgui.ui
``` 
pyuic5 pidgui.ui -o pidgui.py
```

# Run application
``` 
python pid.py 
``` 

# Usage
1. Select port and baud rate
2. Press start listening button to connect and start receiving messages from serial device
3. Adjust kp, ki, and kd accordingly
4. Press "Send PID to Arduino" button to send the selected values
5. Repeat step 4 as many times as you want
6. Stop listening (or just close the windows) to close the connection to the serial device
