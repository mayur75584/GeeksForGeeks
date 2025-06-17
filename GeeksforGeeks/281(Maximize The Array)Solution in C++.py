'''
Maximize The Array

Given two integer arrays Arr1 and Arr2 of size N.
Use the greatest elements from the given arrays to create a new array of size N
such that it consists of only unique elements and the sum of all its elements is maximum.
The created elements should contain the elements of Arr2 followed by elements of Arr1
in order of their appearance.

Example 1:
Input:
N = 5
Arr1 = {7, 4, 8, 0, 1}
Arr2 = {9, 7, 2, 3, 6}
Output: 9 7 6 4 8
Explanation: 9, 7, 6 are from 2nd array
and 4, 8 from 1st array.

Example 2:
Input: N = 4
Arr1 = {6, 7, 5, 3}
Arr2 = {5, 6, 2, 9}
Output: 5 6 9 7
Explanation: 5, 6, 9 are from 2nd array
and 7 from 1st array.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function maximizeArray() which takes the array arr1[],
arr2[] and n as input parameters and returns the desired array of integers.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
0 <=| Arr1[i] |<= 109
0 <= |Arr2[i] |<= 109

View Bookmarked Problems
Company Tags
Topic Tags
Arrays
Mathematical
Numbers
Heap

'''

'Solution is correct but getting TLE for below solution in Python'
# class Solution:
#     def maximizeArray(self,arr1,arr2,n):
#         'Solution is correct but getting TLE for below solution in Python'
#         ans=[]
#         z=[]
#         for i in range(n):
#             if arr2[i] not in z:
#                 z.append(arr2[i])
#             if arr1[i] not in z:
#                 z.append(arr1[i])
#         z.sort()
#         print(z)
#         while(len(z)>n):
#             z.pop(0)
#         print(z)
#         for i in range(n):
#             if arr2[i] in z:
#                 ans.append(arr2[i])
#                 z.remove(arr2[i])
#         for j in range(n):
#             if arr1[j] in z:
#                 ans.append(arr1[j])
#                 z.remove(arr1[j])
#         return ans
#
#
# if __name__ == '__main__':
#     # t=int(input())
#     t=1
#     while(t>0):
#         # n=int(input())
#         # arr1=list(map(int,input().split()))
#         # arr2=list(map(int,input().split()))
#         # n=5
#         # arr1=[7,4,8,0,1]
#         # arr2=[9,7,2,3,6]
#         n=4
#         arr1=[6,7,5,3]
#         arr2=[5,6,2,9]
#         ob=Solution()
#         ans=ob.maximizeArray(arr1,arr2,n)
#         for i in ans:
#             print(i,end=' ')
#         print()
#         t-=1

'Same solution in C++ not getting TLE'

'''
#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> maximizeArray(int arr1[], int arr2[], int n) {
            // code here 
        vector<int> ans;
        set<int> s;
        for(int i=0;i<n;i++){
            s.insert(arr1[i]);
            s.insert(arr2[i]);
        }
        while(s.size()>n){
            s.erase(*s.begin());
        }
        for(int i=0;i<n;i++){
            if(s.find(arr2[i])!=s.end()){
                ans.push_back(arr2[i]);
                s.erase(arr2[i]);
            }
        }
        for(int i=0;i<n;i++){
            if(s.find(arr1[i])!=s.end()){
                ans.push_back(arr1[i]);
                s.erase(arr1[i]);
            }   
        }
        return ans;
    }
    
};

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,i;
        cin>>n;
        int arr1[n],arr2[n];
        for(i=0;i<n;i++){
            cin>>arr1[i];
        }
        for(i=0;i<n;i++){
            cin>>arr2[i];
        }
        Solution ob;
        auto ans=ob.maximizeArray(arr1,arr2,n);
        for(auto x:ans){
            cout<<x<<" ";
        }
        cout<<"\n";
    }
    return 0;
}

        
'''