def score(n):
    """根据成绩，计算成绩的级别，级别有：A、B、C、D
    成绩>=90  ——A
    成绩>=80  ——B
    成绩>=70  ——C
    成绩>=60  ——D

    参数：
    - n-：成绩
    返回值：返回‘A’或‘B’或者'C'或者'D'
    """

    if n >= 90:
        return 'A'
    if n >= 80:
        return 'B'
    if n >= 70:
        return 'C'
    if n >= 60:
        return 'D'


if __name__ == '__main__':
    print(score(75))  # C
    print(score(85))  # B
    print(score(80))  # B
