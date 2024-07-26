'''Mani is given an n-by-n matrix of 0's and 1's where all 1's in each row come before all 0's, his task is to find the most efficient way to return the row with the maximum no of 0's.
Input:
First line of input contains a single integer T which denotes the no of testcases.First line of each testcase contains a single integer N which represent a size of matrix and next matrix elements.
Output:
For each testcase,print the row number.
Examples:
Input:
1
{{1,1,1,1},{1,1,0,0},{1,0,0,0},{1,1,0,0}}
Output:
2 '''
#way-2:finding the index position
for i in range(int(input())):
    nestlist=list(map(int,input().split()))
    n=len(nestlist)
    nestlist=[nestlist]
    for i in range(n-1):
        nestlist.append(list(map(int,input().split())))
    max_count=0
    for i in range(n):
        if max_count<nestlist[i].count(0):
            max_count=nestlist[i].count(0)
            index=i
    print(index) 
