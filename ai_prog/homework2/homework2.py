# 배열을 만든다.
lst = [4, 5, 7, 12, 23, 28, 34, 46, 78]

def bSearch(noList, searchNo):
    # 결과값 변수 선언 및 초기화
    result = None
    # 검색 시작 인덱스 변수 선언 및 초기화
    startIdx = 0
    # 검색 종료 인뎃스 변수 선언 및 초기화
    endIdx = len(noList) - 1
    
    # 검색 횟수 변수 선언 및 초기화
    cnt = 1
    
    print('반복 회차 : ', end='')
    # 반복 탐색
    while True :
        # 반복 회차 출력
        print('*', end='')
        
        # 중간값 변수 생성 및 초기화
        midIdx = (startIdx + endIdx) // 2

        # 조건 처리
        if startIdx > endIdx:
            # 탐색 시작 인덱스가 종료 인덱스보다 큰경우 ==> 리스트에 데이터가 없는 경우
            result = '*** 없는 데이터 입니다. ***'
            break
        elif noList[midIdx] == searchNo :
            # 데이터를 찾은 경우
            result =  midIdx
            break
        elif noList[midIdx] > searchNo:
            # 꺼낸 데이터가 찾는 데어터보다 큰 경우
            endIdx = midIdx - 1
        elif noList[midIdx] < searchNo:
            # 꺼낸 데이터가 찾는 데이터보다 작은 경우
            startIdx = midIdx + 1
        
        # 반복 회차 1 누적
        cnt = cnt + 1
        
    # 반복 회차 출력
    print(' - ', cnt)
    # 결과 값 반환
    return result

# 리스트 내용 출력
print('리스트 내용 : ', lst)
# 찾을 숫자 입력받아 변수에 기억
no = int(input('찾을 숫자 : '))
# 함수 호출해서 찾을 숫자의 위치값 탐색
result = bSearch(lst, no)

if isinstance(result, str):
    # 결과값이 문자열인 경우(result에 '*** 없는 데이터 입니다. ***' 가 입력된 경우)
    print('bSearch(lst, ' + str(no) + ') :', result)
else:
    # 결과값이 문자열이 아닌경우(정상적으로 탐색에 성공해서 인덱스를 기억하는 경우)
    print('bSearch(lst, '+ str(no) +') :', result)
    # 함수 호출 결과로 데이터 출력
    print('lst[' + str(result) + '] : ', lst[result])
