"""  1    
    1 1   
   1 2 1  
  1 3 3 1 
 1 4 6 4 1"""
n=6
x=""
for i in range(0,n+1):
    print(" "*(n-i),end=" ")
    x=str(11**i)
    for j in x:
        print(j,end=" ")
    print()
       
      
