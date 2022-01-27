class Color:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = 1

    def __init__(self, rgba_string):
        self.from_string(string)

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.alpha = 1

    def rgba():
        return (self.red, self.green, self.blue, self.alpha)

    def hex():
        return "Not implemented"

    def hex8():
        return "Not implemented"

    def from_rgba_string(string):
        return "Not implemented"

    def from_hex_string(string):
        return "Not implemented"

    def from_string(string):
        return "Not implemented"

def test(string, hexv):
    color = Color(string)
    print(color.hex, hexv)


