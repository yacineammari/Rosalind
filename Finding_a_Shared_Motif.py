# https://rosalind.info/problems/lcsm/

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

def get_substring(s):
    length = len(s)
    l = [s[i:j+1] for i in range(length) for j in range(i,length)]
    l = sorted(l, key=lambda substring: -len(substring))
    return l

data = read_fasta('f.fasta')
DNA = list(data.values())

l = get_substring(DNA[0])



list_of_subs = []
for sub in l:
    b = False
    for s in DNA:
        if sub not in s:
            b = True
            break
    
    if not b:
        list_of_subs.append(sub)

list_of_subs = sorted(list_of_subs, key=lambda substring: -len(substring))

print(list_of_subs[0])