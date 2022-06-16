key=input("Enter key:")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    
    return [[initial for i in range(x)] for j in range(y)]   
result=[]
for c in key: #storing key
    if c not in result:
        result.append(c)
flag=0
for i in range(65,91): #storing other character
    if chr(i) not in result:
        result.append(chr(i))

flag=0

result.append("%")
result.append("&")
result.append("$")
result.append("!")
index=0
my_matrix=matrix(6,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,6):
        my_matrix[i][j]=result[index]
        index+=1
print(my_matrix)

def locindex(val): #get location of each character
    return [(index, row.index(val)) for index, row in enumerate(my_matrix) if val in row]
            
def to_list(msg):
    list = []
    for char in msg:
        list.append(char)
    return list

def to_string(a):
    str=""
    for i in range(len(a)):
        str+=a[i]
    return str


def encrypt():  #Encryption
    global my_matrix
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    
    msg_list = to_list(msg)

    while i<len(msg)-1:
        
        loc=list()
        loc=locindex(msg_list[i])

        loc1=list()
        loc1=locindex(msg_list[i+1])

        if loc[0][1]==loc1[0][1]:
            if loc[0][0] != 0:
                msg_list[i] = my_matrix[loc[0][0]-1][loc[0][1]]

            else:
                msg_list[i] = my_matrix[4][loc[0][1]]
            if loc1[0][0] !=0:
                msg_list[i+1] = my_matrix[loc1[0][0]-1][loc1[0][1]]
            else:               
                msg_list[i+1] = my_matrix[4][loc1[0][1]]

        elif loc[0][0]==loc1[0][0]:
            if loc[0][1] != 0 :
                msg_list[i] = my_matrix[loc[0][0]][loc[0][1]-1]
            else:
                msg_list[i] = my_matrix[loc[0][0]][5]
                
            if loc1[0][1] != 0 :
                msg_list[i+1] = my_matrix[loc1[0][0]][loc1[0][1]-1]
            else:
            
                msg_list[i+1] = my_matrix[loc1[0][0]][5]

        else:
            if loc[0][1] < loc1[0][1]:
                msg_list[i] = my_matrix[loc1[0][0]][loc[0][1]]
                msg_list[i+1] = my_matrix[loc[0][0]][loc1[0][1]]
            else:
                msg_list[i] = my_matrix[loc[0][0]][loc1[0][1]]
                msg_list[i+1] = my_matrix[loc1[0][0]][loc[0][1]]

        i =i+1    
    print("CIPHER TEXT:", to_string(msg_list)) 
def decrypt():  #decryption
    global my_matrix

    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    msg_list=to_list(msg)    
    i=len(msg_list)-1
    
    while i>0:
        loc=list()
        loc=locindex(msg_list[i])  
       # print(loc)  
         
        loc1=list()
        loc1=locindex(msg_list[i-1])
       # print(loc1)
       # print(msg_list[i],msg_list[i-1])
        if loc[0][1]==loc1[0][1]:
        
            if loc[0][0]!=4 :
                msg_list[i] = my_matrix[loc[0][0]+1][loc[0][1]]
            else:
                msg_list[i] = my_matrix[0][loc[0][1]]

            if(loc1[0][0]!=4):
                msg_list[i-1] = my_matrix[loc1[0][0]+1][loc1[0][1]]             
            else:
                msg_list[i-1] = my_matrix[0][loc1[0][1]]

        elif loc[0][0]==loc1[0][0]:
            if loc[0][1] != 5 and loc1[0][1]!=5:

                msg_list[i] = my_matrix[loc[0][0]][loc[0][1]+1]
                msg_list[i-1] = my_matrix[loc1[0][0]][loc1[0][1]+1]

            elif loc[0][1]==5 and loc1[0][1]!=5:
                msg_list[i] = my_matrix[loc[0][0]][0]  
                msg_list[i-1] = my_matrix[loc1[0][0]][loc1[0][1]+1] 
            else :
                msg_list[i] = my_matrix[loc[0][0]][loc[0][1]+1]
                msg_list[i-1] = my_matrix[loc1[0][0]][0]
         
        else:
            
            if loc[0][1]<loc1[0][1]:
                msg_list[i] = my_matrix[loc1[0][0]][loc[0][1]]
                msg_list[i-1] = my_matrix[loc[0][0]][loc1[0][1]]
               
            elif loc[0][1]>loc1[0][1]:
                msg_list[i-1] = my_matrix[loc1[0][0]][loc[0][1]]
                msg_list[i] = my_matrix[loc[0][0]][loc1[0][1]]
                       
        i=i-1       
    print("PLAIN TEXT:",msg_list)
while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")
