# file: b.py  day_14 2021 Extended Polymerization   part two
#
#  Rules dictionary contains polymer rules   NN -> C
#   insert the letter C,  between a pair of NN's
#   insertions all happen simultaneously.


def get_puzzle_line(fname):
    global template_str, Rules

    my_file = open( fname, "r")
    template_str = my_file.readline().strip("\n")    # template_str 
    nxt_line  = my_file.readline().strip("\n")       # skip blank line

    record_kount = 0 
    nxt_line  = my_file.readline().strip("\n")      # first data line
    while nxt_line != "EOF":                        # watch for EOF at bottom of input file
        key = nxt_line[0:2]
        Rules[key] = nxt_line[-1]
        record_kount += 1
        nxt_line = my_file.readline().strip("\n")

    my_file.close()
    print(F" {record_kount} records read in") 

#  you  just have to keep track of  "how many" of each two-letter permutations you have ... 
#  AND you have to keep track of how many letters you have in your original template 
#  adding in every time you add one more letter

def polymerize(kk):
    global base_polymer, Kounts, Rules 
    import copy 

    def add_key(k, new_base):
        if k in new_base.keys():
            new_base[k] += 1
        else:
            new_base[k] = 1

    def count(letter):
        if letter in Kounts.keys():
            Kounts[letter] += 1
        else:
            Kounts[letter] = 1

#  when you polymerize ... you  change  BC->S    (you have to bump the S count by the number of BC pairs you have )
#  you create two new  pairs ( or add to an already existing pair)    BS  +1     CS +1  
#  I used  template_A  dictionary,  and polymerized into template_B  dictionary, 
#  then over-wrote  A with B 

    new_base = {}
    for pkey in base_polymer:
        if pkey in Rules:
            xtra_letter = Rules[pkey]
            keya = pkey[0] + xtra_letter
            keyb = xtra_letter + pkey[1]
            add_key(keya, new_base)         # add new key to new_base
            add_key(keyb, new_base)         # add new key to new_base
            count(xtra_letter)              # count the extra letter
        else:
            add_key(pkey, base_polymer[pkey])

    for pkey in base_polymer:               # if we have missed any keys, add them now
        if pkey not in new_base:
            new_base[pkey] = base_polymer[pkey]

    base_polymer = {}                       # replace base_polymer with new_base
    base_polymer = copy.deepcopy(new_base)

    some_str = F"{base_polymer}".replace("'","").replace(" ","")
    print(F"{kk:2}    {Kounts['C']:4}     {some_str}")


def populate_Kounts():
    global Kounts, template_str

    for k in range(0,len(template_str)):
        aletter = template_str[k]
        if aletter in Kounts:
            Kounts[aletter] += 1
        else:
            Kounts[aletter] = 1
    print(F"          template={template_str}   {Kounts}")

#====================================================

if __name__ == '__main__':
 
    print("==========================================================")
    print("===                    b.py                           ====")
    print("==========================================================")
    fname = "input.data"
    fname = "test.data"
    template_str = ""
    Rules = {} 

    get_puzzle_line(fname)


    work_pairs = []
    for j in range(0,len(template_str)-1):
        work_pairs.append( template_str[j]+template_str[j+1]  )   
    print(F"        work_pairs={work_pairs}")


    # create a dictionary called base_polymer that has work_pairs as keys
    base_polymer = {}
    for vpair in work_pairs:
        base_polymer[vpair] = 1 
    print(F"      base_polymer={base_polymer}")

    # create a dictionary of letter counts 
    Kounts = {}    
    populate_Kounts()

    k = 0
    print(" n    C:nn    base_polymer")
    some_str = F"{base_polymer}".replace("'","").replace(" ","")
    print(F"{k:2}    {Kounts['C']:4}     {some_str}")

    for k in range(1,11):
        polymerize(k)


