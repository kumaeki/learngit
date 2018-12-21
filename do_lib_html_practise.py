from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.currentTag = ""
        self.previousTag = ""
        self.allEvents = list()
        self.event = dict()
        self.isMissed = False

    def handle_starttag(self, tag, attrs):
        if tag == "h3" and ("class","widget-title just-missed") in attrs:
            self.isMissed = True
        elif tag  == "h3" and ("class","event-title") in attrs:
            
            self.previousTag = "event-title"
        elif self.previousTag == "event-title" and tag == "a":
            
            self.currentTag = "event-title"
        elif tag == "time":
           
            self.currentTag = "event-date"
        elif tag == "span" and ("class","event-location") in attrs:
            
            self.currentTag = "event-location"

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.isMissed:
            pass

        elif self.currentTag == "event-title":
            
            self.event["event-title"] = data
        elif self.currentTag == "event-date":
            
            self.event["event-date"] = data
        elif self.currentTag == "event-location":
            
            self.event["event-location"] = data
            self.allEvents.append(self.event.copy())
            self.currentTag = ""
            self.previousTag = ""

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

req = request.Request('https://www.python.org/events/python-events/')
parser = MyHTMLParser()
with request.urlopen(req) as f:
    data = f.readline()
    while data:
        parser.feed(str(data,encoding="utf-8").strip())
        data = f.readline()

for event in parser.allEvents:
    print(event)