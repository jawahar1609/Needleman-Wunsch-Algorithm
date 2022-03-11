import numpy as np
import pandas as pd

score = {'match':1, 'mismatch':-1, 'gap':-2}

def match(a, b):
    if a==b:
        return score['match']
    else:
        return score['mismatch']

def needleman_wunsch(s1,s2):
    m, n = len(s2), len(s1)
    grid = np.zeros((m+1, n+1))

    row1 = list(' '+s1)
    col1 = list(' '+s2)

    for i in range(1, m+1):
        grid[i][0] = grid[i-1][0] + score['gap']
    
    for j in range(1,n+1):
        grid[0][j] = grid[0][j-1] + score['gap']

    for i in range(1, m+1):
        for j in range(1, n+1):
            left = grid[i][j-1] + score['gap']
            top = grid[i-1][j] + score['gap']
            diag = grid[i-1][j-1] + match(s1[j-1], s2[i-1])

            grid[i][j] = max(left, top, diag)

    df = pd.DataFrame(data=grid, index=col1, columns=row1)
    print(df,'\n')

    trace1, trace2 = '', ''
    i, j = m, n

    while i>0 and j>0:
        left = grid[i][j-1] + score['gap']
        diag = grid[i-1][j-1] + match(s1[j-1], s2[i-1])

        if grid[i][j] == diag:
            trace1 += s1[j-1]
            trace2 += s2[i-1]
            i, j = i-1, j-1

        elif grid[i][j] == left:
            trace1 += s1[j-1]
            trace2 += '-'
            j -= 1
        
        else:
            trace1 += '-'
            trace2 += s2[i-1]
            i -= 1

    trace1, trace2 = trace1[::-1], trace2[::-1]
    print(trace1+"\n"+trace2)


s1 = input("Enter String 1 :")
s2 = input("Enter String 2 :")

needleman_wunsch(s1,s2)
