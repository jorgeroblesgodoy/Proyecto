import os
from fileandfolder import File, Folder

def help():
  print()
  print(" ----------------- HELP ----------------")
  print("HELP - Mostrar lista de instrucciones.")
  print("Clear - CLimpiar la pantalla.")
  print("ls - Listar los archivos y folders del directorio actual.")
  print("cd nombre del folder - Navegar al subfolder.")
  print("cd .. - Navegar al directorio padre.")
  print("mkdir nombre del folder - Crear un subfolder.")
  print("move nombre - nuevo nombre - renombrar.")
  print("rm nombre - Eiminar archivo o directorio.")
  print("exit - Salir.")
  print(" ---------------------------------------")
  print()
  
# Funcion para limpiar la pantalla  
def cls():
  os.system('clear')



#Crear estructura de directorios y archivos
root = Folder("root")
Desktop = root.mkdir("MisDocumentos")
Documentos = root.mkdir("Documentos")
maths = myDocuments.mkdir("Maths")
computerscience = myDocuments.mkdir("ComputerScience")
english = myDocuments.mkdir("English")
photos = myPictures.mkdir("Photos")
cartoons = myPictures.mkdir("Cartoons")
Archivo1 = Documentos.newFile("horario.doc")

cls()


currentFolder= root
currentFolder.dir()

while True:
  print("Type HELP to view list of instructions...")
  instruction = input(">").split(" ")
  if instruction[0].upper()=="EXIT":
    print("Good bye!")
    break
  
  elif instruction[0].upper()=="HELP":
    help()
    
  elif instruction[0].upper()=="CLS":
    cls()    
    
  elif instruction[0].upper()=="DIR":
    currentFolder.dir()
    
  elif instruction[0].upper()=="DEL":
    if len(instruction)<2:
      print("You must specify a file name or a folder name when using the DEL instruction.")
    else:  
      currentFolder.delete(instruction[1])
  elif instruction[0].upper()=="RENAME":
    if len(instruction)<3:
      print("You must specify a file name or a folder name and a new name when using the DEL instruction.")
    else:  
      currentFolder.rename(instruction[1],instruction[2])      
      
  elif instruction[0].upper()=="CD":
    if len(instruction)<2:
      print("You must specify a folder name when using the CD instruction.")
    else:  
      foldername = instruction[1]
      subFolder = currentFolder.cd(foldername)
      if subFolder!=False:
        currentFolder=subFolder
        print("Current Folder: " + currentFolder.foldername)
        
  elif instruction[0].upper()=="MKDIR":
    if len(instruction)<2:
      print("You must specify a folder name when using the MKDIR instruction.")
    else:  
      foldername = instruction[1]
      currentFolder.mkdir(foldername)    
      
  else:
    print("Invalid Instruction... Type a valid isntruction or HELP for a full list of instructions.")

      