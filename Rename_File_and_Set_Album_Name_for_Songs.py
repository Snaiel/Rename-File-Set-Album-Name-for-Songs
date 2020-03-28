import os
import pyinputplus as pyip
import eyed3

directory = input("Folder directory: ")

stripName = pyip.inputBool("Do you want to remove something from the name? (True/ False)? ")
if stripName == True:
    whatToStrip = input("What do you want to strip? ")

setAlbumName = pyip.inputBool("Do you want to set the album name? (True/ False)? ")
if setAlbumName == True:
    albumName = input("What do you want to the album name to be? ")

for filename in os.listdir(directory):

    filedir = os.path.join(directory, filename) # gets the file directory of the original song

    if setAlbumName == True:
        audiofile = eyed3.load(filedir)
        audiofile.tag.album = albumName
        audiofile.tag.album_artist = albumName
        audiofile.tag.save()


    if stripName == True:       
        
        print(filedir)
        newName = filename.replace(whatToStrip, "") # strips the unwanted string
        print(newName)
        newfiledir = os.path.join(directory, newName) # creates a new song directory for the renamed song
        os.rename(filedir, newfiledir) # renames the song to the new directy
        #print(os.path.join(directory, filename))
    
    


print('Complete!')
