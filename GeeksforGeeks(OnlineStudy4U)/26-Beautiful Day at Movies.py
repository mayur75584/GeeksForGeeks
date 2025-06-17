'''

'''
# # i,j,k=map(int,input().split())
# i,j,k=20,23,6
# lst=[]
# for a in range(i,j+1):
#     lst.append(a)
# print(lst)
# count=0

def beautifulDays(i, j, k):
    # Write your code here
    lst=[]
    for a in range(i,j+1):
        lst.append(a)
    count=0
    # print(lst)
    for i in lst:
        z=str(i)
        m=z[::-1]
        ans=abs(i-int(m))
        if ans%k==0:
            count+=1





    return count






if __name__ == '__main__':
    # i,j,k=map(int,input().split())
    # i,j,k=20,23,6
    i,j,k=1,2000000,1000000000
    # beautifulDays(i,j,k)

    result = beautifulDays(i, j, k)
    print(result)
