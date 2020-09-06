import re
with open(input()) as f: str = f.read().replace('  ', '##').replace('"', '').split('\n')
lines = [line for line in str if line.replace(' ', '').replace('\n', '') != '']
lines.append('EOoF')
keyregex = r'(#*[a-zA-Z0-9][^:\n]*:)'
listregex = r'(- )'

for i, line in enumerate(lines):
    if re.match(keyregex, line, re.MULTILINE) != None:
        for id, item in enumerate(lines[i+1:]):
            if re.match(keyregex, line, re.MULTILINE).group(0).count('##') >= item.count('##'):
                lines.insert(id+i+1, '</' + re.match(keyregex, line, re.MULTILINE).group(0).replace('##', '').replace(':', '>').replace(' ', '_'))
                break
        #while i in [re.match(listregex, item, re.MULTILINE) for item in lines[i+1:]] != None :
            #print(re.sub(listregex, lines[id+i], item) + lines[id+i].replace('<', '</'))
        lines[i] = (re.sub(keyregex, '<' + re.match(keyregex, line, re.MULTILINE).group(0).replace('##', '').replace(':', '>').replace(' ', '_'), line, 1))
    else: lines[i] = line.replace('#', '')
for i, line in enumerate(lines):
    if re.match(listregex, line, re.MULTILINE) == None:
        for id, item in enumerate(lines[i+1:]):
            if re.match(listregex, item, re.MULTILINE) != None:
                lines[id+i+1] = re.sub(listregex, line, item) + line.replace('<', '</')
            else: break
lines.pop()
lines.append('</root>')
lines.insert(0, '<root>')
print('\n'.join(lines))
