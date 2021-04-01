
class aPDF:
    name = ""
    url = ""
    hash = ""
    pull = None
    def __init__(self,name,url,hash,pull):
        self.name = name
        self.url = url
        self.hash = hash
        self.pull = pull
