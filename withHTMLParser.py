from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global currentUrl, urls, folders, currentPath
        print("Encountered a start tag:", tag)
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href' and attr[1] not in urls:
                    currentUrl = attr[1]
                    urls[currentUrl] = {'attrs': attrs}
        else if tag == 'h3':
            currentPath.push()


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        global currentUrl, urls
        print("Encountered some data  :", data)
        if len(currentUrl) > 0:
            urls[currentUrl]["title"] = data
            currentUrl = ""


print("Hello, ", 3)
urls = {}
folders = {}
currentUrl = ""
currentPath = []
with open("C:/Users/me/Documents/bookmarks_10_23_18.html", mode="r", encoding="utf-8") as myfile:
    data = myfile.readlines()

parser = MyHTMLParser()
for chunk in data:
    parser.feed(chunk)
