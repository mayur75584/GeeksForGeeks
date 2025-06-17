'''
Input will be like 5624381275.Separate odd places integers= 6,4,8,2,5.

You have to return a 4-digit OTP by squaring the digits. Digits according
to input are 6,4,8,2,5

Square those numbers - 36,16,64,4,25.

So, the OTP to be returned is first four digit i.e. 3616


Input: 5624381275

Output: 3616
'''
s1=input()
s2=''
s3=''
for i in range(1,len(s1),2):
    s2+=s1[i]
for i in s2:
    s3+=str(int(i)**2)
print(int(s3[:4]))
