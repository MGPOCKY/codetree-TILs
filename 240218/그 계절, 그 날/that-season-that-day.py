Y, M, D = list(map(int, input().split()))

isLeapYear = Y % 4 == 0
if Y % 100 == 0 and Y % 400 != 0:
    isLeapYear = False

date = [
    31,
    29 if isLeapYear == True else 28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
    ]
if date[M - 1] >= D:
    season = ''
    if M >= 3 and M <= 5:
        season = 'Spring'
    elif M >= 6 and M <= 8:
        season = 'Summer'
    elif M >= 9 and M <= 11:
        season = 'Fall'
    else:
        season = 'Winter'
    print(season)
else:
    print(-1)