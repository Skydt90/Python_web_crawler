from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
        self.is_inside_article = False
        self.data = []
        self.tags = []

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for (attribute, value) in attrs:
                if attribute == "href":
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        
        if self.is_inside_article:
            if tag != "ul":
                self.tags.append(tag)

        if tag != "article":
            return    
        else:
            self.is_inside_article = True
                
    def handle_endtag(self, tag):
        if tag == "article" and self.is_inside_article:
            self.is_inside_article = False

    def handle_data(self, data):
        if self.is_inside_article:
            self.data.append(" ".join(data.split()))

    def page_links(self):
        return self.links

    def page_data(self):
        self.data = list(filter(lambda name: name.strip(), self.data))
        return self.data

    def page_tags(self):
        return self.tags