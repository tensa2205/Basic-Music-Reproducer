from pygame import mixer
from tinytag import TinyTag
import os


class MusicPlayer:


    def __init__(self):
        mixer.init()
        self._path = ''
        self._pointer = None
        self._available = False
        self._path_songs = []
        self._beautiful_list = []
        self._supported_formats = ('mp3','flac','ogg','wav')
    
    def set_path(self,directory):
        '''
            Es correcto decir que cada vez que se cambia el path, debe cambiarse la lista de canciones
        '''
        self._path = directory
        self._pointer = 0
        self.__set_list(directory)

    def __set_list(self,dir):
        new_list = []
        list_aux = []

        try:
            list_aux = os.listdir(dir)
        except:
            None
        
        new_list = [self._path + '/' + file for file in list_aux if file[-3:] in self._supported_formats or file[-4:] in self._supported_formats]

        if new_list: #Chequea sí la lista tiene elementos.
            self._path_songs = new_list.copy()
            self._available = True
            self.__set_beautiful_list()
        else:
            self._available = False

    def set_pointer(self, new_pointer):
        if new_pointer >= 0 and new_pointer < len(self._path_songs): #Posición máxima, Len(lista) -1.
            self._pointer = new_pointer
    
    def get_current_song(self):
        return self._path_songs[self._pointer]

    def get_availability(self):
        return self._available
    
    def play(self):
        print(self.get_current_song())
        mixer.music.load(self.get_current_song()) #Carga la canción en el string path + canción.mp3
        mixer.music.play() #Empieza la canción.

    def resume(self):
        mixer.music.unpause() #Despausa la canción

    def pause(self):
        mixer.music.pause() #Pausa temporalmente la canción
    
    def stop(self):
        mixer.music.stop() #Pausa la canción pero no hace el unload
        #mixer.music.unload() #Hago el unload

    def repeat(self):
        mixer.music.rewind() #Repite la canción

    def next_song(self):
        ''' Sí la canción está en stream activo (sonando o en pause), debería detenerla y avanzar a la siguiente,
                caso contrario -> hago play.
        '''
        if self._pointer == (len(self._path_songs) -1): #Sí mi puntero está al final, debo volverlo al inicio de nuevo.
            self._pointer = 0
        else: #Sino sigo avanzando en 1.
            self._pointer += 1

        if(mixer.music.get_busy()):
            self.stop()
            self.play()
        else:
            self.play()
    
    def set_volume(self,new_volume):
        mixer.music.set_volume(new_volume * 0.01)

    def get_all_paths(self):
        return self._path_songs
    
    def __set_beautiful_list(self):
        new_list = []

        for song in self._path_songs:
            try:
                metadata = TinyTag.get(song)
                aux = metadata.title + ' - ' + metadata.artist
            except:
                aux = song[song.rfind('/')+1:]
            new_list.append(aux)
    
        self._beautiful_list = new_list.copy()