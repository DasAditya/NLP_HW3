import sys
import json
import time
import os

q = {}
terminals = set()
non_terminals = {}
two_rule = {}
single_rule = {}
pi = {}
bp = {}

def do_cky(line):
    pi = {}
    bp = {}
    # Cky initialization pi(i,i,X) = q(X->xi)
    for i in range(0, len(line)):
        for X in single_rule:
            if line[i] not in terminals:
                line[i] = "_RARE_"
            if line[i] in single_rule[X]:  # unary rule
                pi[(i+1,i+1,X)] = q[(X,line[i])]
    #  print(pi)
    #  CKY algorithm
    for l in range(1, len(line)):
        for i in range(1, len(line)-l+1):
            j = i + l
            for X in two_rule:
                prob_combination = {}
                for YZ in two_rule[X]:
                    # print(YZ)
                    Y = YZ[0]
                    Z = YZ[1]
                    for s in range(i,j):
                        if ((i,s,Y) in pi and (s+1,j,Z) in pi):
                            prob_combination[(X,Y,Z,i,s,j)] = q[(X,Y,Z)]*pi[(i,s,Y)]*pi[(s+1,j,Z)]
                if prob_combination:
                    ma_c = [k for k, v in prob_combination.items() if v == max(prob_combination.values())]
                    pi[(i,j,X)] = max(prob_combination.values())
                    bp[(i,j,X)] = (list(ma_c[0])[1],list(ma_c[0])[2],list(ma_c[0])[4])  #
    temp = 0
    bpk = (1,len(line),"S")
    if (1,len(line),"S") not in pi:
        for X in non_terminals:
            if (1,len(line),X) in pi:
                if pi[(1,len(line),X)] > temp:
                    temp = pi[(1,len(line),X)]
                    bpk = (1,len(line),X)
    return do_return(bpk, [' '] + line, bp)
def do_return(bpk, line, bp):
    (i, j, X) = bpk
    if i==j:
        return [X, line[i]]
    (Y,Z,s) = bp[(i,j,X)]
    return [X, do_return((i,s,Y),line, bp), do_return((s+1,j,Z),line, bp)]
def do_5_6(development_file,op_file):
    with open (op_file, 'w') as output_file:
        for l in open(development_file):
            output_file.write(json.dumps(do_cky(l.strip().split(" ")))+"\n")
if __name__ == "__main__":
    os.system("python count_cfg_freq.py " +sys.argv[1] +" > counts_file.counts")
    for line in open("counts_file.counts","r"):
        if line:
            if "NONTERMINAL" in line:
                non_terminals[line.strip().split(" ")[2]] = int(line.strip().split(" ")[0])
            elif "UNARYRULE" in line:
                q[(line.strip().split(" ")[2], line.strip().split(" ")[3])] = float(line.strip().split(" ")[0])/non_terminals[line.strip().split(" ")[2]]
                if line.strip().split(" ")[2] not in single_rule:
                    single_rule[line.strip().split(" ")[2]] = {}
                if line.strip().split(" ")[3] not in single_rule[line.strip().split(" ")[2]]:
                    single_rule[line.strip().split(" ")[2]][line.strip().split(" ")[3]] = int(line.strip().split(" ")[0])
                terminals.add(line.strip().split(" ")[3])
            elif "BINARYRULE" in line:
                q[(line.strip().split(" ")[2], line.strip().split(" ")[3], line.strip().split(" ")[4])] = float(line.strip().split(" ")[0])/non_terminals[line.strip().split(" ")[2]]
                if line.strip().split(" ")[2] not in two_rule:
                    two_rule[line.strip().split(" ")[2]] = {}
                if (line.strip().split(" ")[3], line.strip().split(" ")[4]) not in two_rule[line.strip().split(" ")[2]]:
                    two_rule[line.strip().split(" ")[2]][(line.strip().split(" ")[3], line.strip().split(" ")[4])] = int(line.strip().split(" ")[0])
    do_5_6(sys.argv[2],sys.argv[3])
