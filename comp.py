import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose2 = sg.FolderBrowse("Choose")

compress = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose1],
                           [label2, input2, choose2],
                           [compress]])

window.read()
window.close()
