tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

thin_cat = '''
I'll do a list:
\t* Cat fuck
\t* fucks
\t* fuck\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(thin_cat)

# study drill
a = "* Cat food"
b = "* Fishies"
c = f"""
I'll do a list:
\t{a}
\t{b}
\t* Catnip\n\t* Grass
"""

d = "aaa"
e = "bbb\n"
f = """
I'll do a list:
\t{}
\t{}
\t* Catnip\n\t* Grass
""".format(d, e)

print(c)
print(f)