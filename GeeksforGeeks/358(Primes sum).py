'''
Primes sum

Given a number N. Find if it can be expressed as sum of two prime numbers.

Example 1:

Input: N = 34
Output: "Yes"
Explanation: 34 can be expressed as
sum of two prime numbers.

Example 2:

Input: N = 23
Output: "No"
Explanation: 23 cannnot be expressed as
sum of two prime numbers.


Your Task:
You dont need to read input or print anything.
Complete the function isSumOfTwo() which takes N as input parameter
and returns "Yes" if can be expressed as sum of two prime numbers.
else return "No".

Expected Time Complexity: O(N*sqrt(N))
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105

'''
'Solution in JAVA'
'''
import java.util.*;
import java.io.*;
class GFG{
    public static void main(String args[]) throws IOException{
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(read.readLine());
        while(t-->0){
            int N=Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.isSumOFTwo(N));
        }
    }
}

class Solution {
    static String isSumOfTwo(int N){
        // code here
        boolean[] primes = new boolean[N];
        Arrays.fill(primes,true);
        for(int i=2;i*i<=N;i++){
            if(primes[i]){
                for(int j=i*i;j<N;j+=i){
                    primes[j]=false;
                }
            }
        }
        for(int i=2;i<=N/2;i++){
            if(primes[i] && primes[N-i]){
                return "Yes";
            }
        }
        return "No";
    }
}
'''
# 'Gettint TLE for Python Solution so done in JAVA'
# class Solution:
#     def isSumOfTwo(self,N):
#         if(N<2):
#             return "No"
#         primes=[True for i in range(N+1)]
#         primes[0]=primes[1]=False
#         p=2
#         while(p*p<=N):
#             if(primes[p]==True):
#                 for i in range(p*p,N+1,p):
#                     primes[i]=False
#             p+=1
#         for i in range(2,N+1):
#             if(primes[i] and primes[N-i]):
#                 return "Yes"
#         return "No"
#     'Getting TLE for below solution'
#     # def SieveOfEratosthenes(self,N,isPrime):
#     #     isPrime[0]=isPrime[1]=False
#     #     for i in range(2,N+1):
#     #         isPrime[i]=True
#     #     p=2
#     #     while(p*p<=N):
#     #         if(isPrime[p]==True):
#     #             i=p*p
#     #             while(i<=N):
#     #                 isPrime[i]=False
#     #                 i+=p
#     #         p+=1
#     # def isSumOfTwo(self,N):
#     #
#     #     isPrime=[0]*(N+1)
#     #     self.SieveOfEratosthenes(N,isPrime)
#     #     for i in range(0,N+1):
#     #         if(isPrime[i] and isPrime[N-i]):
#     #             return "Yes"
#     #     return "No"
#
# if __name__ == '__main__':
#     # t=int(input())
#     t=1
#     for _ in range(t):
#         # N=int(input())
#         # N=34
#         # N=23
#         N=4
#         ob=Solution()
#         print(ob.isSumOfTwo(N))