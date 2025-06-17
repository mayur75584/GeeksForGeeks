'''
Question number 1 of IPA sample questions pdf


Sample Input-
3
Hello
Malayalam
Radar

Sample Output-
Malayalam
Radar
'''

def check_palindrome(inp_str):
    res=[]
    for i in inp_str:
        if i.lower()==i[::-1].lower():
            res.append(i)
    return res




if __name__ == '__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
    output=check_palindrome(inp_str)
    if len(output)!=0:
        for j in output:
            print(j)
    else:
        print("No palindrome found")

