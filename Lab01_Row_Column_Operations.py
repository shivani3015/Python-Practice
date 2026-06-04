"""
Lab 1
------
Find:
1. Row Sum
2. Row Max
3. Column Sum
4. Column Max
"""


data1 = [
    "arun-blr-10,40,3",
    "ravi-mum-40,50,60",
    "hari-chn-70,80,90",
    "john-del-10,50,40"
]

rows = []

for d in data1:
    parts = d.split("-")
    marks = list(map(int, parts[2].split(",")))
    rows.append(marks)

# Row Sum
print("Row Sum:")
for r in rows:
    print(sum(r), end=" ")
print()

# Row Max
print("Row Max:")
for r in rows:
    print(max(r), end=" ")
print()

# Column Sum
print("Column Sum:")
for i in range(len(rows[0])):
    s = 0
    for r in rows:
        s += r[i]
    print(s, end=" ")
print()

# Column Max
print("Column Max:")
for i in range(len(rows[0])):
    m = rows[0][i]
    for r in rows:
        if r[i] > m:
            m = r[i]
    print(m, end=" ")