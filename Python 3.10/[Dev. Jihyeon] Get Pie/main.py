import math

n = 5                 # 5각형 부터 시작
while True:
    degree = 360 / n    # n각형의 내각
    theta = degree / 2  # 내각의 절반이 삼각함수의 기준 각도(A)
    inner_length = math.sin(math.radians(theta)) * 2        # 내접하는 변의 길이 sin A * 2
    outer_length = math.tan(math.radians(theta)) * 2        # 외접하는 변의 길이 tan A * 2
    difference = outer_length - inner_length                # 내접하는 변과 외접하는 변의 길이 차이
    new_pi = n * ((outer_length + inner_length) / 2) / 2    # 중간 값으로 원주율 계산

    # n값 증가에 따른 원주율 값, 오차 변화
    print(n, " 각형  |  파이: ", new_pi)
    n = n + 1           # 다각형의 변의 개수를 늘리기
0.3894020056186793, 0.6263597563213175