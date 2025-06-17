

class Solution:
    def maxDistance(self,arr,n):
        z=list(set(arr))
        max1=[]
        for i in z:
            x=arr.index(i)
            #Logic to find index of elemnet from last in list
            arr1=arr[::-1]
            z1=arr1.index(i)
            x1=(len(arr)-z1-1)
            # print(x,x1)
            max1.append(abs(x-x1))
        return max(max1)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=6
        # arr=[1,1,2,2,2,1]
        n=12
        arr=[3,2,1,2,1,4,5,8,6,7,4,2]
        ob=Solution()
        print(ob.maxDistance(arr,n))