'''
https://www.technoname.com/index.php/2021/09/30/tcs-dca-questions-solved-30-sept-2021/
'''
'''
In the game of scrabble, in order to avoid over-usage of the same letters in any word, 
Mario is trying to calculate if a letter appears more than three times in any word and wants to discard such words. 
In order to assist Mario, write a program to identify the number of times the most repeating letter would appear within any word. 
If the output number is more than three, Mario shall discard such words and choose another word for the game.

Example1:
Input:
s=trumpet
Output:
2 - Highest number of repeating letters in the word "trumpet"

Explanation:
In the word "trumpet", the highest repeating letter is "t" repeated 2
times.

Example2:
Input:
reiterate - s
Output:
3-The highest number of repeating letters in the word reiterate.
Explanation:
The word "reiterate" has 3 occurrence of the letter the rest of the
letters appear only once.

Constraints:
s=(a-z)
The input format for testing:
The candidate has to write the code to accept 1 input.
Accept a single string value(lowercase 301016 alphabets).

The output format for testing.
->The output should be a positive integer number(check the output in Example1
and Example2).
->The system does not allow any kind of hard-coded input value/values.
->The written program code by the candidate will be verified against the
inputs which are supplied from the system.1
'''
def func(s):
    dict1={}
    for i in s:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    max1=0
    for i,j in dict1.items():
        if j>max1:
            max1=j
    return max1


if __name__ == '__main__':
    # s=input()
    # s='trumpet'
    # s='reiterate'
    # s='mayurmmm'
    s='komalllmmml'
    res=func(s)
    print(res)

'''
JAVA Code

import java.util.Scanner;

class Technoname
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		char[] freq = new char[256];
		int max =0;
		int count = 0;
	

		for(int i=0;i<str.length();i++)
		{
			freq[str.charAt(i)]++;
		}
		for(int i=0;i<str.length();i++)
		{
			if(freq[str.charAt(i)] >max)
			{
				max =freq[str.charAt(i)];
			}	
		}
		
		System.out.println(max);
		
	}
}
'''