
a = 1
while(a==1):
    num = input('숫자를 입력해주세요 : ')
    try:
        if int(num)  == 0:
            print(num + "은 0입니다.")
        elif int(num)%2 == 0:
            print(num + "은 짝수입니다.")
        elif int(num)%2 == 1:
            print(num+"은 홀수입니다.")
    except:
        if type(num) != int:
             print('숫자만 입력이 가능합니다.')
