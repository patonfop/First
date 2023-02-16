from datetime import datetime, timedelta

def work_time(date_start,  date_end, days_work, days_skip):
    start = datetime.strptime(date_start, "%Y-%m-%d")
    end = datetime.strptime(date_end, "%Y-%m-%d")
    delta = end - start # Кількість днів в графіку роботи
    graphik = []
    for i in range(0, delta.days, days_skip+days_work):
        for b in range(days_work):
            graphik.append(str(start.date() + timedelta(days=i+b)))
            if graphik[-1] == str(end.date()):
                break

    return graphik


try:
    start_in = input('Введіть дату початку розкладу (у форматі YYYY-MM-DD) : ')
    end_in = input('Введіть дату закінчення розкладу (у форматі YYYY-MM-DD): ')
    work_day_in = int(input('Введіть к-сть робочих днів: '))
    skip_day_in = int(input('Введіть к-сть вихідих днів: '))

    print(work_time(start_in, end_in, work_day_in, skip_day_in))
except AttributeError:
    print( 'Ви допустились помилки')
except ValueError:
    print('Дані введено в невірному форматі')




#work_time('2022-04-20', '2022-05-23', 5, 6)
#work_time('2022-04-20', '2022-05-05', 5, 0)

#work_time('2022-04-20', '2022-04-23', 1, 1)
#work_time('2022-04-25', '2022-06-26', 0, 4)
#work_time('2022-05-14', '2022-05-24', 1, 95)

"""[2022-04-20, 2022-04-23, 1, 1]  -->  [2022-04-20, 2022-04-22]
[2022-04-25, 2022-06-26, 0, 4]  -->  []
[2022-05-14, 2022-05-24, 1, 95] -->   [2022-05-14]
"""
