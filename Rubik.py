from sympy.combinatorics.permutations import *
from sys import argv

moves = {"U":Permutation(1,2,3,4)(5,6,7,8)(9,10,11,12)(13,14,15,16)(17,18,19,20)**3,
         "U'":Permutation(1,2,3,4)(5,6,7,8)(9,10,11,12)(13,14,15,16)(17,18,19,20),
         "D":Permutation(21,22,23,24)(25,26,27,28)(29,30,31,32)(33,34,35,36)(37,38,39,40),
         "R":Permutation(2,7,27,22)(6,11,23,30)(10,3,31,26)(14,47,34,42)(18,43,38,46),
         "L":Permutation(1,12,28,29)(5,4,24,25)(9,8,32,21)(16,44,36,45)(20,48,40,41)**3,
         "F":Permutation(1,6,26,21)(5,10,22,29)(9,2,30,25)(13,46,33,41)(17,42,37,45),
         "B":Permutation(4,32,27,11)(8,28,23,3)(12,24,31,7)(15,48,35,43)(19,44,39,47)
        }
moves["D'"] = moves["D"]**3
moves["R'"] = moves["R"]**3
moves["L'"] = moves["L"]**3
moves["F'"] = moves["F"]**3
moves["B'"] = moves["B"]**3

moves["U2"] = moves["U"]**2
moves["B2"] = moves["B"]**2
moves["L2"] = moves["L"]**2
moves["R2"] = moves["R"]**2
moves["D2"] = moves["D"]**2
moves["F2"] = moves["F"]**2

notation = { 1:"f",	9:"u",		 2:"r",		4:"l",		29:"d",		3:"b",
        6:"f",		10:"u",		7:"r",		5:"l",		30:"d",		8:"b",
        21:"f",		11:"u",		22:"r",		24:"l",		31:"d",		23:"b",
        26:"f",		12:"u",		27:"r",		25:"l",		32:"d",		28:"b",
        13:"f",		17:"u",		14:"r",		16:"l",		37:"d",		15:"b",
        33:"f",		18:"u",		47:"r",		45:"l",		38:"d",		43:"b",
        41:"f",		19:"u",		34:"r",		44:"l",		39:"d",		48:"b",
        46:"f",		20:"u",		42:"r",		36:"l",		40:"d",		35:"b"}
	
pieces=[(1,5,9),(2,6,10),(3,7,11),(4,8,12),(13,17),(14,18),(15,19),(16,20),
        (21,25,29),(22,26,30),(23,27,31),(24,28,32),(33,37),(34,38),(35,39),(36,40)
        ,(41,45),(42,46),(43,47),(44,48)]

move = Permutation(49)

def order(algo):
    algo = algo.split(" ")
    temp = Permutation(49)
    for j in algo:
        temp = temp * moves[j]
    return temp.order()

def commute(x,y,n=1):
    x = x.split(' ')
    y = y.split(' ')
    temp = ["F","B","U","D","R","L"]
    x_ = []; y_ = []
    for j in x:
        if j in temp:
            x_.append(j+"'")
        else:
            x_.append(j[0])
    for j in y:
        if j in temp:
            y_.append(j+"'")
        else:
            y_.append(j[0])
    x_.reverse();y_.reverse()
    ans = ' '.join(x + y + x_ + y_)
    return eval_algo(ans,n)

def ev(piece):
    t =  tuple(move(i) for i in piece)
    return(t)

def track(piece):
    l = [piece]
    while ev(l[-1]) not in l:
        l.append(ev(l[-1]))
    q = []
    for i in l:
        for j in i:
            q.append(j)
    return (l,q)

def string(s):
    j = ''.join([notation[k] for k in s])
    return(j)

def eval_algo(algo,n=1):
    algo = algo.split(' ')
    global move
    move = Permutation(49)
    for j in algo:
        move = move * moves[j]
    move = move**n
    x = set(range(1,49))
    ans = []
    a_list = []
    for j in pieces:
        if j[0] in x:
            l,q = track(j)
            if len(l)!=1:
                ans.append(l)
            for i in set(q):
                x.remove(i)
    for j in ans:
        cyc=[]
        for i in j:
             cyc.append(string(i))
        a_list.append('('+','.join(cyc)+')')
    move = Permutation(49)
    return (' '.join(a_list))
     
if __name__=="__main__":
    n = int(argv[1])
    algo = argv[2:]
    algo = ' '.join(algo)
    print(eval_algo(algo,n))
