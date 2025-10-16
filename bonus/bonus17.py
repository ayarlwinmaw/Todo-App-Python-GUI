import FreeSimpleGUI as sg
from zip_extractor import extract_archive


sg.theme('Black')

label1 = sg.Text("Select an archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse(button_text="Choose", key="archive")

label2 = sg.Text("Select dest folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse(button_text="Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window(title="Archive Extractor",
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [extract_button, output_label]
                   ])
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Extract":
            archive_path = values["archive"]
            dest_folder = values["folder"]
            extract_archive(archive_path, dest_folder)
            window["output"].update("Archive Extracted!")
        case sg.WIN_CLOSED:
            break

window.close()