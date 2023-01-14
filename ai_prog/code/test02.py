'''
    파이 값을 구하는 방법중에 Leibniz 수열을 이용하는 방법이 있다.
    위 식을 이용하여 파이 값을 구하는 코드를 작성하시오.
'''

def getPi(cnt = 10000):
    pi = 0
    print('*' * 20, '파이 값', '*' * 20)
    for n in range(0, cnt + 1):
        pi = pi + ((-1) ** n * 4 / (2 * n + 1))
        if n < 5 or n > cnt - 5:
            if n == 0:
                print('%9s : ' % ('초기값'), pi)
            else :
                print('%10s : ' % (str(n) + ' 번째'), pi)
        elif n == 5:
            print('-'* 20, '중   략', '-' * 20)
getPi(100000)
