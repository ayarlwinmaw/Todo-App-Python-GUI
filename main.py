import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter a todo", key="todo")
add_button = fsg.Button("Add")

window = fsg.Window('My Todo App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case fsg.WINDOW_CLOSED:
            break

window.close()