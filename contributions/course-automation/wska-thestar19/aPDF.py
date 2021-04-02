
class aPDF:
    name = ""
    url = ""
    hash = ""
    pull = None
    path = None
    asText = ""
    def __init__(self,name,url,hash,pull,path = None, asText = None, nameOfFile = ""):
        self.name = name
        self.url = url
        self.hash = hash
        self.pull = pull
        self.path = path
        self.asText = asText
        self.nameOfFile = nameOfFile = ""
