'Below question has came in TCS DCA exam'
'''
Most modern aircrafts are equipped with an autopilot system – one of the most useful features in fighter jets.
In the beta testing of autopilot mode, one of the inputs is a string of literals containing the directions,
which is fed into the flight computer before the take-off. The jet plane is put on an auto-landing mode that enables
the plane to land automatically once all the directions in the string are complete Given the directions in the string
str, the task here is to find out whether the jet plane returns to the same returns to the same
position on the base where it took off.

. Each direction in the string changes at an interval of 1 minute(1<=i<=N), where N
is the number of directions in the input string.
. The directions are North(N),South(S),West(W) and East(E)
. Display a message "Returned successfully" if the plane returns to the starting
position.
. Display a message "Not returned successfully" if the plane does not return
to the starting postion.

Example 1:
Input -
NESW - Value of str
Output-
Returned successfully

Example 2:
Input -
NNWESW - Value of str
Output-
Not returned successfully
'''

def func(s):
    if s.count('N')==s.count('S') and s.count('E')==s.count('W'):
        return 'Return successfully'
    else:
        return 'Not returned successfully'


if __name__ == '__main__':
    # s=input()
    # s='NESW'
    s='NNWESW'
    res=func(s)
    print(res)


