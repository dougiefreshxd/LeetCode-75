# Climbing Stairs Dynamic Programming
# Problem:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you either climb 1 or 2 steps. In how many distinct ways can you climb
# to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n: int) -> int:
    startingPoint = [[0]]
    amountOfPossibilities = 0
    tempList = []

    while(startingPoint):
        for x in startingPoint:
            startingPoint.remove(x)
            lastVarInX = x[-1]

            if(lastVarInX + 1 < n): tempList.append([lastVarInX, lastVarInX + 1])
            elif(lastVarInX + 1 == n): amountOfPossibilities+=1
            else: pass

            if(lastVarInX + 2 < n): tempList.append([lastVarInX, lastVarInX + 2])
            elif(lastVarInX + 2 == n): amountOfPossibilities+=1
            else: pass

            if not startingPoint:
                startingPoint = tempList.copy()
                tempList = []
        
    return amountOfPossibilities


def fibsequence(n: int) -> int:
    x,y = 0,1
    for index in range(n):
        temp = x + y
        x = y
        y = temp
    return y


def main():
    print("Test Case 1: {}".format(climbStairs(2)==2))
    print("Test Case 2: {}".format(climbStairs(3)==3))
    print("Test Case 3: {}".format(climbStairs(4)==5))
    print("Test Case 4: {}".format(climbStairs(5)==8))
    print("Test Case 5: {}".format(climbStairs(6)==13))  
    print("Test Case 6: {}".format(climbStairs(7)==21))
    print("Test Case 7: {}".format(climbStairs(8)==34))
    print("Test Case 8: {}".format(climbStairs(9)==55))
    print("Test Case 9: {}".format(climbStairs(10)==89))


main()
