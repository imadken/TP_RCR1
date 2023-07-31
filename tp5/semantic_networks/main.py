from algorithms import propagation, heritage, exceptions
import json

print("Choisissez la partie que vous voulez tester")
print("1) Partie 1")
print("2) Partie 2")
print("3) Partie 3")

choix = input()

if choix == "1":
    print("Partie 1: l'algorithm de propagation de marqueurs")
    f = open('Bases/propagation.json')

    reseau_semantique = json.load(f)

    M1_node = ["Modes de Representations des connaissances", 
            "Modes de Representations des connaissances",
            "Modes de Representations des connaissances",
            "Modes de Representations des connaissances"]
   

    M2_node = ["Axiome A7",
            "Axiome A4",
            "Axe-IA",
            "Axiome A9"]

    relation = "contient"
    solutions = propagation.propagation_de_marqueurs(reseau_semantique, 
                            M1_node, 
                            M2_node,
                            relation)

    i = 0
    for solution in solutions:
        print(" ".join([M1_node[i], relation, M2_node[i]]))
        i += 1
        print(solution)

elif choix == "2":
    print("Partie 2: l'algorithm d'heritage")

    # f = open('Bases/heritage.json')
    f = open('Bases/propagation.json')

    reseau_semantique = json.load(f)

    # name = "Titi"
    name = "Systeme D"
    print("starting node : "+name+"\n")
    print("Resultat de l'inference utiliser:")
    print(name,end="\n\n")
    nodes, properties = heritage.heritage(reseau_semantique, name)
    for l in nodes:
        print(l,end="\n\n")
    print("Deduction des priorites:")
    
    if properties==[] : print("empty")
    for p in properties:
        print(p,end="\n\n")

elif choix == "3":
    print("Partie 3: l'algorithm de propagation de marqueurs avec exception")
    f = open('Bases/exception.json')

    reseau_semantique = json.load(f)

    M1_node = ["Modes de Representations des connaissances"]

    M2_node = ["Axiome A7"]

    relation = "contient"

    solutions = exceptions.propagation_de_marqueurs(reseau_semantique, 
                            M1_node, 
                            M2_node,
                            relation)

    i = 0
    for solution in solutions:
        print(" ".join([M1_node[i], relation, M2_node[i]]))
        print(solution)

else:
    print("choix invalide")