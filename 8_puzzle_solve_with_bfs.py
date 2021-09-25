import numpy as np

print("Enter your matrix: ")
mat=[[int(input()) for i in range(3)] for j in range(3)]
start=np.array(mat)
goal=np.array([[1,2,3],[4,5,6],[7,8,0]])

class PuzzleSolve:
    def __init__(self,matno,parentno,mat):
        self.matno=matno
        self.parentno=parentno
        self.mat=mat
    
    
q=[]
matno=1
startstate=PuzzleSolve(matno,0,start)
q.append(startstate)
secondary_q=[]

def checkgoal(popped_mat):
    if (np.array_equal(popped_mat,goal)):
        return True
    else:
        return False
def findblank(front):
    for i in range(len(front)):
        for j in range(len(front[i])):
            if front[i][j] == 0:
                return (i, j)
# pos=findblank(0,matrix1)
def solution(state):
    if(state.parentno ==0):
        print(state.mat)
    else:
        parent=secondary_q[state.parentno - 1]
        solution(parent)
        print(state.mat)





while(True):
    front=q.pop(0)
    secondary_q.append(front)
    if(checkgoal(front.mat)):
        print("Goal found!")
        solution(front)
        break
    r_c=findblank(front.mat)
    convert=list(r_c)
    r=convert[0]
    c=convert[1]
   
    mat1=front.mat.copy()
    mat2=front.mat.copy()
    mat3=front.mat.copy()
    mat4=front.mat.copy()
    rowup=r-1
    if rowup>=0:
        temp=mat1[r][c]
        mat1[r][c]=mat1[r-1][c]
        mat1[r-1]=temp
        matno+=1
        newstate=PuzzleSolve(matno,front.matno,mat1)
        q.append(newstate)
    rowdown=r+1
    if rowdown<3:
        temp=mat2[r][c]
        mat2[r][c]=mat2[r+1][c]
        mat2[r+1][c]=temp
        matno+=1
        newstate=PuzzleSolve(matno,front.matno,mat2)
        q.append(newstate)
    colleft=c-1
    if colleft>=0:
        temp=mat3[r][c]
        mat3[r][c]=mat3[r][c-1]
        mat3[r][c-1]=temp
        matno+=1
        newstate=PuzzleSolve(matno,front.matno,mat3)
        q.append(newstate)
    colright=c+1
    if colright<3:
        temp=mat4[r][c]
        mat4[r][c]=mat4[r][c+1]
        mat4[r][c+1]=temp
        matno+=1
        newstate=PuzzleSolve(matno,front.matno,mat4)
        q.append(newstate)