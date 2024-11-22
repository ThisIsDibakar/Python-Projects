print("\n")
def RainWater(lst):

    L = len(lst)
    # L is the length of the list [ For Example: len([ 1, 2, 3, 4, 5 ]) = 5 ]

    left = [0] * L
    # left is an empty list [ For Example: [ 0, 0, 0, 0, 0 ] ]

    right = [0] * L
    # right is an empty list [ For Example: [ 0, 0, 0, 0, 0 ] ]


    left[0] = lst[0] 
    # For Example: If lst = [ 1, 2, 3, 4, 5 ] then left[0] = 1
    for i in range(1, L):
        left[i] = max(lst[i], left[i-1])


    right[-1] = lst[-1]
    # For Example: If lst = [ 1, 2, 3, 4, 5 ] then right[-1] = 5
    for i in range(L-2, -1, -1):
        right[i] = max(lst[i], right[i+1])


    water = 0
    for i in range(L):
        water = water + min(left[i], right[i]) - lst[i]


    return water


lst = eval(input("Enter the Blocks in List: "))
print("\n")

if __name__ == '__main__':
  print("The Number of Blocks of RainWater Stored are:", RainWater(lst))


print("\n")