'''


Input:
4
["red","blue","green","yellow"]
1
"yellow"
Output:
2

Input2:
5
["black","grey","brown","red","pink"]
3
"black"
Output2:
2
'''
def shiftCards(n,cards,ind,c):
    i,j=ind,ind
    count1=0
    count2=0

    while(cards[i]!=c):
        i-=1
        count1+=1
        if i<0:
            i=len(cards)-1
    while(cards[j]!=c):
        j+=1
        count2+=1
        if j>len(cards)-1:
            j=0
    return min(count1,count2)

if __name__ == '__main__':
    # n=int(input())
    # cards=[]
    # for i in range(n):
    #     cards.append(input())
    # ind=int(input())
    # c=input()
    n=4
    cards=["red","blue","green","yellow"]
    ind=1
    c='yellow'
    # n=5
    # cards=['black','grey','brown','red','pink']
    # ind=3
    # c='black'
    result=shiftCards(n,cards,ind,c)
    print(result)