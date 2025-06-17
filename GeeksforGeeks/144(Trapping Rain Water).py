'Correct Solution but getting TLE'
class Solution:
    def trappingWater(self,arr,n):
        sumOfWaterCollected = 0
        for i in range(1,n-1):
            left = arr[i]
            for j in range(i):
                left=max(left,arr[j])
            right = arr[i]
            for j in range(i+1,n):
                right = max(right,arr[j])
            sumOfWaterCollected=sumOfWaterCollected+min(left,right)-arr[i]
        return sumOfWaterCollected
if __name__ == '__main__':
    # T=int(input())
    T=1
    while (T!=0):
        # n=int(input())
        # arr=[]
        # for i in range(n):
        #     arr.append(int(input()))
        # n=6
        # arr=[3,0,0,2,0,4]
        # n=4
        # arr=[7,4,0,9]
        n=3
        arr=[6,9,9]
        obj=Solution()
        print(obj.trappingWater(arr,n))
        T-=1