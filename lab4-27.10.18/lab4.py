inputfile = open('timetable.yml', 'r', encoding = "utf-8")
outputfile = open('timetable.json','w', encoding = "utf-8")
newline = inputfile.readline()
data = list()
lines = 0
closethink = list()
helpstring = list()
while newline:
    data.append(newline)
    lines += 1
    newline = inputfile.readline()
inputfile.close()
start_k = len(data[0]) - len(data[0].lstrip())
outputfile.write("{\n")
for i in range(0, lines - 1):
    if data[i].lstrip()[0] == '-':
        closethink.append('    "' + data[i].lstrip().lstrip('-'))
        outputfile.write('    "' + data[i].lstrip().lstrip('-'))
    else:
        helpstring = data[i].lstrip().split(':', maxsplit = 1)
        outputfile.write('    "' + helpstring[0] + '":' + helpstring[1].lstrip() + ",")
    end_k = len(data[i + 1]) - len(data[i + 1].lstrip())
    if end_k < start_k:
        outputfile.write("  },"'\n')
    if end_k > start_k:
        outputfile.write('\n'"  {"'\n')
    start_k = end_k
outputfile.write('  }\n  }\n}')
inputfile.close()
outputfile.close()