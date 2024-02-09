
import shutil
import os


ruta= os.path.join(os.path.dirname(__file__), "Proyecto_Dia_9.zip")
shutil.unpack_archive(ruta,'C:\\Users\\gabys\\Desktop','zip')
