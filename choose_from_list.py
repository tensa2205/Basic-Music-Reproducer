import PySimpleGUI as sg 

def set_layout(songs):
    title = [[sg.Text('Song List', font = (None,15), justification = 'center')]]
    song_list = [
        [sg.Listbox(values=songs, key='-CHOSEN-',enable_events=True,size=(50,25))]
    ]
    exit = [[sg.Button(image_filename = 'resources/exit.png', border_width = 0, key='-EXIT-')]]

    layout = [
        [sg.Column(title)],
        [sg.Column(song_list)],
        [sg.Column(exit)]
    ]

    return layout


def main(beautiful_list):

    layout = set_layout(beautiful_list)

    window = sg.Window('Basic Music Reproducer', layout, size= (400,590))

    choice = None

    while True:
        event, values = window.read()

        if event in (None,'-EXIT-'):
            break

        if event in '-CHOSEN-':
            choice = beautiful_list.index(values['-CHOSEN-'][0])
            break
    window.close()

    return choice