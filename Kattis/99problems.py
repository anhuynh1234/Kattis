import copy

numb = (input())
 
if len((numb)) <= 2:
    print(str(99))
else:
    list_numb = list(numb)
    list_numb.pop()
    list_numb.pop()
    list_numb.append('9')
    list_numb.append('9')
    big_numb = int("".join(list_numb))
    small_numb = copy.deepcopy(big_numb) - 100
    if big_numb - int(numb) > abs(small_numb - int(numb)):
        print(str(small_numb))
    elif abs(small_numb - int(numb)) > big_numb - int(numb):
        print(str(big_numb))
    else:
        print(str(big_numb))
    pass