'''n = int(input("Номер элемента-" ))'''
S = input()






'''def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print('Значение', fib(n))'''

def palindr(S):
    if len(S) <= 1:
        return True
    else:
        return S[0] == S[-1] and palindr(S[1:-1])

print(palindr(S))

