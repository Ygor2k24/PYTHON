n1 = int(input("DIgite um numero:"))
n2 = int(input("Digite outro numero:"))
n3 = int(input("Digite mais um numero:")) 

if n1 > n2 and n1 > n3:
    print(f"O {n1} é o maior numero de todos")
elif n2 > n1 and n2 > n3:
    print(f"O {n2} é o maior numero de todos")
elif n3 > n1 and  n3 > n2:
    print(f"O {n3} é o maior numero de todos")

