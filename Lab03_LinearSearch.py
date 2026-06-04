data3 = [
    "arun-blr-10,40,30",
    "ravi-mum-40,50,60",
    "hari-chn-70,80,90",
    "john-del-10,50,40"
]

name = input("Enter the student name: ")

found = False

for d in data3:
    parts = d.split("-")

    if parts[0] == name:
        found = True

        city = parts[1]
        marks = list(map(int, parts[2].split(",")))
        total = sum(marks)

        print("Result = FOUND")
        print("City   =", city)
        print("Total  =", total)
        break

if not found:
    print("Result = NOT FOUND")