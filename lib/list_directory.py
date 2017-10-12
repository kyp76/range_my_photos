import os

path = "/cygdrive/c/Users/svandenbulcke/Code/Perso/range_my_photos/tests"

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def listFiles(path):
    dictListFiles = {}

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            pathOfFile = os.path.join(root, name)
            dictListFiles[name] = {'extension'  : name[-3:],
                                   'path'       : pathOfFile,
                                   'size'       : convert_bytes(os.path.getsize(pathOfFile))}

    return dictListFiles




mlist_dir = listFiles(path)

listkey1 = mlist_dir.keys()
print('keys are {}'.format(listkey1))
print ('value of runtest.txt {}'.format((mlist_dir[listkey1[1]].get('path'))))


