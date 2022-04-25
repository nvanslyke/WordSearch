from distutils.util import change_root
import numpy as np
import termcolor
from termcolor import colored
import csv
import random
import sys

sys.setrecursionlimit(999999)
file = open('matrix.csv')
rows = []
for row in file:
    r = row.split(",")
    if "\n" in r[len(r)-1]:
        r[len(r)-1] = r[len(r)-1][:1]
    rows.append(r)

matrix = np.array(rows)

z = 1
def findWord(): 
    word = input("What word would you like to find? ")
    if word == "change":
        n = 0
        b, c = firstmat(n, word)
        prnt(b,c)
        return
    found = False
    found, pos = findHorizontal(word)    
    if not found:
        found, pos = findVertical(word) 
    
    if not found:
        found, pos =  findDiag(word)

    if not found:
        found, pos = findDiag2(word)
    
    if not found:
        found, pos = findDiag3(word)
    
    if not found:
        found, pos = findDiag4(word)

    
    if found:
        prnt(matrix, pos)
    else:
        print("not found")

def firstmat(n, word):
    global matrix
    global z
    file = open('matrix2.csv')
    rows = []
    for row in file:
        r = row.split(",")
        if "\n" in r[len(r)-1]:
            r[len(r)-1] = r[len(r)-1][:1]
        rows.append(r)

    matrix = np.array(rows)
    file.close()
    if n == 0:
        print()
        print()
        word = input("What word would you like to find? ")
        print()
        n = input("What size should the matrix be? ")
        writeto(int(n), word)
    found = False
    while found == False:   

        found, pos = findHorizontal(word)    
        if not found:
            found, pos = findVertical(word) 
        
        if not found:
            found, pos =  findDiag(word)

        if not found:
            found, pos = findDiag2(word)
        
        if not found:
            found, pos = findDiag3(word)
        
        if not found:
            found, pos = findDiag4(word)

        if not found:
            writeto(n, word)
   
    return matrix, pos

def writeto(n, word):    
    global z
    letters = 'abcdefghijklmnopqrstuvwxyz'
    file = open('matrix2.csv', 'w')
    writer = csv.writer(file, quoting=csv.QUOTE_NONE)
    for i in range(n):
        row = []
        for r in range(n):
            row.append(random.choice(letters))
    
        writer.writerow(row)
    
    file.close()
    
    print(z, end='\r')
    z += 1  
    
    firstmat(n, word)

def findHorizontal(word): 
    row = ""
    for i, r in enumerate(matrix):
        for char in r:
            row += char
        if word in row :
            pos1 = row.find(word)
            pos = [[i,pos1]]
            for b in range(pos1 + 1, pos1 + len(word)):
                pos.append([i,b])
            return True, pos
        elif word in row[::-1]:
            pos1 = row.find(word[::-1])
            pos = [[i,pos1]]
            for b in range(pos1 + 1, pos1 + len(word)):
                pos.append([i,b])
            return True, pos
        row = ""
    list = [[0,0]]
    return False, list

def findVertical(word):       
    col = ""
    for c in range(len(matrix[0])):
        for r in matrix:
            col += r[c]
        if word in col: 
            pos1 = col.find(word)
            pos = [[pos1,c]]
            for b in range(pos1 + 1, pos1 + len(word)):
                pos.append([b,c])
            return True, pos
        elif word in col[::-1]:
            pos1 = col.find(word[::-1])
            pos = [[pos1,c]]
            for b in range(pos1 + 1, pos1 + len(word)):
                pos.append([b,c])
            return True, pos
        col = ""
    list = [[0,0]]
    return False, list


def findDiag(word):
    diag = ""
    for i in range(len(matrix[0])):
        r = 0
        c = i
        while r < len(matrix) and c < len(matrix[r]):
            diag += matrix[r][c]
            r+=1
            c+=1
        if  word in diag:
            pos1 = diag.find(word)
            pos = [[pos1, i + pos1]]
            c = i+pos1 + 1
            for b in range(pos1 + 1, pos1 + len(word)):
                tmp = [b,c]
                pos.append(tmp)
                c += 1
            return True, pos
        elif word in diag[::-1]:
            pos1 = diag.find(word[::-1])
            pos = [[pos1, i + pos1]]
            c = i+pos1+1
            for b in range(pos1+ 1, pos1 + len(word)):
                pos.append([b,c])
                c += 1
            return True, pos
        diag = ""
    list = [[0,0]]
    return False, list

def findDiag2(word):
    diag = ""
    for i in range(len(matrix)):
        r = i
        c = 0
        while r < len(matrix) and c < len(matrix[r]):
            diag += matrix[r][c]
            r+=1
            c+=1
        if  word in diag:
            pos1 = diag.find(word)
            pos = [[i + pos1, pos1]]
            r = i+pos1 + 1
            for b in range(pos1 + 1, pos1 + len(word)):
                tmp = [r,b]
                pos.append(tmp)
                r += 1
            return True, pos
        elif word in diag[::-1]:
            pos1 = diag.find(word[::-1])
            pos = [[pos1 + i, pos1]]
            r = i+pos1+1
            for b in range(pos1+ 1, pos1 + len(word)):
                pos.append([r,b])
                r += 1
            return True, pos
        diag = ""
    list = [[0,0]]
    return False, list

def findDiag3(word):
    diag = ""
    for i in range(len(matrix[0]) -1, -1, -1):
        r = 0
        c = i
        while r < len(matrix) and c >= 0:
            diag += matrix[r][c]
            r+=1
            c-=1
        if  word in diag:
            pos1 = diag.find(word)
            pos = [[pos1, i - pos1]]
            c = i-pos1 - 1
            for b in range(pos1 + 1, pos1 + len(word)):
                tmp = [b,c]
                pos.append(tmp)
                c -= 1
            return True, pos
        elif word in diag[::-1]:
            pos1 = diag.find(word[::-1])
            pos = [[pos1, i - pos1]]
            c = i-pos1 - 1
            for b in range(pos1+ 1, pos1 + len(word)):
                pos.append([b,c])
                c -= 1
            return True, pos
        diag = ""
    list = [[0,0]]
    return False, list


def findDiag4(word):
    diag = ""
    for i in range(len(matrix[0])):
        r = len(matrix) -1
        c = i
        while r >= 0 and c < len(matrix[r]):
            diag += matrix[r][c]
            r-=1
            c+=1
        if  word in diag:
            pos1 = diag.find(word)
            pos = [[len(matrix) - pos1 -1, i + pos1]]
            c = i+pos1 + 1
            for b in range(len(matrix) - pos1 - 2, len(matrix) - pos1 - 2  - len(word) + 1, -1):
                tmp = [b,c]
                pos.append(tmp)
                c += 1
            return True, pos
        elif word in diag[::-1]:
            pos1 = diag.find(word[::-1])
            pos = [[len(matrix) - pos1 -1, i + pos1]]
            c = i+pos1+1
            for b in range(len(matrix) - pos1 -2, len(matrix) - pos1 -2 - len(word)):
                pos.append([b,c])
                c += 1
            return True, pos
        diag = ""
    list = [[0,0]]
    return False, list


def prnt(matrix, pos):
    print()
    print()
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if c == len(matrix[r]) - 1:
                if [r,c] in pos:
                    termcolor.cprint(matrix[r][c], 'red')
                else:
                    print(matrix[r][c])
            else:
                if [r,c] in pos:
                    termcolor.cprint(matrix[r][c], 'red', end = "  ", flush=True)

                else:    
                    print(matrix[r][c], end = "  ", flush=True)
    print()




findWord()


