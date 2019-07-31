import sys
# script, input_encoding, error = sys.argv
script, input_encoding, error = "ex23.py", "utf-8", "strict"

def main(language_file, encoding, errors):
    line = language_file.readline() # 每步文本里的探针停留在下一行
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)    # 递归读取下一行

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("./ex23/languages.txt", encoding="utf-8")

main(languages, input_encoding, error)