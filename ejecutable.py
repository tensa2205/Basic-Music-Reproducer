import PySimpleGUI as sg
import os
from music_player import MusicPlayer
sg.theme('Default1')

def main():
    caratula = [[sg.Image(filename='resources/defecto.png',size=(210,210),key='-CARATULA-')]]
    volumen = [
        [sg.Text(' '*3),sg.Slider(range=(1,100),default_value = 50,size = (15,6),key = 'volumen',enable_events = True,visible = False,orientation='horizontal')]
    ]
    controllers = [
        [sg.Button(image_filename='resources/list.png',border_width=0,size = (1,1),key = '-LIST-'),sg.Text(' '*50),sg.Button(image_filename='resources/volume.png',border_width=0,size = (1,1),key = '-VOLUME-')]
    ]
    principal = [
        [sg.Text(' '*15) ,sg.Button(image_filename = 'resources/stop.png',border_width=0,size = (1,1),key = '-STOP-',disabled = True)],
        [sg.Text(' '*2), sg.Button(image_filename = 'resources/restart.png',border_width=0,size = (1,1), key = '-RESTART-',disabled = True), sg.Button(image_filename = 'resources/play.png',border_width=0,size = (1,1),key = '-PLAY-',disabled = True),sg.Button(image_filename = 'resources/next.png', border_width=0,size = (11,1), key = '-NEXT-',disabled = True)],
        [sg.Text(' '*15), sg.Button(image_filename = 'resources/pause.png',border_width=0, size= (1,1), key = '-PAUSE-',disabled = True)]
    ]
    title = [
        [sg.Text(' '*10),sg.Text('Automatic',font = (None,14), key = '-TITULO-',justification = 'center')],
        [sg.Text(' '*11),sg.Text('Red Velvet',font = (None,10), key = '-ARTISTA-',justification = 'center')]
    ]

    search_end = [
        [sg.In(visible = False,enable_events=True,key='-FOLDER-'),sg.FolderBrowse(),sg.Text(' '*48), sg.Button(image_filename='resources/exit.png', border_width=0, key = '-EXIT-')],
    ]

    layout = [
        [sg.Text(' '*11),sg.Column(caratula)],
        [sg.Column(controllers)],
        [sg.Text(' '*11),sg.Column(volumen)],
        [sg.Text(' '*11),sg.Column(principal)],
        [sg.Text(' '*11),sg.Column(title)],
        [sg.Column(search_end)],
    ]

    file_list = [] 

    window = sg.Window('Basic Music Reproducer', layout, size = (350,590))
    

    player = MusicPlayer()

    play_switch = True
    volume_switch = True
    
    while True:
        event,values = window.read()
        if event in (None,'-EXIT-'):
            break

        if event == '-PLAY-':
            if play_switch: #Play
                player.play()
            else: #Resume
                player.resume()

        elif event == '-PAUSE-':
            player.pause()

        elif event == '-STOP-':
            player.stop()

        elif event == '-RESTART-':
            player.repeat()

        elif event  == '-NEXT-':
            player.next_song()

        if event == '-LIST':
            pass

        if event == '-VOLUME-':
            if volume_switch:
                window['volumen'].update(visible = True)
                volume_switch = False
            else:
                window['volumen'].update(visible = False)
                volume_switch = True
                
        if event == 'volumen': #Se cambió el volumen supongo.

        if event == '-FOLDER-':
            player.set_path(values['-FOLDER-'])
            window['-PLAY-'].update(disabled = False)
            window['-PAUSE-'].update(disabled = False)
            window['-STOP-'].update(disabled = False)
            window['-RESTART-'].update(disabled = False)
            window['-NEXT-'].update(disabled = False)
    
    window.close()

if __name__ == "__main__":
    main()
