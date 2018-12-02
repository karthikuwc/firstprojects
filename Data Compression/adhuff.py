from trees import *

def calcweights(xt):
    weights = []
    for i in range(len(xt)):
        if len(xt[i][1]) == 0:
            weights.append(1)
        else:
            weights.append(weights[xt[i][1][0]] + weights[xt[i][1][1]])
    return weights


def codeword(xt, c):
    i = 0
    while int(xt[i][2]) != c:
        i += 1
    b = []
    
    while i != len(xt) - 1:
        if xt[i][0] == xt[i+1][0]:
            b.insert(0,0)
        else:
            b.insert(0,1)
        i = xt[i][0]
    return b

def charfind(xt,y):
    i = -1
    for k in range(len(y)):
        if len(xt[i][1]) == 0:
            return (int(xt[i][2]),k)
        elif k == 0:
            i = xt[i][1][0]
        elif k == 1:
            i = xt[i][1][1]

def update(xt,c, weights,let):
    
    i = let[int(c)]

    return balance(i, 1, xt, weights,let)

def balance(i, count, xt, weights,let):
    #If node is orphan return tree
    if xt[i][0] == -1:
        j = i
        if len(xt[j][1]) != 0:
            weights[j] = count + weights[xt[j][1][0]] + weights[xt[j][1][1]]
        else:
            weights[j] += count
        result = [xt,weights,let]
        return result
    j = i
    
    #Check highest order in weight class
    while j < (len(weights)-1):
        if weights[j] == weights[j+1]:
            j += 1
        else:
            break
    
    #Conduct swap if needed
    if j != i:
        #Swap children
        children = xt[i][1]
        xt[i][1] = xt[j][1]
        xt[j][1] = children

        #Swap labels
        label = xt[i][2]
        xt[i][2] = xt[j][2]
        xt[j][2] = label

        if int(xt[j][2]) < 128: let[int(xt[j][2])] = j;
        if int(xt[i][2]) < 128: let[int(xt[i][2])] = i;

        #Correct children's parents
        for k in children:
            xt[k][0] = j
        for l in xt[i][1]:
            xt[l][0] = i
            
    #Update node weight
    if len(xt[j][1]) != 0:
        weights[j] = count + weights[xt[j][1][0]] + weights[xt[j][1][1]]
    else:
        weights[j] += count
    #call balance on parent node with count = 0
    return balance(xt[j][0], 0, xt, weights, let)
