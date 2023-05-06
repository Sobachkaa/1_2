
M = {1,3,7,10,15,24,36,58,62,100}

# отношение R
R = [(x,y) for x in M for y in M if x <= y]
print("Отношение R:", R)

# матрица отношения R
R_matrix = [[1 if (i,j) in R else 0 for j in M] for i in M]
print("Матрица отношения R:")
for row in R_matrix:
    print(row)

# матрица противоположного отношения
not_R = [(x,y) for x in M for y in M if x > y]
not_R_matrix = [[1 if (i,j) in not_R else 0 for j in M] for i in M]
print("Матрица противоположного отношения:")
for row in not_R_matrix:
    print(row)

# матрица обратного отношения
R_inv = [(y,x) for (x,y) in R]
R_inv_matrix = [[1 if (i,j) in R_inv else 0 for j in M] for i in M]
print("Матрица обратного отношения:")
for row in R_inv_matrix:
    print(row)

# матрица составного отношения
R_comp = [(x,z) for (x,y1) in R for (y2,z) in R if y1 == y2]
R_comp_matrix = [[1 if (i,j) in R_comp else 0 for j in M] for i in M]
print("Матрица составного отношения:")
for row in R_comp_matrix:
    print(row)

# матрица транзитивного замыкания
R_trans = R.copy()
for (x,y1) in R:
    for (y2,z) in R:
        if y1 == y2:
            R_trans.append((x,z))
R_trans_matrix = [[1 if (i,j) in R_trans else 0 for j in M] for i in M]
print("Матрица транзитивного замыкания:")
for row in R_trans_matrix:
    print(row)

# матрица рефлексивного замыкания
R_refl = R.copy()
for x in M:
    R_refl.append((x,x))
R_refl_matrix = [[1 if (i,j) in R_refl else 0 for j in M] for i in M]
print("Матрица рефлексивного замыкания:")
for row in R_refl_matrix:
    print(row)