string = list(input().strip())

new_string = []

for k in string:
    if k != "<":
        new_string.append(k)
    elif k == "<":
        new_string.pop()
print("".join(new_string))
