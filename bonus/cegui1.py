import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet: ")
input1 = sg.InputText()
label2 = sg.Text("Enter inches: ")
input2 = sg.InputText()
button1 = sg.Button("Convert")

window = sg.Window("Convertor", layout=[
    [label1, input1],
    [label2, input2],
    [button1]
])

window.read()
window.close()