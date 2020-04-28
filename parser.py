from html.parser import HTMLParser
from lxml import etree
from markdown import markdown

class HTMLFilter(HTMLParser):                       #Class to handle the converting from html to normal text output
    text = ""
    def handle_data(self, data):                    #Function to do this
        self.text += data

def pars():                                     #Funtion to parse and print the xml content

    feed = "F:\\Coding\\RSS_Feed\\rss.xml"

    content = ""

    tree = etree.parse(feed)                        #get the feed from the file
    root = tree.getroot()                           #get the root from the elementtree

    for item in root.iter('item'):                  #for every subpoint "item" do:
        title = item.find('title').text             #now get all the stuff important to the reader like title, link, releasedate, description and content
        link = item.find('link').text
        reldate = item.find('pubDate').text
        desc = item.find("description").text
        try:                                        #command in line 24 throws error, wen there is no content, handle this
            content = item.find("content:encoded", root.nsmap).text
        except AttributeError:                      #just continue when error (maybe caused by no content beeing given)
            content = ""

        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"{title} ({reldate})")
        print(link, "\n")
        print(desc)

        html = markdown(content)
        fd = HTMLFilter()                           #convert html to readable text
        fd.feed(html)
        print(fd.text)


if __name__ == "__main__":
    pars()