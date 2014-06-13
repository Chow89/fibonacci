import math

#calculates the n-th number of fibonacci recursive
def fibr(n):
    if n==0 or n==1:
        return n
    else:
        return fibr(n-1)+fibr(n-2)

#calculates the n-th number of fibonacci iterative
def fibi(n):
    if n==0 or n==1:
        return n
    else:
        first=0
        second=1
        summe=0
        i=2
        while i<=n:
            summe=first+second
            first=second
            second=summe
            i=i+1
        return summe

#calculates the n-th number of fibonacci by the formula of moivre and binet
def fibc(n):
    return round(1/math.sqrt(5)*((((1+math.sqrt(5))/2)**n)-((1-math.sqrt(5))/2)**n))
            
print (fibr(10))
print (fibi(10))
print (fibc(10))
