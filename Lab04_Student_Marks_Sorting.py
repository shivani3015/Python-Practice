data4 = ["arun=60", "sunil=80", "ravi=75", "manoj=88", "elan=70", "hari=5"]

for i in range(len(data4)-1):
    for j in range(i+1, len(data4)):

        m1 = int(data4[i].split("=")[1])
        m2 = int(data4[j].split("=")[1])

        if m1 > m2:
            data4[i], data4[j] = data4[j], data4[i]

for d in data4:
    print(d)