
import os
import glob
from subprocess import call
from shutil import copyfile


def find():
    for file in glob.glob("*.wem"):
        print()
        print (file)

def find_that_ends(end):
    l = ()
    for file in glob.glob("*"):
        if file[-len(end):] == end:
            l = l+( file,)
    return l

def restore_old():
    for file in glob.glob("_old/*"):
        newname = cut_after(file, "_old")[1:]
        print("    Restoring "+newname)
        f = open(newname, "wb")
        f.close()
        copyfile(file, newname)
    print("Done restoring")
        
def backup():
    directory = "_old"
    try:
        os.stat(directory)
        print("directory _old exists, continuing")
    except:
        os.mkdir(directory)     
        print("creating _old")
    for file in glob.glob("*.wem"):
        print("    Backing up "+file)
        newname = "_old/"+file
        f = open(newname, "wb")
        f.close()
        copyfile(file, newname)    
    print("Done backing up")
        
def install():
    directory = "_songs"
    files = glob.glob("_songs/*.wem")
    total = len(files)
    print("Found",total,"songs")
    print("Installing...")
    f = open("_list.txt", "r")
    t = f.read()
    dest = str.split(t)
    count = 0
    for destination in dest:
        src = files[count]
        print("    Saving "+src+" as "+destination)
        copyfile(src, destination) 
        count = count + 1
        if count==total:
            count = 0
    print("Done!")
        
def cut_after(org, s):
    i = org.index(s)
    return org[i+len(s):]

def replacelove():
    songs = glob.glob("*.wem")
    love = ""
    print("Finding song...")
    for song in songs:
        if "345422383" in song:
            love = song
            print("Found: "+love)
            break
    import random
    print ("Choosing replacement")
    replacement = random.choice(songs)
    while "345422383" in replacement:
        replacement = random.choice(songs)
    print("Replacement: "+replacement)
    copyfile(replacement, love) 
    print("Song replaced")
    
while True:
    print("\n")
    print("Welcome to the Rocket League soundtrack replacer")
    print("Made by Joao Figueira")
    print('Please place the contents of this folder on "rocketleague\TAGame\CookedPCConsole"')
    print('Place your .wem converted audio files on "rocketleague\TAGame\CookedPCConsole\_songs"')
    print('You can convert audio file to .wem with Wwise: https://www.audiokinetic.com/download/')
    print('Note that there are originally 42 songs and that if you have more songs than that they will not be used')
    print('Also note that if you have less than 42 songs, some of your songs will be repeated')
    print("Make sure to backup songs first!")
    print('To backup current songs write "b", to restore old songs write "r", to install new songs on folder write "i"')
    print('If you just hate that "I love you love you" song that allways plays at the start, write "x" to replace it with a random one')
    print('Write anything else to exit')
    if find_that_ends("Antenna_Fallout_VaultBoy_SF.upk") == ():
        print()
        print("WARNING: THIS FILE IS NOT IN THE CORRECT DIRECTORY")
        print('Please place the contents of this folder on "rocketleague\TAGame\CookedPCConsole"')
        exit()
    inp = input(">")
    while inp == "":
        inp = input(">")
    if inp == "r":
        if find_that_ends("_old") == ():
            print("No backup saved! exiting")
            exit()
        else:
            print("Restore folder found! Restoring")
            restore_old()
    elif inp == "b":
        backup()
    elif inp == "i":
        install()
    elif inp in "x":
        replacelove()
    else:
        break