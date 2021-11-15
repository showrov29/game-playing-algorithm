

matrix=[[6,1,10,2],[7,11,4,14],[5,0,5,15],[8,12,13,3]]
inver=[]
def inversion(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 4):
        for j in range(i + 1, 4):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
    

def isSolvable(puzzle) :
 
    
    inv_count = inversion([j for sub in puzzle for j in sub])
 
   
    return (inv_count % 2 == 0)
    
      
if(isSolvable(matrix)) :
    print("Solvable")
else :
    print("Not Solvable")

#tiktiki bokachuda
    

