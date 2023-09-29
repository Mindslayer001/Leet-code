#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    if not matrix:
        print(matrix)

    rows, cols = len(matrix), len(matrix[0])
    row_flag = [False] * rows
    col_flag = [False] * cols

    # Scan the matrix to identify rows and columns to update
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_flag[i] = True
                col_flag[j] = True

    # Update the matrix based on row_flag and col_flag
    for i in range(rows):
        for j in range(cols):
            if row_flag[i] or col_flag[j]:
                matrix[i][j] = 1

                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends