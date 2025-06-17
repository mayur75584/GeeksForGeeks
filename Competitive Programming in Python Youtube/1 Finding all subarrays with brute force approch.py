
#generate all the subarrays
def bruteforce(A):
    n=len(A)
    subarrays=[]
    for i in range(n+1):
        for j in range(i+1,n+1):
            s=A[i:j]
            subarrays.append(s)
    print(subarrays)


testcase = [-2,-3,4,-1,-2,1,5,-3]
bruteforce(testcase)