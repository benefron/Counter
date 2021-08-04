import PySimpleGUI as sg
import serial
import time
import math
import serial.tools.list_ports

import PySimpleGUI as sg


sg.theme('DarkBrown1')

ports = serial.tools.list_ports.comports()
portList = [port.name for port in ports]
layoutPop = [  [sg.Text('Please choose the Arduino COM port', size=(20, 2), justification='center')],
            [sg.InputCombo(portList,key= '-PORT-',enable_events=True)]]

windowPop = sg.Window('COM port',layoutPop)

while True:                  # the event loop
    event, values = windowPop.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-PORT-']:    # if something is highlighted in the list
        port_name = values['-PORT-']
        break
windowPop.close()

# linux version
ser = serial.Serial(f"/dev/{port_name}",'9600',timeout=1)
# Windows version
# ser = serial.Serial(port_name,'9600',timeout=1)
sg.theme('DarkBrown1')


layout = [  [sg.Text('x', size=(20, 2), justification='center'),sg.T(' ' * 10),sg.Text('y', size = (20,2), justification='center')],
            [sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUTX-'),sg.Button('zeroX'), sg.T(' ' *5),sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUTY-'),sg.Button('zeroY')],
            [sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUTZ-'),sg.Button('zeroZ'), sg.T(' ' *5),sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUTD-'),sg.Button('zeroDepth')],
          [sg.T(' ' * 5),sg.Quit(),sg.Button('countX')],
         [sg.Button('Zero All')]]

window = sg.Window('Stopwatch Timer', layout)

timer_running, counter = True, 0
counterX=0
counterY = 0
counterZ = 0
counterD = 0


while True:                                 # Event Loop
    event, values = window.read(timeout=0.3) # Please try and use as high of a timeout value as you can
    window['-OUTPUTX-'].update('{:04d}.{:02d}'.format((counterX)//200,abs((counterX)//2)%100))
    window['-OUTPUTY-'].update('{:05d}'.format((counterY)))
    window['-OUTPUTZ-'].update('{:05d}'.format((counterZ)))
    window['-OUTPUTD-'].update('{:05d}'.format((counterD)))
    line = ser.readline()

    if event in (sg.WIN_CLOSED, 'Quit'):             # if user closed the window using X or clicked Quit button
        ser.close()
        break
    elif event == 'Zero All':
        counterX=0
        counterY = 0
        counterZ = 0
        counterD = 0
        window['-OUTPUTX-'].update('{:04d}.{:02d}'.format((counterX),(counterX)))
    if line:
        window['-OUTPUTX-'].update('{:04d}.{:02d}'.format((counterX//200),(abs(counterX//2)%100)))
        try:
            string = line.decode()  # convert the byte string to a unicode string
            counterX += int(string) # 
        except:
            counterX=0
                
window.close()
ser.close()
