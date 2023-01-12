import copy

rows = []
for _ in range(4):
    rows.append(list(map(int, input().split())))

columns = []
column = []

for i in range(4):
    column.append(rows[0][i])
    column.append(rows[1][i])
    column.append(rows[2][i])
    column.append(rows[3][i])
    columns.append(copy.deepcopy(column))
    column= []

move = int(input())


def operation(rows):
    rows_new = []
    for i in rows:
        row_new = []
        for x in i:
            if x != 0:
                row_new.append(x)  
        if len(row_new) < 4:
            for _ in range(4-len(row_new)):
                row_new.append(0)
        row_new1 = [row_new[0]]
        log = row_new[0]
        for k in row_new[1:]:
            if k == log:
                row_new1.pop()
                row_new1.append(2*k)
                log = 1
            elif k != log:
                row_new1.append(k)
                log = k
        # row_new1.append(log)
        if len(row_new1) < 4:
            for _ in range(4-len(row_new1)):
                row_new1.append(0)    
        rows_new.append(row_new1)
    return rows_new


if move == 0:
    rows_new = operation(rows)
    for m in rows_new:
        print(" ".join([str(x) for x in m]))
elif move == 1:
    columns_new = operation(columns)
    rows_new = []
    row = []
    for x in range(len(columns_new)):
        row.append(columns_new[0][x])
        row.append(columns_new[1][x])
        row.append(columns_new[2][x])
        row.append(columns_new[3][x])
        rows_new.append(copy.deepcopy(row))
        row = []
    for i in rows_new:
        print(' '.join([str(k) for k in i]))

elif move == 2:
    rows_reverse = []
    for x in rows:
        x.reverse()
        rows_reverse.append(x)
    rows_new = operation(rows_reverse)
    rows_new_reverse = []
    for x in rows_new:
        x.reverse()
        rows_new_reverse.append(x)
    for m in rows_new_reverse:
        print(" ".join([str(x) for x in m]))
elif move == 3:
    columns_reverse = []
    for k in columns:
        k.reverse()
        columns_reverse.append(k)
    columns_new = operation(columns_reverse)
    columns_new_reverse = []
    for k in columns_new:
        k.reverse()
        columns_new_reverse.append(k)
    rows_new = []
    row = []
    for x in range(len(columns_new_reverse)):
        row.append(columns_new_reverse[0][x])
        row.append(columns_new_reverse[1][x])
        row.append(columns_new_reverse[2][x])
        row.append(columns_new_reverse[3][x])
        rows_new.append(copy.deepcopy(row))
        row = []
    for i in rows_new:
        print(' '.join([str(k) for k in i]))