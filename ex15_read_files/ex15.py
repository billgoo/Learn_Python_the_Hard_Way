from sys import argv

script, fn = argv

txt = open(fn)

print(f"Here's your file {fn}:")
print(txt.read())
txt.close()
'''
print("Type the  fn again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
'''

# python3 -m pydoc open