import PySimpleGUI as sg
import os
sg.theme('Default1')

def main():
    caratula = [[sg.Image(filename='resources/defecto.png',size=(210,210),key='-CARATULA-')]]
    volumen = [
        [sg.Text(' '*3),sg.Slider(range=(1,100),default_value = 50,size = (15,6),key = 'volumen',enable_events = True,visible = True,orientation='horizontal')]
    ]
    controladores = [
        [sg.Button(image_filename='resources/list.png',border_width=0,size = (1,1),key = '-LIST-'),sg.Text(' '*50),sg.Button(image_filename='resources/volume.png',border_width=0,size = (1,1),key = '-VOLUME-')]
    ]
    principal = [
        [sg.Text(' '*15) ,sg.Button(image_filename = 'resources/stop.png',border_width=0,size = (1,1),key = '-STOP-')],
        [sg.Text(' '*2), sg.Button(image_filename = 'resources/restart.png',border_width=0,size = (1,1), key = '-RESTART-'), sg.Button(image_filename = 'resources/play.png',border_width=0,size = (1,1),key = '-PLAY-'),sg.Button(image_filename = 'resources/next.png', border_width=0,size = (11,1), key = '-NEXT-')],
        [sg.Text(' '*15), sg.Button(image_filename = 'resources/pause.png',border_width=0, size= (1,1), key = '-PAUSE-')]
    ]
    titulo = [
        [sg.Text(' '*10),sg.Text('Automatic',font = (None,14), key = '-TITULO-',justification = 'center')],
        [sg.Text(' '*11),sg.Text('Red Velvet',font = (None,10), key = '-ARTISTA-',justification = 'center')]
    ]

    buscar_final = [
        [sg.In(visible = False,enable_events=True,key='-FOLDER-'),sg.FolderBrowse(),sg.Text(' '*48), sg.Button(image_filename='resources/exit.png', border_width=0, key = '-EXIT-')],
    ]

    layout = [
        [sg.Text(' '*11),sg.Column(caratula)],
        [sg.Column(controladores)],
        [sg.Text(' '*11),sg.Column(volumen)],
        [sg.Text(' '*11),sg.Column(principal)],
        [sg.Text(' '*11),sg.Column(titulo)],
        [sg.Column(buscar_final)],
    ]

    file_list = [] 

    window = sg.Window('Basic Music Reproducer', layout, size = (350,590))
    
    while True:
        event,values = window.read()
        if event in (None,'-EXIT-'):
            break
        if event == '-PLAY-':
            pass
        elif event == '-PAUSE-':
            pass
        elif event == '-STOP-':
            pass
        elif event == '-RESTART-':
            pass
        elif event  == '-NEXT-':
            pass
        if event == '-LIST':
            pass
        if event == '-VOLUME-':
            pass
        if event == '-FOLDER-':
            print(values['-FOLDER-'])
            folder = values['-FOLDER-']
            try:
                file_list = os.listdir(folder)
            except:
                None
    
    print(file_list)
    
    window.close()

if __name__ == "__main__":
    main()
