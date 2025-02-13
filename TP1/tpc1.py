import sys

total = 0
temp = 0
switch = True

for line in sys.stdin:
    i = 0
    while i < len(line):

        if line[i] in "0123456789":
            while i < len(line) and line[i] in "0123456789":
                temp = temp * 10 + int(line[i])
                i += 1
            if switch:
                total += temp
            temp = 0
        elif len(line) >= i+2 and line[i] in "Oo" and line[i+1] in "Ff" and line[i+2] in "fF":
                switch = False
                i += 3
        elif line[i] in "Oo" and line[i+1] in "Nn":
                switch = True
                i += 2
        elif line[i] in "=":
            i += 1
            print(total)
        else:
            i += 1
print(total)


                