import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose2 = sg.FolderBrowse("Choose", key="folder")

compress = sg.Button("Compress")
output = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose1],
                           [label2, input2, choose2],
                           [compress,output]])
while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed !")

window.close()



