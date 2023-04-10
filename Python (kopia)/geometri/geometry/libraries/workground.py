class point:
    def __init__(self, xy, name):
        self.xy = xy
        self.name = name
    def length (self):
        return math.sqrt(self.xy[0]**2+self.xy[1]**2)


