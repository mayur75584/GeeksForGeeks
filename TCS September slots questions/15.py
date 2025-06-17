'''
In a puzzle game, there are five blocks. Each block is assigned with some repeating numbers

Block 1








1     ------------->

9    ←----------




2----------------->

8 ←---------------

10 --------------->


3-------------->

7←------------

11------------->


4--------------->

 6←------------

12-------------->

So on


5

13

The number 1 starts from block-1,2 on block-2,3 on block -3, 4 on block-4 and 5 on block-5. Again 6 on block-4 and so on.

Here we observe a pattern, the numbers 10,8 and 2 are on block-2 , 3,7 and 11 on the block 3 and so on.

Given a positive integer N. The task is to find the correct block to which the number assigned.

Example 1:

Input :

3   ---> Value of N

Output :

3    -> Block number

Example 2:

Input :

16    ---> Value of N

Output :

2    ---> Block number

The input format for testing

The candidate has to write the code to accept one input

First input - Accept value for number of N (Positive integer number)

The output format for testing

The output should be a positive integer (Check the output  in Example 1, Example 2)


'''