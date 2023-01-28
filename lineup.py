alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
name = []

for _ in range(n):
    name.append(input().strip())

name_numb = []
names_numb = []

for i in name:




# name_1st = []
# name_2nd = []

# for i in name:
#     name_1st.append(list(i)[0])
#     name_2nd.append(list(i)[1])

# increase_1st = False
# decrease_1st  = False
# neither_1st = False
# increase_2nd = False
# decrease_2nd  = False
# neither_2nd = False
# same = False

# for k in range(1, n):
#     if list(alphabet).index(name_1st[k]) < list(alphabet).index(name_1st[k-1]) and increase_1st == False:
#         decrease_1st = True
#     elif decrease_1st == False and list(alphabet).index(name_1st[k]) > list(alphabet).index(name_1st[k-1]):
#         increase_1st = True
#     elif list(alphabet).index(name_1st[k]) < list(alphabet).index(name_1st[k-1]) and increase_1st == True:
#         neither_1st = True
#         break
#     elif decrease_1st == True and list(alphabet).index(name_1st[k]) > list(alphabet).index(name_1st[k-1]):
#         neither_1st = True
#         break
#     if list(alphabet).index(name_1st[k]) == list(alphabet).index(name_1st[k-1]):
#         same = True
#         if list(alphabet).index(name_2nd[k]) < list(alphabet).index(name_2nd[k-1]) and increase_2nd == False:
#             decrease_2nd = True
#         elif decrease_2nd == False and list(alphabet).index(name_2nd[k]) > list(alphabet).index(name_2nd[k-1]):
#             increase_2nd = True
#         elif list(alphabet).index(name_2nd[k]) < list(alphabet).index(name_2nd[k-1]) and increase_2nd == True:
#             neither_2nd = True
#             break
#         elif decrease_2nd == True and list(alphabet).index(name_2nd[k]) > list(alphabet).index(name_2nd[k-1]):
#             neither_2nd = True
#             break
# if neither_1st == False and neither_2nd == False:
#     if same == False:
#         if increase_1st:
#             print("INCREASING")
#         elif decrease_1st:
#             print("DECREASING")
#     elif same:
#         if increase_1st and increase_2nd:
#             print("INCREASING")
#         elif decrease_2nd and  decrease_1st:
#             print("DECREASING")
#         else:
#             print("NEITHER")
# elif neither_2nd == True or neither_1st == True:
#     print("NEITHER")