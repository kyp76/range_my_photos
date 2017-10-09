import os


path = "/cygdrive/c/Users/svandenbulcke/Code/Perso/range_my_photos/tests"

def list_directory(path):
    list_dir = os.listdir(path)
    #for el in list_dir:
    #   list_directory(el)
    return list_dir



mlist_dir = list_directory(path)
print('the list directory is {}'.format(mlist_dir))