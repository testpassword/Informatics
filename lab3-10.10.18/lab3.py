def CutStr(stroka):
    man = list()
    probel = line.find(".") + 3
    man.append(line[0:probel])
    part = line.split()
    for i in range(2, 6): man.append(part[i])
    man.append((int(part[3]) + int(part[4]) + int(part[5])) / 3)
    return man

def SortBySr(i):
    return i[5]

students = list()
file1 = open("data.txt", "r")
for line in file1: students.append(CutStr(line))
file1.close()
students.sort(key=SortBySr, reverse=True)
for i in students: print(i[0], "|", i[1], "|", i[2], i[3], i[4], "->", i[5])