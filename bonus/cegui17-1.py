import FreeSimpleGUI as sg

lbl_feet = sg.Text('Enter feet: ')
input_feet = sg.InputText(key='feet')

lbl_inches = sg.Text('Enter inches: ')
input_inches = sg.InputText(key='inches')

btn_convert = sg.Button('Convert', key='convert')
lbl_result = sg.Text('Result: ', key='result')

window = sg.Window("Convertor", layout=[
    [lbl_feet, input_feet],
    [lbl_inches, input_inches],
    [btn_convert, lbl_result]
])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'convert':
            feet, inches = float(values['feet']), float(values['inches'])
            meters = feet * 0.3048 + inches * 0.0254
            window['result'].update(value=f"{meters} m")
        case sg.WIN_CLOSED:
            break

window.close()