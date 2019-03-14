import re
from os import listdir
from os.path import isfile, join
import ctypes.wintypes

# https://stackoverflow.com/questions/6227590/finding-the-users-my-documents-path
CSIDL_PERSONAL = 5  # My Documents
SHGFP_TYPE_CURRENT = 0  # Get current, not default value

buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
bookmarkFiles = [f for f in listdir(buf.value) if
                isfile(join(buf.value, f)) and re.search("bookmarks_\d+_\d+_\d+\.html", join(buf.value, f))]

if not bookmarkFiles:
    sys.exit()

with open(join(buf.value,bookmarkFiles[0]), mode="r", encoding="utf-8") as myfile:
    data = myfile.readlines()
newData = []
folders = {}
atLastFolder = True
for i, item in enumerate(data):
    # check for folder
    x = re.search("^\s*<H3.*>(.*)</H3>$", item)
    if x:
        # set current folderName
        folderName = x.string[x.regs[1][0]:x.regs[1][1]]
        atLastFolder = False
        if folderName not in folders:
            atLastFolder = True
            folders[folderName] = i
        if not atLastFolder:
            continue
    if not atLastFolder:
        for f in folders:
            if folders[f] > folders[folderName]:
                folders[f] = folders[f]+1
    if atLastFolder:
        newData.append(item)
    else:
        y = re.search("^\s*<A HREF.*>(.*)</A>$",item)
        if y is not None:
            newData.insert(folders[folderName]+2, item)
    # print(i, item)

with open(join(buf.value,"bookmarks_fixed.html"), mode="w", encoding="utf-8") as newFile:
    for i, item in enumerate(newData):
        newFile.write("%s" % item)
