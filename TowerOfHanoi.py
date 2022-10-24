#towers of hanoi function
def TowerOfHanoi(n, tower1, tower3, tower2):
    if n == 0:
        return
    TowerOfHanoi(n-1, tower1, tower2, tower3 )
    print("Move disk", n, "from rod", tower1, "to rod", tower2)
    TowerOfHanoi(n-1, tower3, tower2, tower1)
    
#Driver Code
N = 3


# A, C, B are the name of the rods
TowerOfHanoi(N, 'A', 'C', 'B')

#probably wrong order? not sure
