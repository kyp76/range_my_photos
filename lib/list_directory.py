import os
import sys
import re

# For EXIF reading
head = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(head, 'exifread'))
import exifread


#path = "/Users/svandenbulcke/Code/perso/range_my_photos/tests"
path = '/Users/svandenbulcke/Photo_need_to_rank'


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
    dictListFiles = {}

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


def extractTime(TimeOriginal):
    TimeOriginalreformat = re.match('([0-9]{4}):([0-9]{2}):([0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})', TimeOriginal)
    return TimeOriginalreformat.groups()



mlist_dir = listFiles(path)

listkey1 = mlist_dir.keys()
print ('list of files present in my dico {}'.format(listkey1))


#pathImg = mlist_dir[listkey1[5]].get('path')

#TimeOriginal = get_exif(pathImg)['EXIF DateTimeOriginal']


##TimeOriginalreformat = re.match('([0-9]{4}):([0-9]{2}):([0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})',str(TimeOriginal))

###yearOfPhoto, monthOfPhoto, dayOfPhoto, hourOfPhoto = extractTime(str(TimeOriginal))


print('full informations of dico are {}'.format(mlist_dir))
#print ('path of {} is {}'.format(listkey1[0],(mlist_dir[listkey1[0]].get('path'))))

#print ('exif of {} is {}'.format(listkey1[5],dictExifValue))


#TODO : methode to share information of dico folder , ext or folder , time .....

#TODO : creation of directory depending of TimeOriginal

#TODO argpass

