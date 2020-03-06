import datetime as dt
def string_formatting():
    ls = [2019, 9, 20, 12, 30, 20]
    date = dt.datetime(*ls)
    print(date)
    print('year is {0:%Y} month is {0:%B} day is {0:%d}'.format(date))

    dict = {'a':1,'b':2}

    for i ,j in dict.items():
        print(i,j)
if __name__ == '__main__':
    string_formatting()
