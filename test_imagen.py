from tinytag import TinyTag
from convert import convert_to_bytes
import PySimpleGUI as sg



tag = TinyTag.get('Ice Cream Cake.mp3',image=True)
print("Cancion de ", tag.artist)

imagen = tag.get_image()


layout = [
    [sg.Image(data=convert_to_bytes(imagen,resize=(250,250)))]
]
window = sg.Window("Una ventana",layout,size = (300,300))

event,values = window.read()
