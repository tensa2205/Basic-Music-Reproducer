import PySimpleGUI as sg
from tinytag import TinyTag
from music_player import MusicPlayer
from convert import convert_to_bytes
from layout_generator import get_layout
import choose_from_list as list_songs_window

sg.theme('Default1')

def set_metadata(window,player):
    tag = TinyTag.get(player.get_current_song(),image=True)
    artist = tag.artist

    try:
        image = convert_to_bytes(tag.get_image(),resize = (210,210))
    except:
        image = convert_to_bytes('resources/defecto.png',resize = (210,210))

    window['-TITULO-'].update(tag.title if artist != None else 'Unknown song') #Cambía el titulo, sólo si tiene la metadata.
 
    if artist != window['-ARTISTA-']: #cambia el artista
            window['-ARTISTA-'].update(tag.artist if artist != None else 'Unknown artist')
    if image != window['-CARATULA-']: #cambia la caratula sí es posible
        try:
            window['-CARATULA-'].update(data = image)
        except:
            window['-CARATULA-'].update(filename = image)

def main():
    layout = get_layout()

    window = sg.Window('Basic Music Reproducer', layout, size = (350,600))
    

    player = MusicPlayer()

    volume_switch = True
    is_playing = True
    
    while True:
        event,values = window.read()
        if event in (None,'-EXIT-'):
            break

        if event == '-PLAY-':
            if is_playing: #Play , DEBO cambiar imagen y etc. a ver si messirve
                player.play()
                set_metadata(window,player)
            else: #Resume
                player.resume()
                is_playing = True

        elif event == '-PAUSE-':
            player.pause()
            is_playing = False

        elif event == '-STOP-':
            player.stop()

        elif event == '-RESTART-':
            player.repeat()

        elif event  == '-NEXT-':
            player.next_song()
            set_metadata(window,player)

        if event == '-LIST-':
            window.hide()
            choice = list_songs_window.main(player._beautiful_list)
            window.un_hide()
            if choice != None:
                player.set_pointer(choice)
                player.play()
                set_metadata(window,player)

        if event == '-VOLUME-':
            if volume_switch:
                window['volumen'].update(visible = True)
                volume_switch = False
            else:
                window['volumen'].update(visible = False)
                volume_switch = True

        if event == 'volumen': #Se cambió el volumen.
            player.set_volume(values['volumen'])

        if event == '-FOLDER-':
            player.set_path(values['-FOLDER-'])
            if values['-FOLDER-'] != '' and player.get_availability() :
                window['-PLAY-'].update(disabled = False)
                window['-PAUSE-'].update(disabled = False)
                window['-STOP-'].update(disabled = False)
                window['-RESTART-'].update(disabled = False)
                window['-NEXT-'].update(disabled = False)
                window['-LIST-'].update(disabled = False)
    
    window.close()

if __name__ == "__main__":
    main()
