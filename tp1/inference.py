import os
import shutil
import sys

if len(sys.argv) < 2:
    print("Veuillez entrer le nom du fichier cnf en arguments.")
    quit()

if not os.path.exists(sys.argv[1]):
    print("Fichier cnf n'existe pas dant le chemain entré.")
    quit()

ubcnf = sys.argv[1]
newfile = ubcnf
base = os.path.splitext(ubcnf)[0]
os.rename(newfile, base + '.txt')
shutil.copy(base+'.txt', 'copy.txt')
os.rename(base+'.txt', base + '.cnf')
file = open('copy.txt', "r")
line = file.readline().split()

# extracter les information du fichier cnf
nbr_litteraux = int(line[2])
print("Le nombre des litteraux utilisé est: "+str(nbr_litteraux))
print("Le nombre de clauses originaux: "+line[3])
line[3] = str(int(line[3])+1)
print("Le nombre de clauses apres le traitement: "+line[3])
s = " "
newline = s.join(line)
newline = newline+'\n'
file.close()
but = 0


litteraux = {'Na': 1, 'Nb': 2, 'Nc': 3, 'Cea': 4, 'Ceb': 5, 'Cec': 6, 'Ma': 7, 'Mb': 8, 'Mc': 9, 'Coa': 10, 'Cob': 11, 'Coc': 12}
print("Les litteraux sont:", litteraux)
print("\n")

while True:
        litteral = input("Donner le nom de litteral que vous voulez tester: ")
        
        if litteral in litteraux.keys():
             print("litteral de test valide")
             but = litteraux[litteral]
             break
        print("Litteral n'existe pas")

non_but = -1 * but
with open('copy.txt') as f:
    lines = f.readlines()

lines[0] = newline
f1 = open('copy.txt', "w")
f1.writelines(lines)
f1.close()

# ajouter le non de litteral a la fin
f2 = open('copy.txt', "a")
f2.write('\n'+str(non_but)+' 0')
f2.close()

os.rename('copy.txt', 'copy.cnf')
os.system('ubcsat -alg saps -i copy.cnf -solve > tmp.txt')
check = "# No Solution found for"
infere = False
f3 = open('tmp.txt', "r")
for i in f3:
    if check in i:
        infere = True

if (infere == True):
    print("BC infère '" + litteral + "'")
else:
    print("BC n'infère pas '" + litteral + "'")
f3.close()
if os.path.isfile('copy_done.cnf'):
    os.remove('copy_done.cnf')
os.rename('copy.cnf', 'copy_done.cnf')
    


