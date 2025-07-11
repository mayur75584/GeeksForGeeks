'''
The Bit Game

Two players, Player 1 and Player 2, are given an integer N to play a game.
The rules of the game are as follows :
1. In one turn, a player can remove any set bit of N in its binary representation to make a new N.
2. Player 1 always takes first turn.
3. If a player cannot make a move, he loses.



Example 1:

Input:
N = 8
Output:
1
Explanation:
N = 8
N = 1000 (binary)
Player 1 takes the bit.
The remaining bits are all zero.
Player 2 cannot make a move,
so Player 1 wins.





Example 2:

Input:
N = 1
Output:
1
Explanation:
N = 0001
Player 1 takes one in one
move, so Player 2 loses.



Your Task:

You don't need to read input or print anything.
Your task is to complete the function swapBitGame() which takes an integer N
3and returns "1" if Player 1 wins, else return "2".



Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)



Constraints :
1 <= N <= 10^12
'''

class Solution:
    def swapBitGame(self,N):
        b=bin(N).replace('0b','')
        count1=b.count('1')
        if(count1%2==0):
            return 2
        else:
            return 1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=8
        N=1
        ob=Solution()
        print(ob.swapBitGame(N))