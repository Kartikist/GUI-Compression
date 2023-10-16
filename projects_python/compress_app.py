import PySimpleGUI as pg

label1 = pg.Text("Choose file to compress.")
textbox1 = pg.Input()
choosebutton1 = pg.FilesBrowse()

label2 = pg.Text("Choose destination folder.")
textbox2 = pg.Input()
choosebutton2 = pg.FolderBrowse()

compress = pg.Button("Compress")

window = pg.Window("File Compressor", layout=[[label1,textbox1,choosebutton1],[label2,textbox2,choosebutton2],[compress]])
window.read()
window.close()





