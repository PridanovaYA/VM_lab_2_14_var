import numpy as np


"""пункт 1"""
print("Создать квадратную матрицу из случайных вещественных чисел из  интервала (-1,1) размера 10.\n"
      "Найти скалярное произведение 2 строки  на 7 столбец. Использовать срезы матриц.")

A = np.random.randint(-1,1,(10,10))
cln7 = A[:,6]
str2 = A[1]
r = sum(r * c for r, c in zip(str2, cln7))
print(r)
print("_______________________________________________________________________________________________")

"""пункт 2"""
print("Создать две матрицы из случайных целых чисел из [3,10] подходящего\n"
      "размера. Найти их произведение тремя способами: 1) скалярный \n"
      "алгоритм умножения матриц 2) векторный алгоритм, 3) проверив с \n"
      "помощью функции np.dot.")

A = np.random.randint(3,10,(2,10))
B = np.random.randint(3,10,(10,3))
C = np.zeros((2,3), dtype = int)

print("Скалярное произведение ☺:\n")
for i in range(2):
    for j in range(3):
        for p in range(10):
            C[i,j]  =C[i,j]+ A[i,p]*B[p,j]
print(C)

print("Векторное произведение ☺:\n")
for i in range(2):
    for j in range(3):
            C[i,j] = np.dot(A[i,:], B[:,j])
print(C)

print("Проверка ☺:\n")
C = np.dot(A,B)
print(C)

print("_______________________________________________________________________________________________")

"""пункт 3"""
print("Создать произвольную нижняя унитреугольную матрицу А 7 порядка,\n"
      "вектор B произвольный. Решить систему AX = B")

A = [[1,0,0,0,0,0,0],
     [2,1,0,0,0,0,0],
     [3,1,1,0,0,0,0],
     [1,0,2,1,0,0,0],
     [0,2,0,4,1,0,0],
     [1,0,3,0,6,1,0],
     [0,4,0,5,0,6,1]]

В = [[0],[1],[2],[1],[0],[0],[1]]
X = np.zeros((7,1), int)
for i in range(7,1):
    X[i] = B[i] - np.dot(A[i, :i], X[ :i])
print(X)


print("_______________________________________________________________________________________________")

print("Решить систему, используя LU разложение ")

a = np.array([[3.8,14.2,6.3,-15.5],
             [8.3,-6.6,5.8,12.2],
             [6.4,-8.5,-4.3,8.8],
             [17.1,-8.3,14.4,-7.2]])

b = np.array([[2.8],[-4.7],[7.7],[13.5]])

def decompose_to_LU(a):
    lu_matrix = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]

    for k in range(n):
        for j in range(k, n):
            lu_matrix[k, j] = a[k, j] - lu_matrix[k, :k] * lu_matrix[:k, j]
        print(lu_matrix)
        for i in range(k + 1, n):
            lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]
        print(lu_matrix)
    return lu_matrix

lu_matrix = decompose_to_LU(a)

def solve_LU(lu_matrix, b):
    y = np.matrix(np.zeros([lu_matrix.shape[0], 1]))

    for i in range(y.shape[0]):
        y[i, 0] = b[i, 0] - lu_matrix[i, :i] * y[:i]

    x = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
    for i in range(1, x.shape[0] + 1):
        x[-i, 0] = (y[-i] - lu_matrix[-i, -i:] * x[-i:, 0] )/ lu_matrix[-i, -i]

    return x

res = solve_LU(lu_matrix, b)
print(res)


