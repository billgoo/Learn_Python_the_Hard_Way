from sys import argv
from os.path import exists
"""
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we coule do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
"""

"""
What you should SEE.

$ # first make a sample file
$ echo "This is a test file." > test.txt
$ # then look at it
$ cat test.txt
This is a test file.
$ # now run our script on it
$ python3.6 ex17.py test.txt new_file.txt
Copying from test.txt to new_file.txt
The input file is 21 bytes long
Does the output file exist? False
Ready, hit RETURN to continue, CTRL-C to abort.
Alright, all done.

"""
# a short alternative answer
open(argv[2], 'w').write(open(argv[1]).read())