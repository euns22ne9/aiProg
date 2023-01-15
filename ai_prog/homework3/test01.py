'''
    1960년대에 Frank Drake가 인간과 교신할 수 있는 지적인 외계 문명(생명체)의 수 N
    을 추정하는 Drake 방정식을 만들었다.
        N = R * p * n * f * i * c * L, 여기서
            R: 우리 은하 안에서 1년동안 탄생하는 항성의 수 ( 7로 가정)
            p: 항성이 행성을 갖고 있을 비율(percent)
            n: 행성들 중에서 생명체가 살 수 있는 조건을 갖춘 행성의 수
            f: 조건을 갖춘 행성에서 실제로 생명체가 탄생할 행성의 비율(percent)
            i: 탄생한 생명체가 지적 생명체로 진화할 비율(percent)
            c: 지적 생명체가 외부와 교신할 기술을 갖고 있을 비율(percent)
            L: 통신 기술을 가진 생명체가 존속할 수 있는 기간(단위: 년)
            
    위 입력을 받아서 N 값을 구하는 코드를 작성하세요.
'''
def getDrake(R = 10, p = 0.5 , n = 2, f = 1, i = 0.01, c = 0.01, L = 10000):
    # 드레이크가 1961년 사용한 값으로 초기값 셋팅
    return R * p * n * f * i * c * L


def input_calc_drake():
    print('* 질문의 값을 입력하세요!', end='\n\n')
    R = int(input('우리 은하 안에서 1년동안 탄생하는 항성의 수 (R = 7)\n: '))
    p = float(input('항성이 행성을 갖고 있을 확룰 (p = 0.5)\n: '))
    n = int(input('행성들 중에서 생명체가 살 수 있는 조건을 갖춘 행성의 수 (n = 2)\n: '))
    f = float(input('조건을 갖춘 행성에서 실제로 생명체가 탄생할 행성의 비율 (f = 1)\n: '))
    i = float(input('탄생한 생명체가 외부와 교신할 기술을 갖고 있을 비율 (i = 0.01)\n: '))
    c = float(input('지적 생명체가 외부와 교신할 기술을 갖고 있을 비율 (c = 0.01)\n: '))
    L = int(input('통신 기술을 가진 생명체가 존속할 수 있는 기간 (L=10000)\n: '))
    count = getDrake(R, p, n, f, i, c, L)
    print('=' * 60)
    print('### 입력받은 값을 사용한 방정식 결과 :', count, '###')
    print('=' * 60)

while True:
    print('=' * 60)
    code = input('%-30s : d\n%-30s : i\n%-32s : q\n%-45s\n%-30s : ' % ('Drake 가 사용한 값의 결과', '입력한 값으로 계산', '프로그램 종 료',('-' * 45), '코드를 입력하세요.'))
    print('=' * 60)
    if code == 'd':
        count = getDrake()
        print('*' * 60)
        print('********** 1961년 Drake 가 사용한 값 결과 : ', count, '**********')
        print('*' * 60)
    elif code == 'i' :
        input_calc_drake()
    elif code == 'q':
        print('### 프로그램을 종료합니다. ###')
        print('=' * 60)
        break
    else :
        print('# 잘못된 코드입니다. 다시 입력하세요! #')


