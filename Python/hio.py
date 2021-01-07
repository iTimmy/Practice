def create(parameter):
    #creu rhes hefo digon o rhifau
    row = []
    for i in range (0,parameter):
        num = input("rhif yn rhes: ")
        if num == "":
            num = 0
        num = int(num)
        row.append(num)
    return row

def determinant(m):
    det = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
    return det

def minor(m):
    #creu'r matrics meinor. Maer pethau yn yr array yn columau, nid rhesi
    row = 0
    column = 0
    minors = []
    col = []
    for i in range(0,3):
        for i in range(0,3):
            
            R1 = []
            R2 = []
            mat = [] 
            if row == 0:
                if column == 0:
                    R1.append(m[1][1])
                    R1.append(m[1][2])
                    R2.append(m[2][1])
                    R2.append(m[2][2])
                elif column == 1:
                    R1.append(m[1][0])
                    R1.append(m[1][2])
                    R2.append(m[2][0])
                    R2.append(m[2][2])
                else:
                    R1.append(m[1][0])
                    R1.append(m[1][1])
                    R2.append(m[2][0])
                    R2.append(m[2][1])
            elif row == 1:
                if column == 0:
                    R1.append(m[0][1])
                    R1.append(m[0][2])
                    R2.append(m[2][1])
                    R2.append(m[2][2])
                elif column == 1:
                    R1.append(m[0][0])
                    R1.append(m[0][2])
                    R2.append(m[2][0])
                    R2.append(m[2][2])
                else:
                    R1.append(m[0][0])
                    R1.append(m[0][1])
                    R2.append(m[2][0])
                    R2.append(m[2][1])
            else:
                if column == 0:
                    R1.append(m[0][1])
                    R1.append(m[0][2])
                    R2.append(m[1][1])
                    R2.append(m[1][2])
                elif column == 1:
                    R1.append(m[0][0])
                    R1.append(m[0][2])
                    R2.append(m[1][0])
                    R2.append(m[1][2])
                else:
                    R1.append(m[0][0])
                    R1.append(m[0][1])
                    R2.append(m[1][0])
                    R2.append(m[1][1])
            mat.append(R1)
            mat.append(R2)
            row += 1
            col.append(mincalc(mat))
            
        column += 1
        row = 0
        minors.append(col)
        mat = []
        col = []
    return minors
def mincalc(m):
    #i gwneud y rhifau am y marics meinor 
    ans = m[0][0]*m[1][1]-m[1][0]*m[0][1]
    return ans

def adj(mat):
    mat[0][1] = -(mat[0][1])
    mat[1][0] = -(mat[1][0])
    mat[1][2] = -(mat[1][2])
    mat[2][1] = -(mat[2][1])
    return mat

go = True
while go:
    R1 = create(3)
    R2 = create(3)
    R3 = create(3)

    matrix = []
    matrix.append(R1)
    matrix.append(R2)
    matrix.append(R3)
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])


    det = determinant(matrix)
    print (det)
    if det == 0:
        print("inverse of this matrix does not exist")
        nope = True
    else:
        adjugate = adj(minor(matrix))
        print("")
        print("    ",adjugate[0])
        print("1/"+str(det),adjugate[1])
        print("    ",adjugate[2])

    print("")
    print("")
    print("")
