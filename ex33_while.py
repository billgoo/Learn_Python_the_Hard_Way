 
def count_num(num, incre, use_while=True):
    numbers = []

    if use_while:
        i = 0
        while i < num:
            print(f"At the top i is {i}")
            numbers.append(i)

            i += incre
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {i}")
    else:
        for i in range(0, num, incre):
            print(f"At the top i is {i}")
            numbers.append(i)

            # i += incre
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)



if __name__ == "__main__":
    count_num(10, 2, False)