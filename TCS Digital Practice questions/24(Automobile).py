'''
An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:

    1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
    2nd data, Total number of wheels = W



The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.



Example :

Input :

    200  -> Value of V
    540   -> Value of W

Output :

    TW =130 FW=70



Explanation:

130+70 = 200 vehicles

(70*4)+(130*2)= 540 wheels



Constraints :

    2<=W
    W%2=0
    V<W



Print “INVALID INPUT” , if inputs did not meet the constraints.

The input format for testing

The candidate has to write the code to accept two positive numbers separated by a new line.

    First Input line – Accept value of V.
    Second Input line- Accept value for W.



The output format for testing

    Written program code should generate two outputs, each separated by a single space character(see the example)
    Additional messages in the output will result in the failure of test case
'''
'''
Logic

x+y=V
2x+4y=W

y=V-x

2x=W-4y
2x=W-4(V-x)
2x=W-4V+4x
-2x=(W-4V)
2x=4V-W
x=(4V-W)//2
'''
'''
W&1 means it will give 1 if 1&1 , means we have only 1 wheel other than that it gives 0 meas have more than 1 wheels
'''
def func(V,W):

    x=((4*V)-W)//2
    y=V-x

    if((W&1)==1) or W<2 or W<=V:
        print("INVALID INPUT")
    else:
        print('TW ={} FW ={}'.format(x,y))



if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        V=int(input())
        W=int(input())
        # V=200
        # W=540
        # V=100
        # W=160
        func(V,W)



