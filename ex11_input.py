# original
print("how old?", end=' ')
age = input()
print("how tall?", end=' ')
height = input()
print("how much weight?", end=' ')
weight = input()

print(f"so, you're {age} old, {height} tall and {weight} heavy.")

print()

# my approach
print("how old?", end=' ')
print("how tall?", end=' ')
print("how much weight?", end=' ')
line = input()
value = line.split(',')
age, height, weight = (i for i in value)

print(f"so, you're {age} old, {height} tall and {weight} heavy.")