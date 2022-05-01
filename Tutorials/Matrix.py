print ('Welome to 3*3 matix adder')
Matrix=[[0,0,0],[0,0,0],[0,0,0]]
i=0
j=0
print ('MatrixA')
for Row in Matrix:
    for Column in Row:
        Value=input('>')
        Matrix[i][j]=int(Value)
        j+=1
        if j==3:
            j=0
    i+=1
    if i==3:
        i=0
print ('MatrixB')
Matrix1=[[0,0,0],[0,0,0],[0,0,0]]
i=0
j=0
for Row in Matrix1:
    for Column in Row:
        Value=input('>')
        Matrix1[i][j]=int(Value)
        j+=1
        if j==3:
            j=0
    i+=1
    if i==3:
        i=0

Add_matrix=[[0,0,0],[0,0,0],[0,0,0]]
def Matrix_adder():
    i=0
    j=0
    for Row in Matrix:
        for Column in Row:
            Add_matrix[i][j]=Matrix[i][j]+Matrix1[i][j]
            j+=1
            if j==3:
                j=0
        i+=1
        if i==3:
            i=0
    print('The Result is',Add_matrix)     
Matrix_adder()
            
        