'''
https://www.technoname.com/index.php/2021/09/28/tcs-digital-capability-assessment-solutions-28-sept-2021/
'''
'''
    A faulty program stores values from the username and password fields as a continuous sequence of characters. 
    When trying to fetch either the username or password, the entire string is displayed Given the string str, 
    the task here is to find and extract only the letters and special characters from the whole string stored.

    Note:

    The letters and special characters should be displayed separately.

    The output should consist of all the letters, followed by all the special characters present in the input string.
    
    Example1:
    Input:
    name@1234password - Value of str
    Output:
    namepassword@ - only letters and special characters
    
    Explanation:
    From the inputs given above string name@1234password, Extracting only lettrs
    and special characters
    
    Constraints
    Str=[A-Z,a-z,0-9,special characters]
    
    The input format for testing:
    The candidate has to write the code to accept 1 input 
    First Input - 
    Accept value of str(String)
    
    The output format for testing:
    The output should be only letters and special characters from
    the input string(check the output in Example1).
    
    Additional messages in output will cause the failure of test cases.
    
    Instructions:
    The system does not allow any kind of hardcoded input value/values.
    
'''
def func(str):
    s1=''
    s2=''
    for i in str:
        if i.isalpha():
            s1+=i
        elif i.isnumeric():
            continue
        elif i.isdigit():
            continue
        else:
            s2+=i
    return s1+s2



if __name__ == '__main__':
    # str=input()
    # str='name@1234password'
    str='mayur75584@gmail.com'
    res=func(str)
    print(res)


'''
JAVA Code

//Solution by technoname.com

import java.util.Scanner;

public class Technoname
{
    static String Result(String s)
    {
        String alphabets="",specialCharacter="";
        for(int i=0;i<s.length();i++)
        {
            if((s.charAt(i)>='A'&& s.charAt(i)<='Z') || (s.charAt(i)>='a'&& s.charAt(i)<='z'))
            {
            	alphabets+=s.charAt(i);
            }
            else if(!(s.charAt(i)>='0'&& s.charAt(i)<='9'))
            {
            	specialCharacter+=s.charAt(i);
            }
        }
        return alphabets+specialCharacter;
    }
 public static void main(String[] args) 
 {
  Scanner sc=new Scanner(System.in);
  String s=sc.nextLine();
  System.out.println(Result(s));
 }
}
'''