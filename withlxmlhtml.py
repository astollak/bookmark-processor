from lxml import html

with open("C:/Users/me/Documents/bookmarks_10_23_18.html", mode="r", encoding="utf-8") as myfile:
    data = myfile.read()

tree = html.fromstring(data)
huge = tree.xpath("//*")
big = tree.xpath("//a | //h3 ")
first = big[3].attrib['href']
print("Done")
