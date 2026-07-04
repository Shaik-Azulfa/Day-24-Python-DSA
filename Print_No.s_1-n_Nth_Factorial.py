#print no.s from 1 to n
class Solution:
    def printNos(self, n):
        #Your code here
        if n == 0:
            return
        self.printNos(n - 1)
        print(n, end = " ")
#Nth Fibonacci
class Solution:
    def nthFibonacci(self, n):
        #code here
        a = 0  # i=0
        b = 1  # i=1
        
        if n == 0:
            return a
        if n == 1:
            return b
            
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
            
        return b
