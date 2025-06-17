'''
Question number 7 of IPA sample questions pdf

Sample Input-
4
11
7
90
44

Sample Output-
1
[[11, 7], [90, 44]]
'''

def check_prime(number):
    if number>1:
        for j in range(2,number):
            if number%j==0:
                return 0
        else:
            return 1
    else:
        return 0

def prime_composite_list(list_numbers):
    prime=[]
    composite=[]
    for i in list_numbers:
        if i>1:
            if check_prime(i)==1:
                prime.append(i)
            elif check_prime(i)==0:
                composite.append(i)
        else:
            continue
    result=[]
    result.append(prime)
    result.append(composite)
    return result



if __name__ == '__main__':
    n=int(input())
    list_numbers=[]
    for i in range(n):
        list_numbers.append(int(input()))
    print(check_prime(list_numbers[1]))
    result=prime_composite_list(list_numbers)
    print(result)