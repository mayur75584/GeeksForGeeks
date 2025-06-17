'''
A chocolate distributor unit has installed two new automatic arms for the unloading of chocolate bars from containers.
Arm A has the capacity to unload one chocolate bar, whilst the other arm B unloads two bars at
a time. In order for any two-containers to be unloaded fully and simultaneously by both arms, the distributor has to choose the correct chocolate bars quantity
(quantity X for container unloaded by arm A and quantity Y for container unloaded by arm B) in those containers from the supplier.

The task is to develop a code to identify a pair of quantities (maximum quantity 5000)
such that both the arms unload all chocolate bars from those containers fully and complete their unloading simultaneously,
so the following containers can be placed for unloading automatically.

The correct pair identified can be marked as "Yes" and the Incorrect pair as "No".

Example1:
Input -
100
200
Output-
Yes
(Prints Yes indicating 100 and 200 chocolates bars can be fully emptied simultaneously)

Example2-
500
900
Output-
No
(Prints No indicating 500 and 900 chocolate bars cannot be fully emptied
simultaneously).

Explanation:
Arm A unloads 500 bars in 500 times and Arm B also unloads 900 bars in 450
times. Hence both the containers are not emptied at the same time and so,
the next pair of containers cannot be automatically placed for unloading until arm A
unloads another 50 bars.
Hence the output is "No".
'''


X=int(input())
Y=int(input())
if(X*2==Y):
    print("Yes")
else:
    print("No")