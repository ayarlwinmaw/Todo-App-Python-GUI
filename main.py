import functions
import FreeSimpleGUI as fsg
import time

fsg.theme('DarkTeal4')

clock = fsg.Text('', key='clock')
label = fsg.Text("Type in a todo")
input_box = fsg.InputText(tooltip="Enter a todo", key="todo")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=[45, 10]
)
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")


window = fsg.Window('My Todo App',
                    layout=[
                        [clock],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]
                    ],
                    font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first!", font=('Helvetica', 12))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fsg.popup("Please select an item first!", font=('Helvetica', 12))

        case "Exit":
            break

        case fsg.WINDOW_CLOSED:
            break

window.close()