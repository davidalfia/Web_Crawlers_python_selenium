

class Article(object):

    def __init__(self, url, text):
        self.url = url
        self.text = text

    def get_url(self):
        return self.url

    def get_text(self):
        return self.text

