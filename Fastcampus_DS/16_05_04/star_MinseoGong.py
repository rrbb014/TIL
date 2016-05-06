# 패캠 파이썬 강의 day1 5월4일
# 자료형, 제어문, 입출력, 함수



def star_1(count):
    """정방향 좌측정렬 별 찍는 함수"""
    result = "1. 저는 별찍기 정방향 좌측정렬된 별을 찍는 함수입니다. \n"
    for i in range(count):
        result += ("*" * (i + 1))+"\n"
    result += "\n"
    return result


def star_2(count):
    """정방향 우측정렬 별 찍는 함수"""
    result = "2. 저는 별찍기 정방향 우측정렬된 별을 찍는 함수입니다. \n"
    array = range(count)
    length = len(array)
    for i in array:
        result +=" " * (length - (i + 1)) + "*" * (i + 1) + "\n"
    result += "\n"
    return result

def star_3(count):
    """역방 좌측정렬 별 찍는 함수"""
    result = "3. 저는 역방향 좌측정렬된 별을 찍는 함수입니다. \n"
    loo = range(count)
    for i in loo:
        result += "*" * (len(loo) - i) + "\n"
    result += "\n"
    return result

def another_star_3(count):
    """역방 좌측정렬 별 찍는 함수 ver.3 """
    result = "3-1. 저는 역방향 좌측정렬된 별을 찍는 함수의 2번째 버젼입니다. \n"
    for i in range(count):
        for j in range(count, 0, -1):
            if i < j:
                result += "*"
            else:
                result += " "
        result += "\n"
    result += "\n"
    return result

def star_4(count):
    """역방향 우측정렬 별 찍는 함수"""
    result = "4. 저는 역방향 우측정렬된 별을 찍는 함수입니다. \n"
    loo = range(count)
    length = len(loo)
    for i in loo:
        result += " " * i + "*" * (length - i) +"\n"
    result += "\n"
    return result

def call_homeworks(count):
    final_result="나는 숙제다. \n\n===========시작============== \n\n"
    final_result += star_1(count) + star_2(count) + star_3(count) + another_star_3(count) + star_4(count)
    return final_result


report = call_homeworks(int(input("stars?")))
with open("05_04_star_homework.txt", "w") as f:
    f.write(report)
