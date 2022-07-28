# https://rosalind.info/problems/lcsm/
import string
import random

def read_fasta(fasta_file):
    # read fasta file
    # this function return a dictionary
    with open(fasta_file, 'r') as f:
        data = {}
        ind = ""
        adn = ""
        for line in f:
            if line[0] == ">":
                if len(adn) > 1 and len(ind) > 1:
                    data[ind] = adn
                ind = line.strip()
                adn = ""
            else:
                adn = adn + line.strip()
        else:
            data[ind] = adn
    return data

def ts(word):
    t = []  # list of position
    s = []  # list of tuple (sufix,position)
    # geanrating all possible the sufix
    for i in range(len(word)):
        s.append((word[i:], i))
    # sorting and saving position
    for pos in sorted(s):
        t.append(pos[0])
    return t

def len_of_pref(p1, p2):
    # len of the longes commen pref between p1 and p2
    l1 = len(p1)
    l2 = len(p2)
    i = 0
    j = 0
    while i < l1 and j < l2:
        if p1[i] != p2[j]:
            break

        j += 1
        i += 1
    return i

def lcp(word, tts):
    lcp_tab = []  # list lcp or htr
    lcp_tab.append(-1)
    # filling lcp table
    for i in range(1, len(tts)):
        lcp_tab.append(len_of_pref(word[tts[i]::], word[tts[i-1]::]))

    return lcp_tab

def Random_pad(used_one):
    c = ''.join(random.choice(string.printable) for i in range(1))
    while c in used_one:
        c = ''.join(random.choice(string.printable) for i in range(1))
    used_one.append(c)
    return c


# alphab = ['G','A','T','C']

# used_char = ['G','A','T','C']

# data = read_fasta('f.fasta')
# DNA = data.values()

alphab = ['A','B','C','D']

used_char = ['A','B','C','D']


DNA = ['AABC','BCDC','BCDE','CDED']

# padding all DNA strings
DNA_concat = ''
for s in DNA:
    DNA_concat = DNA_concat + s + Random_pad(used_char)

print()
print(lcp(DNA_concat,ts(DNA_concat)))

