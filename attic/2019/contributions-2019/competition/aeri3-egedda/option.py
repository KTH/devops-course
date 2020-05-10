import random

class Option:
    def __init__(self, names, optionFormat, paramFormat=None, params=None):
        self.names = names
        self.optionFormat = optionFormat
        self.paramFormat = paramFormat
        self.params = params
    
    def randomizeAndFormat(self):
        name, param = self.randomize()
        return self.format(name, param)

    def randomize(self):
        return (random.choice(self.names), random.choice(self.params)) if self.params else (random.choice(self.names), None)
    
    def format(self, name, param=None):
        return self.paramFormat.format(name, param) if param else self.optionFormat.format(name)
