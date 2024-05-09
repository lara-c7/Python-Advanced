n_size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n_size)]

primary_diagonal = [matrix[i][i] for i in range(n_size)]
secondary_diagonal = [matrix[i][-i - 1] for i in range(n_size)]
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
