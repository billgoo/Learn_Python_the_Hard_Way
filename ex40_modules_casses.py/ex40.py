class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def delete_the_song(self):
        self.lyrics.pop(0)
        print(self.lyrics)


h_b_l = ["Happy birthday to you",
         "I don't want to get sued",
         "So I'll stop right there"]
happy_bday = Song(h_b_l)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

happy_bday.delete_the_song()

bulls_on_parade.delete_the_song()