# https://rosalind.info/problems/tran/

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

mapper = {
    'transition' : ['AG','GA','CT','TC'],
    'transversion' : ['AC','CA','AT','TA','CG','GC','GT','TG']
}


data = read_fasta('f.fasta')

DNA1 = list(data.values())[0]
DNA2 = list(data.values())[1]
transition = 0
transversion = 0

for i in range(len(DNA1)):
    if DNA1[i]+DNA2[i] in mapper['transition']:
        transition +=1
    elif DNA1[i]+DNA2[i] in mapper['transversion']:
        transversion +=1
    else:
        pass

print(f'{(transition/transversion):.11f}')

