from pygame import mixer
import os

class MusicPlayer:

    def __init__(self):
        mixer.init()
        self._path = ''
        self._song_list = []
        self._pointer = None
    
    def set_path(self,directory):
        '''
            Es correcto decir que cada vez que se cambia el path, debe cambiarse la lista de canciones
        '''
        self._path = directory
        self._pointer = 0
        self.__set_list(directory)

    def __set_list(self,dir):
        try:
            list_aux = os.listdir(dir)
        except:
            None
        for file in list_aux:
            if file[-3:] == 'mp3': self._song_list.append(file)

    def set_pointer(self, new_pointer):
        if new_pointer >= 0 and new_pointer < len(self._song_list): #Posición máxima, Len(lista) -1.
            self._pointer = new_pointer
    
    def play(self):
        mixer.music.load(self._path + self._song_list[self._pointer]) #Carga la canción en el string path + canción.mp3
        mixer.music.play() #Empieza la canción.

    def resume(self):
        mixer.music.unpause() #Despausa la canción

    def pause(self):
        mixer.music.pause() #Pausa temporalmente la canción
    
    def stop(self):
        mixer.music.stop() #Pausa la canción pero no hace el unload
        mixer.music.unload() #Hago el unload

    def repeat(self):
        mixer.music.rewind() #Repite la canción

    def next_song(self):
        ''' Sí la canción está en stream activo (sonando o en pause), debería detenerla y avanzar a la siguiente,
                caso contrario -> hago play.
        '''
        if self._pointer == (len(self._song_list) -1): #Sí mi puntero está al final, debo volverlo al inicio de nuevo.
            self._pointer = 0
        else: #Sino sigo avanzando en 1.
            self._pointer += 1

        if(mixer.music.get_busy()):
            self.stop()
            self.play()
        else:
            self.play()