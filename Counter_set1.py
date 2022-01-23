import PySimpleGUI as sg
import serial
import time
import math
import serial.tools.list_ports


import PySimpleGUI as sg

import PySimpleGUI as sg


sg.theme('Dark Green 7')

#ports = serial.tools.list_ports.comports()
#portList = [port.name for port in ports]
#layoutPop = [  [sg.Text('Please choose the Arduino COM port', size=(20, 2), justification='center',font=('Ariel',15))],
 #           [sg.T(' ' * 5),sg.InputCombo(portList,key= '-PORT-',enable_events=True,size=(10, 4),font=('Ariel',15))]]

#windowPop = sg.Window('COM port',layoutPop,location=(800,500))

#while True:                  # the event loop
#    event, values = windowPop.read()
#    if event == sg.WIN_CLOSED:
#        break
#    if values['-PORT-']:    # if something is highlighted in the list
#        port_name = values['-PORT-']
#        break
#windowPop.close()

port_name = 'COM7'
# linux version
# ser = serial.Serial(f"/dev/{port_name}",'9600',timeout=1)
# Windows version
ser = serial.Serial(port_name,'9600',timeout=1)
#sg.theme('Dark Green 7')


layout = [  
            [sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', key='-OUTPUTXL-',border_width=5,relief='groove'),
             sg.Button('zeroXL'), sg.T(' ' *5),sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', 
                                                      key='-OUTPUTYL-',border_width=5,relief='groove'),sg.Button('zeroYL')],
            
            [sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', key='-OUTPUTZL-',border_width=5,relief='groove'),sg.Button('zeroZL'), sg.T(' ' *5),
             sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', key='-OUTPUTDL-',border_width=5,relief='groove'),sg.Button('zeroDepthL')
            ],
          [sg.Button('Zero All L')],
    [sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', key='-OUTPUTXR-',border_width=5,relief='groove'),
             sg.Button('zeroXR'), sg.T(' ' *5),sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', 
                                                      key='-OUTPUTYR-',border_width=5,relief='groove'),sg.Button('zeroYR')],[sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', key='-OUTPUTZR-',border_width=5,relief='groove'),sg.Button('zeroZR'), sg.T(' ' *5),
             sg.Text(size=(10, 1), font=('Helvetica', 20), justification='center', key='-OUTPUTDR-',border_width=5,relief='groove'),sg.Button('zeroDepthR')
            ]
            ,[sg.Button('Zero All R')],[sg.T(' ')],[sg.Quit()]]

window = sg.Window('Monitor', layout,location=(600,500))


counterXL=0
counterYL = 0
counterZL = 0
counterDL = 0
counterXR=0
counterYR = 0
counterZR = 0
counterDR = 0


while True:                                 # Event Loop
    event, values = window.read(timeout=1) # Please try and use as high of a timeout value as you can
    window['-OUTPUTXL-'].update('{:04d}.{:02d}'.format((counterXL)//200,abs((counterXL)//2)%100))
    window['-OUTPUTYL-'].update('{:04d}.{:02d}'.format((counterYL)//200,abs((counterYL)//2)%100))
    window['-OUTPUTZL-'].update('{:04d}.{:02d}'.format((counterZL)//200,abs((counterZL)//2)%100))
    window['-OUTPUTDL-'].update('{:04d}.{:02d}'.format((counterDL)//200,abs((counterDL)//2)%100))
    window['-OUTPUTXR-'].update('{:04d}.{:02d}'.format((counterXR)//200,abs((counterXR)//2)%100))
    window['-OUTPUTYR-'].update('{:04d}.{:02d}'.format((counterYR)//200,abs((counterYR)//2)%100))
    window['-OUTPUTZR-'].update('{:04d}.{:02d}'.format((counterZR)//200,abs((counterZR)//2)%100))
    window['-OUTPUTDR-'].update('{:04d}.{:02d}'.format((counterDR)//200,abs((counterDR)//2)%100))
    line = ser.readline()

    if event in (sg.WIN_CLOSED, 'Quit'):             # if user closed the window using X or clicked Quit button
        
        break
    elif event == 'Zero All L':
        counterXL=0
        counterYL = 0
        counterZL = 0
        counterDL = 0
    elif event == 'Zero All R':
        counterXR=0
        counterYR = 0
        counterZR = 0
        counterDR = 0
        
        #window['-OUTPUTXL-'].update('{:04d}.{:02d}'.format((counterXL),(counterXL)))
        #window['-OUTPUTYL-'].update('{:04d}.{:02d}'.format((counterYL),(counterYL)))
        #window['-OUTPUTZL-'].update('{:04d}.{:02d}'.format((counterZL),(counterZL)))
        #window['-OUTPUTDL-'].update('{:04d}.{:02d}'.format((counterDL),(counterDL)))
    elif event == 'zeroXL':
        counterXL=0
        #window['-OUTPUTXL-'].update('{:04d}.{:02d}'.format((counterXL),(counterXL)))
    elif event == 'zeroYL':
        counterYL=0
        #window['-OUTPUTYL-'].update('{:04d}.{:02d}'.format((counterYL),(counterYL)))
    elif event == 'zeroZL':
        counterZL=0
        #window['-OUTPUTZL-'].update('{:04d}.{:02d}'.format((counterZL),(counterZL)))
    elif event == 'zeroDepthL':
        counterDL=0
    elif event == 'zeroXR':
        counterXR=0
        #window['-OUTPUTXL-'].update('{:04d}.{:02d}'.format((counterXL),(counterXL)))
    elif event == 'zeroYR':
        counterYR=0
        #window['-OUTPUTYL-'].update('{:04d}.{:02d}'.format((counterYL),(counterYL)))
    elif event == 'zeroZR':
        counterZR=0
        #window['-OUTPUTZL-'].update('{:04d}.{:02d}'.format((counterZL),(counterZL)))
    elif event == 'zeroDepthR':
        counterDR=0
        #window['-OUTPUTDL-'].update('{:04d}.{:02d}'.format((counterDL),(counterDL)))
    if line:
        #window['-OUTPUTXL-'].update('{:04d}.{:02d}'.format((counterXL//200),(abs(counterXL//2)%100)))
        try:
            string = line.decode()  # convert the byte string to a unicode string
            if string[1] == 'L':
                if string[0] == 'X':
                    counterXL += int(string[2:]) # 
                elif string[0] == 'Y':
                    counterYL += int(string[2:])
                elif string[0] == 'Z':
                    counterZL += int(string[2:])
                elif string[0] == 'D':
                    counterDL += int(string[2:])
            if string[1] == 'R':
                if string[0] == 'X':
                    counterXR += int(string[2:]) # 
                elif string[0] == 'Y':
                    counterYR += int(string[2:])
                elif string[0] == 'Z':
                    counterZR += int(string[2:])
                elif string[0] == 'D':
                    counterDR += int(string[2:])
        except:
            counterXL=0
            counterYL=0
            counterZL=0
            counterDL=0
            counterXR=0
            counterYR=0
            counterZR=0
            counterDR=0
                
window.close()
ser.close()