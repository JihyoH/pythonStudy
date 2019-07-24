# input() 함수!!
# keyboard = input()
# print(keyboard)

# 홀짝
# a="q"
# while(a!="a"):
#     aaa = input("얼마 넣을래?")
#     try:
#         if int(aaa) % 2 == 0:
#             print(aaa+"는 짝수")
#         else:
#             print(aaa+"는 홀수")
#     except:
#         print("숫자만 넣으란 말야!!")
#     a = input("a는 뭐할래")



# 변수(veriable)는 처리할 데이터를 저장시키는 기억장소를 말한다.
# 변수명 작성방법
# 영문자, 숫자, 특수문자(_)만 사용할 수 있으며 대문자와 소문자를 구별한다.
# 반드시 문자로 시작해야 하고 파이썬의 예약어는 사용할 수 없다.

# 변수를 선언할 때는 c, java 언어와 달리 변수의 자료형을 지정하지 않으며 입력
# 되는 데이터의 타입에 따라 자동으로 변수의 타입이 결정된다.

# '='은 같다라는 의미로 사용되지 않고 '=' 오른쪽의 데이터를 '=' 왼쪽의 기억장소
# 에 저장시키라는 의미로 사용된다. => '=='를 사용해야 같다로 인식된다.
name = '홍길동'
print(type(name))
age = 20
print(type(age))
height = 175.5
print(type(height))
gender = True
print(type(gender))
none = None # 빈 변수를 만든다.
print(type(none))
# 변수를 삭제하려면 del 명령을 사용한다.
# del name
# print(type(name))
print('*' * 50)

'''
# 1줄 주석은 '#'으로 하지만 여러줄 주석은 작은따옴표 3개 사이에 쓰면 된다.
print('이름을 입력하세요 : ', end = '')
name = input()
print('%s님 안녕하세요' % name)
print('*' * 50)

# input() 함수는 데이터를 무조건 문자열로 입력받는다.
name = input('이름을 입력하세요 : ')
# 문자열로 입력받은 데이터는 int() 또는 float() 함수를 사용해 숫자로 변환한다.
age = int(input('나이를 입력하세요 : '))
print('{}님은 올해 {}살 입니다.'.format(name, age))
print('{}님은 내년에 {}살 입니다.'.format(name, age + 1))
print('*' * 50)

# split(구분자) : 문자열을 구분자를 경계로 분리한다. 나눈다. 쪼갠다.
name, age = input('이름과 나이를 입력하세요 : ').split(' ')
print('{}님은 올해 {}살 입니다.'.format(name, age))
print('{}님은 내년에 {}살 입니다.'.format(name, int(age) + 1))
print('*' * 50)
'''

# map() 함수를 사용해서 입력받은 데이터를 일괄적으로 숫자로 변환시킬 수 있다.
python, java, spring = map(int, input('3과목 점수를 입력하세요 : ').split(' '))
# age + 1과 같이 변수에 저장된 문자열과 상수를 덧셈하면 에러가 발생되지만
# python + java + spring와 같이 변수에 저장된 문자열을 덧셈하면 문자열끼리
# 연결시킨다.
print('총점 : {}'.format(python + java + spring))














