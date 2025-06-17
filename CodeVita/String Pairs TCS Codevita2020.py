'''
String Pairs | TCS Codevita 2020

    Difficulty Level : Medium
    Last Updated : 15 Jan, 2021

One person hands over the list of digits to Mr. String, But Mr. String understands only strings. Within strings also he understands only vowels. Mr. String needs your help to find the total number of pairs which add up to a certain digit D.

The rules to calculate digit D are as follows:

    Take all digits and convert them into their textual representation.
    Next, sum up the number of vowels i.e. {a, e, i, o, u} from all textual representation. This sum is digit D.
    Now, once digit D is known find out all unordered pairs of numbers in input whose sum is equal to D.

Problem Statement: Given an array arr[] consisting of N ( 1 ≤ N ≤ 100 ) integers, the task is to convert each array element ( 1 ≤ arr[i] ≤ 100 ) into their respective textual representations and print the lowercase representation of the count of all possible pairs from the array whose sum is equal to the total count of vowels present in their textual representation. If the count exceeds 100 print “greater 100”.
Note: For the number 100, convert it to textual representation as hundred and not as one hundred.

Examples:

    Input: arr[] = {1, 2, 3, 4, 5}
    Output: one
    Explanation:
    1 -> one -> o, e (2 vowels)
    2 -> two -> o (1 vowel)
    3 -> three -> e, e (2 vowels)
    4 -> four -> o, u (2 vowels)
    5 -> five – > i, e (2 vowels)
    The total count of vowels in their textual representations = {2 + 1 + 2 + 2 + 2} = 9.
    Now from the given array, only a single unordered pair {4, 5} sums up to 9. Therefore, the count is 1. Hence, the required output is “one“.


    Input: arr[] = {7, 4, 2, }
    Output: zero
    Explanation:
    7 -> seven -> e, e (2 vowels)
    4 -> four -> o, u (2 vowels)
    2 -> two -> o (1 vowel)
    The total count of vowels in their textual representation = {2 + 2 + 1} = 5.
    Now from the given array, no pair exists which adds up to 5. Therefore, the answer is “zero“.

Recommended: Please try your approach on {IDE} first, before moving on to the solution.

Approach: Follow the steps below to solve this problem:

    Store textual representation of each number from 0 to 100 in a Map.
    Traverse the array and for each array element, convert each digit to its textual form.
    Find the total number of vowels present in the textual forms and store it in a variable, say D.
    Now, generate all the pairs possible from the given array.
    Count all the pairs with sum D.
    If the count exceeds 100, “greater 100”. Otherwise, print its textual form.

Below is the implementation of the above approach:
'''


from itertools import combinations
def pairs(arr):
    words={0: 'zero', 1: 'one', 2: 'two', 3: 'three',
             4: 'four', 5: 'five', 6: 'six', 7: 'seven',
             8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
             12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
             18: 'eighteen', 19: 'nineteen', 20: 'twenty',
             21: 'twentyone', 22: 'twentytwo', 23: 'twentythree',
             24: 'twentyfour', 25: 'twentyfive', 26: 'twentysix',
             27: 'twentyseven', 28: 'twentyeight', 29: 'twentynine',
             30: 'thirty', 31: 'thirtyone', 32: 'thirtytwo',
             33: 'thirtythree', 34: 'thirtyfour', 35: 'thirtyfive',
             36: 'thirtysix', 37: 'thirtyseven', 38: 'thirtyeight',
             39: 'thirtynine', 40: 'forty', 41: 'fortyone',
             42: 'fortytwo', 43: 'fortythree', 44: 'fortyfour',
             45: 'fortyfive', 46: 'fortysix', 47: 'fortyseven',
             48: 'fortyeight', 49: 'fortynine', 50: 'fifty',
             51: 'fiftyone', 52: 'fiftytwo', 53: 'fiftythree',
             54: 'fiftyfour', 55: 'fiftyfive', 56: 'fiftysix',
             57: 'fiftyseven', 58: 'fiftyeight', 59: 'fiftynine',
             60: 'sixty', 61: 'sixtyone', 62: 'sixtytwo',
             63: 'sixtythree', 64: 'sixtyfour', 65: 'sixtyfive',
             66: 'sixtysix', 67: 'sixtyseven', 68: 'sixtyeight',
             69: 'sixtynine', 70: 'seventy', 71: 'seventyone',
             72: 'seventytwo', 73: 'seventythree', 74: 'seventyfour',
             75: 'seventyfive', 76: 'seventysix', 77: 'seventyseven',
             78: 'seventyeight', 79: 'seventynine', 80: 'eighty',
             81: 'eightyone', 82: 'eightytwo', 83: 'eightythree',
             84: 'eightyfour', 85: 'eightyfive', 86: 'eightysix',
             87: 'eightyseven', 88: 'eightyeight', 89: 'eightynine',
             90: 'ninety', 91: 'ninetyone', 92: 'ninetytwo',
             93: 'ninetythree', 94: 'ninetyfour', 95: 'ninetyfive',
             96: 'ninetysix', 97: 'ninetyseven', 98: 'ninetyeight',
             99: 'ninetynine', 100: 'hundred'}

    lst=[]
    vowels=['a','e','i','o','u']
    lst1=[]
    count=0
    # vowels='aeiou'
    for i in arr:
        c=0
        z=words[i] #one
        for j in z:
            if j in vowels:
                c+=1
        lst.append(c)
    print(lst)
    D=sum(lst)
    print(D)
    for i in arr:
        if i<=D:
            lst1.append(i)
    comb=combinations(lst1,2)
    for i in list(comb):
        if sum(i)==D:
            count+=1
    if count<=100:
        print(words[count])
    else:
        print("greater 100")








if __name__ == '__main__':
    # arr=list(map(int,input().split()))
    arr=[1,2,3,4,5]
    pairs(arr)