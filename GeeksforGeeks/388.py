'Need to work on this code , the one which using input is failing'
'https://www.geeksforgeeks.org/problems/account-merge/1'
'Not able to solve all test cases'
class Solution:
    def accountsMerge(self,accounts):
        dict1={}
        dict2={}
        # for i in accounts:
        #     print(i[0])
        x=[i[0] for i in accounts]
        print(x)
        y=[i[1:] for i in accounts]
        print(y)
        res=list(set.intersection(*map(set,y)))
        print(res)
        for i in range(len(x)):
            if x[i] not in dict1:
                dict1[x[i]]=sorted(set(y[i]))
                print(dict1,end='\n')
            else:
                if x[i] in dict1:
                    k=set(dict1[x[i]])
                    print(k)
                    k1=set(y[i])
                    k2=k.intersection(k1)
                    print(k2)
                    if len(k2)>0:
                        dict1[x[i]]=sorted(list(k.union(k1)))
                        print(dict1)
                    else:
                        dict2[x[i]]=sorted(set(y[i]))
        print(dict1,dict2)
        names=list(dict1.keys())+list(dict2.keys())
        print(names)
        emails=list(dict1.values())+list(dict2.values())
        print(emails)
        for i in range(len(emails)):
            emails[i].insert(0,names[i])
        # print("ans",emails)
        return emails





if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # accounts=[]
        # for i in range(n):
        #     cntEmails=int(input())
        #     nameEmails=input().split()
        #     accounts.append(nameEmails)
        # n=4
        # accounts=[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
#         n=5
#         accounts=[["Gabe","Gabe00@m.co","Gabe3@m.co","Gabe1@m.co"],
# ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
# ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
# ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
# ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
#         n=6
#         accounts=[["mark","mark2@gmail.com"],["alice", "alice2@mail.com" ,"alice9@google.in" ,"alice6gfg.org"],["fern" ,"fern9gfg.org" ,"fern3@mail.com" ,"fern3@mail.com" ,"fern7gfg.org" ,"fern2gfg.org" ,"fern8@mail.com"],
#                   ["kevin" ,"kevin0gfg.org" ,"kevin3@mail.com" ,"kevin2@gmail.com" ,"kevin8@gmail.com" ,"kevin8@mail.com"]
#                   ,["kevin" ,"kevin1@gmail.com" ,"kevin6@google.in" ,"kevin6@google.in" ,"kevin2@mail.com" ,"kevin7@google.in" ,"kevin5@gmail.com" ,"kevin9gfg.org"],
#                   ["bob" ,"bob3@gmail.com", "bob4@mail.com"]]
        n=41
        accounts=[["mark","mark1@google.in","mark1@google.in","mark0@google.in","mark1@gmail.com","mark8@gmail.com","mark2@mail.com"],
                  ["john","john5@mail.com","john5gfg.org","john2@google.in","john7@gmail.com","john1@gmail.com","john2@mail.com"],
                  ["mark","mark9gfg.org","mark4@google.in","mark9@gmail.com","mark4@gmail.com","mark5@mail.com"],
                  ["bob","bob3@mail.com","bob3@mail.com","bob4gfg.org","bob4gfg.org","bob9gfg.org","bob7@mail.com","bob7@google.in"],
                  ["bob","bob7@google.in","bob3@gmail.com","bob9@google.in","bob2@google.in","bob3@mail.com"],
                  ["mark","mark4@google.in","mark4gfg.org","mark5@gmail.com","mark7@mail.com","mark3gfg.org","mark4gfg.org"],
                  ["kevin","kevin9@mail.com","kevin0@google.in","kevin6gfg.org","kevin9@google.in","kevin6gfg.org"],
                  ["john","john8@mail.com"],
                  ["alice","alice6gfg.org","alice6@gmail.com","alice3@google.in","alice9@gmail.com","alice5@google.in","alice1@mail.com","alice8@mail.com","alice8@mail.com"],
                  ["kevin","kevin6gfg.org","kevin5@gmail.com","kevin2@google.in","kevin0@google.in","kevin1@mail.com","kevin0@gmail.com"],
                  ["bob","bob2@google.in","bob0@mail.com","bob2@gmail.com","bob2@mail.com","bob9@gmail.com","bob2@mail.com","bob6@mail.com","bob4@gmail.com"],
                  ["kevin","kevin4@google.in","kevin8@mail.com","kevin6gfg.org","kevin7gfg.org","kevin4@mail.com","kevin0@mail.com"],
                  ["levin","levin8@gmail.com","levin0gfg.org","levin1@google.in","levin7@gmail.com","levin2@gmail.com","levin3@mail.com"],
                  ["bob","bob2@google.in","bob2@mail.com","bob8@google.in","bob1gfg.org"],
                  ["levin","levin8@gmail.com","levin8@gmail.com","levin5gfg.org"],
                  ["alice","alice2@google.in","alice8@mail.com","alice2@mail.com","alice0@google.in","alice3gfg.org","alice2@mail.com","alice0gfg.org","alice7@gmail.com"],
                  ['john', 'john2gfg.org', 'john8gfg.org'],
                  ['fern', 'fern8gfg.org', 'fern2@mail.com', 'fern5@mail.com', 'fern7gfg.org', 'fern4gfg.org', 'fern0@gmail.com'],
                  ['kevin', 'kevin9@google.in', 'kevin9gfg.org', 'kevin8@google.in'],
                  ['fern', 'fern2@google.in'],
                  ['levin', 'levin7@google.in', 'levin8@mail.com', 'levin9@google.in'],
                  ['levin', 'levin1@mail.com', 'levin6@google.in', 'levin9gfg.org', 'levin0gfg.org', 'levin0gfg.org', 'levin7@mail.com', 'levin1@mail.com', 'levin9@google.in', 'levin2@mail.com'],
                  ['mark', 'mark7@google.in', 'mark5@gmail.com', 'mark0@google.in', 'mark0gfg.org', 'mark7@mail.com', 'mark1@mail.com', 'mark6@google.in'],
                  ['alice', 'alice3@mail.com', 'alice6gfg.org', 'alice2gfg.org', 'alice8gfg.org', 'alice0@mail.com', 'alice3gfg.org', 'alice8@gmail.com'],
                  ['bob', 'bob7gfg.org', 'bob7@google.in', 'bob1@mail.com'],
                  ['fern', 'fern0@mail.com', 'fern7@google.in', 'fern3gfg.org', 'fern3@gmail.com', 'fern1@google.in', 'fern0@gmail.com', 'fern1gfg.org'],
                  ['alice', 'alice0@google.in', 'alice1@mail.com', 'alice0gfg.org', 'alice7@google.in', 'alice3@mail.com', 'alice0gfg.org', 'alice7@gmail.com', 'alice3@gmail.com'],
                  ['levin', 'levin9@mail.com', 'levin6@google.in', 'levin6@google.in', 'levin9@gmail.com'],
                  ['levin', 'levin4@mail.com', 'levin6@google.in'],
                  ['john', 'john7@google.in', 'john0@mail.com', 'john7@gmail.com', 'john6@google.in', 'john5@google.in', 'john3@google.in', 'john6@mail.com', 'john4@gmail.com'],
                  ['kevin', 'kevin2@gmail.com', 'kevin8gfg.org', 'kevin9@google.in', 'kevin7@gmail.com', 'kevin1gfg.org'],
                  ['alice', 'alice5@google.in', 'alice7gfg.org', 'alice2@google.in', 'alice2@mail.com', 'alice7@mail.com', 'alice0@gmail.com', 'alice5@mail.com', 'alice8@google.in'],
                  ['kevin', 'kevin6gfg.org', 'kevin3@google.in'],
                  ['john', 'john0@mail.com', 'john9@google.in', 'john5@google.in', 'john8@gmail.com', 'john2@gmail.com'],
                  ['kevin', 'kevin4gfg.org', 'kevin8@google.in', 'kevin2@mail.com', 'kevin6gfg.org', 'kevin2@mail.com'],
                  ['kevin', 'kevin4@gmail.com'],
                  ['john', 'john0@mail.com', 'john3@google.in', 'john6@google.in', 'john8@google.in', 'john7@google.in', 'john0@gmail.com', 'john4@mail.com'],
                  ['mark', 'mark2@gmail.com', 'mark8@google.in', 'mark1@google.in', 'mark9@google.in', 'mark8gfg.org'],
                  ['bob', 'bob9@google.in', 'bob1gfg.org'],
                  ['levin', 'levin9@mail.com', 'levin3@google.in', 'levin8@google.in', 'levin7gfg.org', 'levin0gfg.org', 'levin5@gmail.com', 'levin0@gmail.com', 'levin0@mail.com'],
                  ['mark', 'mark3@gmail.com', 'mark8@google.in', 'mark4@google.in', 'mark6@gmail.com', 'mark7gfg.org']]
        ob=Solution()
        res=ob.accountsMerge(accounts)
        res.sort()
        print('[',end='')
        for i in range(len(res)):
            print('[',end='')
            for j in range(len(res[i])):
                if j!=(len(res[i])-1):
                    print(res[i][j],end=',')
                else:
                    print(res[i][j],end=',')
            if(i!=len(res)-1):
                print('] ')
            else:
                print(']',end='')
        print(']')
