import os
import sys
import json
rr=set()
r={}
def find_rare_in_rules(rules, rr):
    #find rare recursively
    #[[[[],[]],[]],[[],[]]] rules can be like this
    if len(rules) == 3:
        find_rare_in_rules(rules[1], rr)
        find_rare_in_rules(rules[2], rr)
    elif rules[1] in rr:
        rules[1] = "_RARE_"
    return rules
def q4():
    for line in open("cfg.counts", "r"):
        if "UNARYRULE" in line:
            if line.split(" ")[3] in r:
                r[line.split(" ")[3]] += int(line.split(" ")[0])
            else:
                r[line.split(" ")[3]] = int(line.split(" ")[0])
    for word,count in r.items():
        if count<5:
            rr.add(word.strip("\n"))
if __name__ == "__main__":

    if sys.argv[1] == 'q4':
        os.system("python count_cfg_freq.py "+ sys.argv[2] +"> cfg.counts")
        q4()
        with open (sys.argv[3], 'w') as op_file:
            for line in open(sys.argv[2]):
                op_file.write(json.dumps(find_rare_in_rules(json.loads(line), rr))+"\n")
        os.system("python count_cfg_freq.py "+ sys.argv[3] +"> cfg_Rare.counts")
    else:
        os.system("python3 parser.py q4 parse_train.dat parse_train.RARE.dat")
        os.system("python count_cfg_freq.py "+ sys.argv[2] +"> cfg.counts")

        os.system("python helper_5_6.py "+ sys.argv[2] + " " + sys.argv[3] + " "+sys.argv[4])
