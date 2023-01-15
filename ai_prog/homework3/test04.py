'''
    0과 1미만 사이의 실수를 돌려주는 함수 random.random() 있다. 
    이 함수를 이용하여 coin 함수를 만들었다.
    
    import random
    def coin():
        if random.random() < 0.5:
            return 1 # head
        return 0 # tail
    
     위 함수를 이용하여 동전을 n번 던졌을때 헤드가 나오는 평균값을 구하는 함수를 작성하고, 
    100번, 1000번, 10000번 던졌을 때 나오는 평균값을 출력하는 
    코드를 작성하세요.
'''

import random

def coin():
    if random.random() < 0.5:
        return 1    # 앞면
    return 0        # 뒷면

def getMean(n):
    sum = 0
    for i in range(n):
        sum = sum + coin()
    return sum / (n + 1)

print('100 번 던졌을 때 확율 :', getMean(100))
print('1000 번 던졌을 때 확율 :', getMean(1000))
print('10000 번 던졌을 때 확율 :', getMean(10000))