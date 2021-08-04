Counter

This Repository holds the following items:
- Firmware code to upload to Arduino Due
- Python code for GUI to read counter positions, heart rate and control heat pad temp 
- Executable for running the GUI 


To work with the python source code the following libraries need to be installed:
- PySimpleGUI https://realpython.com/pysimplegui-python/#installing-pysimplegui
- pyserial https://pythonforundergradengineers.com/python-arduino-potentiometer.html


For the Arduino Due The Encode library needs to be installed


When running the GUI you are first asked to choose the Arduino port
After you choose the port a new window appears with the following:
- 4 counters
	each with a zero button 
	(The Depth counter can also be zeroed using a physical button)
- zero all button
	to zero all 4 counters (also can recieve long physical button push to zero)
- Quit  Button
	closes the GUI
	
- Heart monitor
	opens a pop up window and starts monitoring heart rate
- Heating pad Button
	Starts the heating pad and shows the it's temp

