import os


path = "/cygdrive/c/Users/svandenbulcke/Code/Perso/range_my_photos/tests"

def listFiles(path):
    dictListFiles = {}

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            print name
            dictListFiles[name] = os.path.join(root, name)

    return dictListFiles




mlist_dir = listFiles(path)
print('the list directory is {}'.format(mlist_dir))