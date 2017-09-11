class record:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __str__(self):
        return "{} {}".format(self.index, self.value)

    def __repr__(self):
        return "{} {}".format(self.index, self.value)
