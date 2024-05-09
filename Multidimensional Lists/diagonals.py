n_lines = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n_lines)]

primary_diagonal = [matrix[i][i] for i in range(n_lines)]
secondary_diagonal = [matrix[i][- i - 1] for i in range(n_lines)]

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')
