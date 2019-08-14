import mystuff


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apples(self):
        print("I AM APPLES!")


# dict style
# mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
