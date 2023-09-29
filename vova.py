line_=[]
slov = {}
with open('input.txt') as f:
    inp = f.read()
lines = inp.split('\n')[:-1]
for a in lines:
    line_ = a.split()
    if not(line_[0] in slov):
        slov[line_[0]] = {}
    if line_[1] in slov[line_[0]]:
        slov[line_[0]][line_[1]] = int(slov[line_[0]][line_[1]]) + int(line_[2])
    else:
        slov[line_[0]][line_[1]] = int(line_[2])
slov_ = sorted(slov.keys())
for i in slov_:
    z = sorted(slov[i].keys())
    name = i + ':'
    print(name)
    for j in z:
        c = j + ' ' + str(slov[i][j])
        print(c)


