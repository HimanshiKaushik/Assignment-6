def pascal_triangle(n):
    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            row.append(row[j - 1] * (i - j + 1) // j)
        print(row)

n = int(input("enter the number of rows: "))
print(pascal_triangle(n))