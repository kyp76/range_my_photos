import os
import sys

# For EXIF reading
head = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(head, 'exifread'))
import exifread


path = "/Users/svandenbulcke/Code/perso/range_my_photos/tests"


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
            dictListFiles[name] = {'extension'  : name[-3:],
                                   'path'       : pathOfFile,
                                   'size'       : convert_bytes(os.path.getsize(pathOfFile))}

    return dictListFiles




mlist_dir = listFiles(path)

listkey1 = mlist_dir.keys()
print('mlist_dir is  {}'.format(listkey1[0]))
pathImg = mlist_dir[listkey1[5]].get('path')

#
#print('keys are {}'.format(listkey1))
#print ('path of {} is {}'.format(listkey1[0],(mlist_dir[listkey1[0]].get('path'))))

print ('exif of {} is {}'.format(listkey1[5],get_exif(pathImg)))