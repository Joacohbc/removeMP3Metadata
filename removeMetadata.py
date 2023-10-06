import os
import sys
from mutagen.mp3 import MP3

TEXT_ENCODING = 'utf8'

# Verifico que se haya pasado un path como argumento
if (len(sys.argv) > 1):
    fpath = sys.argv[1]
else:
    # Sino tomo el path del script
    fpath = os.path.abspath(os.path.dirname(sys.argv[0]))


# Recorro todos los archivos del directorio
for fn in os.listdir(fpath):

    # Obtengo el nombre completo del archivo
    fname = os.path.join(fpath, fn)

    # Si es un archivo .mp3
    if fname.lower().endswith('.mp3'):
        mp3 = MP3(fname)        
        try:
            mp3.delete()
            mp3.save()
            print(f"ID3 tag removed from {fn}")
        except:
            print('no ID3 tag')

print('Done')