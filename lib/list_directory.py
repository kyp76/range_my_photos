import os
import sys
import re
import collections
import shutil

# For EXIF reading
head = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(head, 'exifread'))
import exifread


#originalPath = "/Users/svandenbulcke/Code/perso/range_my_photos/tests"
#desitnationPath = originalPath

originalPath = "/Users/svandenbulcke/Photo_need_to_rank"
#desitnationPath = "/Users/svandenbulcke/Dropbox/PHOTO"

def get_exif(image_filename, verbosity=None):
    """Read the EXIF metadata of the specified image.

        :param str image_filename: The filename of the image.
        :param verbosity: None or a list of strings, permits to activate additional debug on particular sections.
               Supported items: ['MakerNote']
        :returns: dict -- A dictionnary containing the EXIFs.
    """
    with open(image_filename, 'rb') as f:
        return exifread.process_file(f, verbosity=verbosity)


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def listFiles(path):
    dictListFiles = collections.OrderedDict()

    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            pathOfFile = os.path.join(root, name)
            try:
                TimeOriginal = get_exif(pathOfFile)['EXIF DateTimeOriginal']
            except KeyError:
                TimeOriginal = 'Null'
                pass
            dictListFiles[name] = {'extension'  : name[-3:],
                                   'path'       : pathOfFile,
                                   'size'       : convert_bytes(os.path.getsize(pathOfFile)),
                                   'TimeOfPhoto': TimeOriginal
                                   }

    return dictListFiles


def extractTime(timeOriginal):
    if timeOriginal == 'Null':
        return

    timeOriginalreformat = re.match('([0-9]{4}):([0-9]{2}):([0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})', timeOriginal)
    return timeOriginalreformat.groups()


def printValueDictionnary(dictionnary,needValues):
    for key in dictionnary.keys():
        value = dictionnary.get(key).get(str(needValues))
        print (key , value)




def createdirectory(dictionnary):
    for key in dictionnary.iterkeys():
        value = extractTime(str(dictionnary.get(key).get("TimeOfPhoto")))
        imagePath = dictionnary.get(key).get("path")
        if value is not None:
            createdPath = os.path.join(os.sep,desitnationPath,value[0],"_".join(value)[0:13])
            if not os.path.exists(createdPath):
                os.makedirs(createdPath)
            try:
                shutil.copy(imagePath,createdPath)
            except:
                print ("Error during copy file")
                pass




mdictValuable = listFiles(originalPath)

keyofDict = mdictValuable.keys()
print ('list of files present in my dico {}'.format(keyofDict))
#valueOfDict = mdictValuable.values()
#print ('list of value present in my dico {}'.format(valueOfDict))

#createdirectory(mdictValuable)
printValueDictionnary(mdictValuable,"TimeOfPhoto")

#TODO test inn real life

#TODO argpass

#TODO unit test

#TODO update documentation and refactor



