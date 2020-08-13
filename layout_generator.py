def get_layout():
    import PySimpleGUI as sg

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
        [sg.Text(' '*6),sg.Text('Unknown song',font = (None,14), key = '-TITULO-',justification = 'center')],
        [sg.Text(' '*7),sg.Text('Unknown artist',font = (None,10), key = '-ARTISTA-',justification = 'center')]
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
    return layout