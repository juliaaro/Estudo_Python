n1 = int(input())
n3 = int(input())
n4 = int(input())
n6 = int(input())

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

print("Lista de apostas:")

for i in range(n1+1,n3,2):
    for j in range(n4+1,n6,2):
        if (((n1+i+n3+n4+j+n6) % 7) != 0) and (((n1+i+n3+n4+j+n6) % 13) != 0):
            n2 = i
            n5 = j
            print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))

