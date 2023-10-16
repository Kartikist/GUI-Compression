import functions as fn
import PySimpleGUI as pg

label = pg.Text("Enter a To-Do: ")
input_box = pg.InputText(tooltip="Enter to do")
add_button = pg.Button("Add")

window = pg.Window("To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
