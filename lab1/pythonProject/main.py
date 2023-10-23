# Exercitiul 1
def ex1():
    lista_numere = input("Scrie cateva numere: ")
    numere = lista_numere.split()
    n = len(numere)
    a = int(numere[0])

    for index in range(2, n):
        b = int(numere[index])

        # in a vom obtine cmmmdc dintre a si b
        while a != b:
            if a > b:
                a = a - b;
            else:
                b = b - a;

    print("cmmdc:", a)


# Exercitiul 2
def ex2():
    s = str(input("Scrie un sir: "))
    cont = 0
    vocals = "AEIOUaeiou"

    for index in range(0, len(s)):
        if s[index] in vocals:
            cont = cont + 1

    print(cont)


# Exercitiul 3
def ex3():
    sub = str(input("Scrie un subsir: "))
    sir = str(input("Scrie un sir: "))

    start = 0
    cont = 0
    # l1 = len(sub)
    l2 = len(sir)

    while start < l2:
        start = sir.find(sub, start)
        if start < 0:
            break
        cont += 1
        start += 1

    print("Numarul de aparitii al sirului %s in sirul %s este: %d" % (sub, sir, cont))


# Exercitul 4
def ex4():
    s = str(input("Scrie un sir: "))
    newS = ""

    for ch in s:
        if ch.isupper():
            if len(newS) == 0:
                newS += ch.lower()
            else:
                newS = newS + "_" + ch.lower()
        else:
            newS += ch
    print("Sirul modificat este: ", newS)


# Exercitiul5
def ex5():
    dim = int(input("Da dimensiunea matricii: "))

    matrice = []

    for i in range(dim):
        linie = str(input())
        matrice.append(linie)

    """for i in range(dim):
        for j in range(dim):
            print(matrice[i][j], end=" ")"""

    stanga = 0
    dreapta = 0
    sus = 0
    jos = 0

    cont = dim * dim
    while cont > 0:
        for i in range(stanga, dim - dreapta):
            print(matrice[sus][i], end="")
            cont -= 1
        sus += 1

        for i in range(sus, dim - jos):
            print(matrice[i][dim - dreapta - 1], end="")
            cont -= 1
        dreapta += 1

        for i in range(dim - dreapta - 1, stanga - 1, -1):
            print(matrice[dim - jos - 1][i], end="")
            cont -= 1
        jos += 1

        for i in range(dim - jos - 1, sus - 1, -1):
            print(matrice[i][stanga], end="")
            cont -= 1
        stanga += 1


# Exercitiul 6
def ex6():
    nr = int(input("Scrie un numar: "))
    copie = nr
    ogl = 0

    while copie:
        ogl = ogl * 10 + copie % 10
        copie //= 10

    # print(ogl)
    if ogl == nr:
        print("Numarul %d este palindrom" % nr)
    else:
        print("Numarul %d nu este palindrom" % nr)


# Exercitiul7
def ex7():
    dig = "0123456789"
    text = str(input("Scrie un text: "))
    nr = ""

    for index in range(len(text)):
        if text[index] in dig and len(nr) == 0:
            while text[index] in dig:
                nr += text[index]
                if index + 1 < len(text):
                    index += 1
                else:
                    break
            else:
                break
    print(nr)


# Exercitiul8
def ex8():
    nr = int(input("Scrie un numar: "))

    # varianta lunga
    bits1 = 0

    while nr > 0:
        if nr % 2 == 1:
            bits1 += 1
        nr //= 2
        print(nr)
    print("Numarul de biti din reprezentarea binara: ", bits1)

    # varianta scurta
    """formatB = bin(nr)
    print("Numarul de biti din reprezentarea binara: ", formatB.count("1"))"""


# Exercitiul9
def ex9():
    text = input("Scrie un text: ")
    alphabet = "ABCDEFGHIJKLMNOPQRSTOVWXYZabcdefghijklmnopqrstuvwxyz"
    char_max = ""
    max = 0

    for char in alphabet:
        if text.count(char) > max:
            max = text.count(char)
            char_max = char

    print(char_max)


# Exercitiul10
def ex10():
    text = input("Scrie un text: ")
    cont = len(text.split())
    print("Numarul de cuvinte din sirul dat este: ", cont)


def main():
    # ex1()
    # ex2()
    ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()


if __name__ == "__main__":
    main()
