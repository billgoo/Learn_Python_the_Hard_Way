class Other(object):

    def override(self):
        print("O o()")

    def implicit(self):
        print("O i()")

    def altered(self):
        print("O a()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("C o()")

    def altered(self):
        print("C, Before O a()")
        self.other.altered()
        print("C, After O a()")

son = Child()

son.implicit()
son.override()
son.altered()
