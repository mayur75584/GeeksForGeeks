
class Solution:
    def NumberofElementsInIntersection(self,a,b,n,m):
        z = set(a).intersection(set(b))
        return len(z)






if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        ob=Solution()
        print(ob.NumberofElementsInIntersection(a,b,n,m))


