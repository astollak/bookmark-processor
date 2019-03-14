from lxml import etree
from io import StringIO


def parsetree(el):
    global level
    if len(el) > 0:
        level = level + 1
        print('  ' * level, "Recursing from ", el.tag, el.text)
        for i in range(len(el)):
            parsetree(el[i])
        print('  ' * level, "done with ", el.tag, el.text)
        level = level - 1
    else:
        print('  ' * level, "Tag: ", el.tag, ", ", el.text)
        if el.tag == 'h3':
            path.append(el.text)


with open("C:/Users/me/Documents/bookmarks_10_23_18.html", mode="r", encoding="utf-8") as myfile:
    data = myfile.read()

level = 1
path = []
parser = etree.HTMLParser()
tree = etree.parse(StringIO(data), parser)
top = tree.getroot()
parsetree(top)
print("Done")
