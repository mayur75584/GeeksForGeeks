'''
Migratory Birds

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type.
If more than 1 type has been spotted that maximum amount, return the smallest of their ids.



Example
arr=[1,1,2,2,3]
There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1

.

Function Description

Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

    int arr[n]: the types of birds sighted

Returns

    int: the lowest type id of the most frequently sighted birds

Input Format

The first line contains an integer,n
, the size of arr.
The second line describes arr as n

space-separated integers, each a type number of the bird sighted.

Constraints

5<=n<=2*10^5

It is guaranteed that each type is 1,2 ,3 , 4, or 5.

    .

Sample Input 0

6
1 4 4 4 5 3

Sample Output 0

4

Explanation 0

The different types of birds occur in the following frequencies:

 Type1:1 birds
 Type2:0 birds
 Type3: 1 birds
 Type4: 3 birds
 Type5: 1 birds

The type number that occurs at the highest frequency is type 4
, so we print 4 as our answer.

Sample Input 1

11
1 2 3 4 5 4 3 2 1 3 4

Sample Output 1

3

Explanation 1

The different types of birds occur in the following frequencies:
Type1:2
Type2:2
Type3:3
Type4:3
Type5:1

Two types have a frequency of 3, and the lower of those is type 3.
'''

def migratoryBirds(arr):
    lst=[]
    dict={}
    s1=set(arr)
    for i in s1:
        dict[i]=arr.count(i)
    # print(dict)
    # print(max(dict,key=dict.get))
    max_value = max(dict.values())
    for i,j in dict.items():
        if j==max_value:
            lst.append(i)
    # print(lst)
    return min(lst)


if __name__ == '__main__':
    # arr_count = int(input().strip())
    # arr = list(map(int,input().strip().split()))

    # arr_count = 11
    # arr=[1,2,3,4,5,4,3,2,1,3,4]

    arr_count=6
    arr=[1,4,4,4,5,3]
    # migratoryBirds(arr)
    result = migratoryBirds(arr)
    print(result)