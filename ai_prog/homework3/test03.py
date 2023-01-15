'''
    피타고라스의 정리를 만족하는 삼각형들을 모두 찾아보자. 삼각형 한 변의 길이는 1
    부터 30 이하이다.

                x**2+y**2==z**2
    
    [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26),
    (12, 16, 20), (15, 20, 25), (20, 21, 29)]
'''


def getTri():
    resultList = []
    for x in range(1,31):
        for y in range(1, 31):
            for z in range(1, 31):
                if z**2 == x**2 + y**2:
                    resultList.append((x, y, z))
    return resultList

result = getTri()
print(result)