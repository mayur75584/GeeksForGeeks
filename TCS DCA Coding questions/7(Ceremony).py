'''
There are 26 chairs that need to be arranged for a ceremony.
The chairs are named from A to Z . Every chair should be arranged according to the ordinal number of the letter
 in the English alphabet.
 Due to some misunderstanding, the chairs are randomly arranged.
 Given a str, the task here is to find the number of chairs which are correctly placed
  as per the ordinal number of the letters as given below.

  The same positions apply for both uppercase and lowercase letters.

  Example1:
  Input1:
  abcxyz
  Output:
  3-Number of chairs that are correctly placed as 3 per ordinal position of the
  letters of the English alphabet.

  Explanation:
  From the inputs given above: Letters a,b and c are in correct positions
  1,2, and 3, respectively Rest of Letters are not in the correct positions.
  Hence the output is 3.

  Example2:
  Input:
  abcxyzgh
  Output:
  5-Number of chairs that are correctly placed as per the ordinal position of the
  letters of the English alphabet.
'''
def func(s):
    z=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    z1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    count1=0
    for i in range(len(s)):
        if s[i]==z[i] or s[i]==z1[i]:
            count1+=1
    return count1


if __name__ == '__main__':
    # s=input()
    # s='abcxyzgh'
    s='abcxyz'
    res=func(s)
    print(res)