'''
Minimum number of chairs required to ensure that every worker is seated at any instant

Given a string S representing the record of workers entering and leaving the rest area, where E represents entering and
L represents leaving the rest area. For each worker, one chair is required. The task is to find the minimum number of chairs
required so that there is no shortage of chairs at any given time.

Examples:

    Input: S = “EELEE”
    Output: 3
    Explanation:
    Step 1: One person enters. Therefore, 1 chair is required for now.
    Step 2: Another person enters. Therefore, the number of chairs are required to be increased to 2.
    Step 3: One person leaves. Therefore, no need to increase the number of chairs.
    Step 4: Another person enters. Still, no need to increase the number of chairs.
    Step 4: Another person enters. Therefore, number of chairs are needed to be increased to 3.
    Therefore, minimum 3 chairs are required such that there is never a shortage of chairs.

    Input: S = “EL”
    Output: 1

Recommended: Please try your approach on {IDE} first, before moving on to the solution.

Approach: Follow the steps below to solve the problem:

    Initialize a variable, say, count.
    Iterate over the characters of the string using a variable, say i.
    If the ith character is ‘E’, then increase the count by 1, as more chairs are required.
    If the ith character is ‘L’, then decrease the count by 1 as one of the chairs is emptied.
    Print the maximum value of count obtained at any step.

Below is the implementation of the above approach:

Time Complexity - O(N)
Space Complexity - O(1)
'''
def findMinimumChairs(s):
    count1=0
    i=0
    mini=-99999
    while(i<len(s)):
        if s[i]=='E':
            count1+=1
        else:
            count1-=1
        mini=max(count1,mini)
        i+=1
    return mini



if __name__ == '__main__':
    s='EELEE'
    # s='EL'
    print(findMinimumChairs(s))