data2 = [
    "arun-blr-10,40,30",
    "ravi-mum-40,50,60",
    "hari-chn-70,80,90",
    "john-del-10,50,40"
]

rows = []

for d in data2:
    parts = d.split("-")
    marks = list(map(int, parts[2].split(",")))
    rows.append(marks)

# 2nd Max Row-wise
print("2nd Max Row-wise:")
for r in rows:
    temp = sorted(r)
    print(temp[-2], end=" ")

print()

# 2nd Max Column-wise
print("2nd Max Column-wise:")
for i in range(len(rows[0])):
    col = []

    for r in rows:
        col.append(r[i])

    col.sort()
    print(col[-2], end=" ")