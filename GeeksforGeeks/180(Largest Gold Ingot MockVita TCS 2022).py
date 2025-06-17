
'''
Largest Gold Ingot

Photos of question are taken in mobile
'''
def func(G,B,H,length):
    leftSmall=[0]*G
    rightSmall=[0]*G
    st = []
    # Left array
    for i in range(G):
        while (len(st) != 0 and length[st[-1]] >= length[i]):
            st.pop(-1)
        if (len(st) == 0):
            leftSmall[i] = 0
        else:
            leftSmall[i] = st[-1] + 1
        st.append(i)
    # print(leftSmall)

    while (len(st) != 0):
        st.pop(-1)

    # Right array
    for i in range(G - 1, -1, -1):
        while (len(st) != 0 and length[st[-1]] >= length[i]):
            st.pop(-1)
        if (len(st) == 0):
            rightSmall[i] = G - 1
        else:
            rightSmall[i] = st[-1] - 1
        st.append(i)
    # print(rightSmall)
    # Calculating Area and Finding Maximum Area
    maxA = 0
    for i in range(G):
        maxA = max(maxA, length[i] * ((rightSmall[i] - leftSmall[i]) + 1))

    return maxA

    #OR

    # s = [-1]
    # n = len(length)
    # area = 0
    # i = 0
    # left_smaller = [-1] * n
    # right_smaller = [n] * n
    # while i < n:
    #     while s and (s[-1] != -1) and (length[s[-1]] > length[i]):
    #         right_smaller[s[-1]] = i
    #         s.pop()
    #     if ((i > 0) and (length[i] == length[i - 1])):
    #         left_smaller[i] = left_smaller[i - 1]
    #     else:
    #         left_smaller[i] = s[-1]
    #     s.append(i)
    #     i += 1
    # for j in range(0, n):
    #     area = max(area, length[j] * (right_smaller[j] - left_smaller[j]- 1))
    # return area


if __name__ == '__main__':
    G=int(input())
    B,H=map(int,input().split())
    length=list(map(int,input().split()))
    # G=7
    # B,H=1,2
    # length=[1,2,6,4,5,3,4]
    # G=7
    # B,H=1,1
    # length=[6,7,3,4,5,1,3]
    res=func(G,B,H,length)
    cuboid=res*B*H
    # print(cuboid)
    vol_gold=0
    z=sum(length)*B*H
    # print(z)
    ans=abs(z-cuboid)
    print(ans)