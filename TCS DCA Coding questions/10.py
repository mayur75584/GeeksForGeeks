'Write complete question'
'''
    In an amusement park ticket booking system, reservations are stored in batches of user purchase as continuous ascending and nonrepeating reservation IDs.
    Reservation IDs are positive integers, set between 1 to 10000 and reset to 1 once 10000 is reached.
    Occasionally, it has been observed that for batches of booking between 3 and a maximum of 25 tickets by any user,
    one of the reservation IDs is omitted in the system. While a permanent fix is being provided by the software vendor,
    the task is to develop a program to identify the omitted reservation ID from such impacted batches. .

    The tickets are always sorted in ascending order.


'''

# N=int(input())
# ar=list(map(int,input().split()))
# N=5
# ar=[23,24,25,26,28]
N=7
ar=[1,2,4,5,6,7,8]
ar=sorted(ar)
for i in range(len(ar)-1):
    if ar[i]+1!=ar[i+1]:
        print(ar[i]+1)
        break

'''
JAVA code


import java.util.Arrays;
import java.util.Scanner;

class Technoname
{
	public static void main(String args[])
	{
	Scanner sc=new Scanner(System.in); 
	int num=sc.nextInt();
	int[] a=new int[num]; 
	int c=0;

	for(int i=0;i<num;i++) 
	{ 
		a[i]=sc.nextInt ();

	}

	Arrays.sort(a);

	for(int i=0;i<a.length-1;i++)
	{
		if(a[i+1]-a[i]!=1)
		{
			c=a[i+1]-1;
			break;

		}

	} 
	System.out.println(c);
	
}
}
'''



