liczby = [5, 2, 1, 4, 3]

print("Przed: ", liczby)

for i in range(len(liczby)): #indeksy
    index_minimum = i
    print('i', i, 'liczby:', liczby[i:])
    for j in range(i+1, len(liczby)):
        if liczby[j] < liczby[index_minimum]:
            index_minimum = j
    liczby[i], liczby[index_minimum] = liczby[index_minimum], liczby[i] # zamienia miejscami
    print('i: ', i, 'liczby: ', liczby)
# liczby[0], liczby[4] = liczby[4], liczby[0]

print("Po: ", liczby)
