'''
Gadgets of Doraland

In Doraland, people have unique Identity Numbers called D-id. Doraemon owns the most popular gadget shop in Doraland. Since his gadgets are in high demand and he has only K gadgets left he has decided to sell his gadgets to his most frequent customers only. N customers visit his shop and D-id of each customer is given in an array array[ ]. In case two or more people have visited his shop the same number of time he gives priority to the customer with higher D-id. Find the D-ids of people he sells his K gadgets to.

Example 1:

Input:
N = 6
array[] = {1, 1, 1, 2, 2, 3}
K = 2
Output:
1 2
Explanation:
Customers with D-id 1 and 2 are most
frequent.

Example 2:

Input:
N = 8
array[] = {1, 1, 2, 2, 3, 3, 3, 4}
K = 2
Output:
3 2
Explanation: People with D-id 1 and 2 have
visited shop 2 times Therefore, in this
case, the answer includes the D-id 2 as 2 > 1.

Your Task:
You don't need to read input or print anything. Complete the function TopK() which takes array[ ] and integer K as input parameters and returns an array containing D-id of customers he has decided to sell his gadgets to.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
1 ≤ D-id ≤ 104
'''
class Solution:
    def TopK(self,array,k):
        dict={}
        for i in array:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        print(dict)
        z=sorted(dict.items(),key=lambda x:(x[1],x[0]),reverse=True)
        print(z)
        x=[]
        count1=0
        for i in z:
            x.append(i[0])
            count1+=1
            if count1==k:
                break
        return x



if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # array=[]
        # for i in range(n):
        #     array.append(int(input()))
        # k=int(input())

        n=8
        array=[1,1,2,2,3,3,3,4]
        k=2
        # n=6
        # array=[1,1,1,2,2,3]
        # k=2
        obj=Solution()
        res=obj.TopK(array,k)
        for j in res:
            print(j,end=' ')
        print()
