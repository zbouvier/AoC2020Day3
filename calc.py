lines = []
f = open('input.txt', 'r+')
for line in f.readlines():
    lines.append(line.rstrip())
f.close()


startX = 0
startY = 0
treeCount = 0
lineLength = len(lines[0])
#print(lineLength)


def treeFinder(xSlope, ySlope):
    treeCount = 0
    startX = 0
    startY = 0
    while 1==1:
        if(startY < len(lines)):
            if(lines[startY][startX%lineLength] == "#"):
                treeCount+=1
            startX+=xSlope
            startY+=ySlope
        else:
            return treeCount

print(treeFinder(1, 1) * treeFinder(3, 1) * treeFinder(5,1) * treeFinder(1, 2) * treeFinder(7, 1))
