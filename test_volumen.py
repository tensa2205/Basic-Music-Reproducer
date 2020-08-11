import PySimpleGUI as sg
from pygame import mixer
mixer.init()

layout = [
    [sg.Button('Volumen')],
    [sg.Slider(range=(1,100),default_value=7,size=(7,20),key ='sli',enable_events=True,visible=False)],
    [sg.Button('Salir',key = 'ex')]
]
window = sg.Window("",layout,size = (300,300))
while True:
    event,values = window.read()
    if event is None:
        values['sli'] = 7
        break
    if event in 'ex':
        break
    if event in 'Volumen':
        window['sli'].update(visible=True)

mixer.music.set_volume(values['sli'] * 0.01)
print(mixer.music.get_volume())  