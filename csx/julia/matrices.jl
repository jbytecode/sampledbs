using LinearAlgebra


# m is a matrix with 3 rows and 3 columns
m = [1 4 6; 6 5 4; 3 -1 10]

# Dimensions of the matrix
rows, cols = size(m)
println("Rows: $rows, Columns: $cols")

# Accessing elements
println("Element at (1, 2): ", m[1, 2])  # Accessing element at row 1, column 2
println("Element at (2, 3): ", m[2, 3])  # Accessing element at row 2, column 3

# Accessing a row
println("Row 1: ", m[1, :])  # Accessing the first row

# Accessing a column
println("Column 2: ", m[:, 2])  # Accessing the second column

# Modifying an element
m[1, 2] = 10
println("Modified matrix: \n", m)

# Adding a new row
m = [m; 2 3 4]  # Adding a new row at the end
println("Matrix after adding a new row: \n", m)

# Adding a new column
m = [m [7; 8; 9; 10]]  # Adding a new column at the end
println("Matrix after adding a new column: \n", m)

# Transposing the matrix
m_transposed = m'

# Matrix of zeros 
m_zeros = zeros(3, 3)

# Matrix of ones
m_ones = ones(3, 3)

# Identity matrix
m_identity = I(3)

# Random matrix
m_random = rand(3, 3)

# Inverse of a matrix
A = [1 2; 3 4]
A_inv = inv(A)

# Determinant of a matrix
det_A = det(A)

# Eigenvalues and eigenvectors
eigen_A = eigen(A)
println("Eigenvalues: ", eigen_A.values)
println("Eigenvectors: \n", eigen_A.vectors)




