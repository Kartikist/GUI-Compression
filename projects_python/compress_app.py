import PySimpleGUI as pg
import zip_creator as zc

label1 = pg.Text("Choose file to compress.")
textbox1 = pg.Input()
choosebutton1 = pg.FilesBrowse("Select", key='filepath')

label2 = pg.Text("Choose destination folder.")
textbox2 = pg.Input()
choosebutton2 = pg.FolderBrowse("Select", key='folderpath')

compress = pg.Button("Compress")

window = pg.Window("File Compressor", layout=[[label1,textbox1,choosebutton1],[label2,textbox2,choosebutton2],[compress]])
while True:
    event, values = window.read()
    print(event, values)
    filepath = values['filepath']
    folderpath = values['folderpath']
    zc.make_archive(filepath, folderpath)
window.close()





