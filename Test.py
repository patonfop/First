from datetime import datetime, timedelta


def work_time(date_start,  date_end, days_work, days_skip):
    start = datetime.strptime(date_start, "%Y-%m-%d")
    end = datetime.strptime(date_end, "%Y-%m-%d")
    delta = end - start # Кількість днів в графіку роботи
    graphik = []
    if days_work >0:
        for i in range(0, delta.days, days_skip+1):
            graphik.append(str(start.date() + timedelta(days=i)))
    print(graphik)
    return graphik







work_time('2022-04-20', '2022-04-23', 1, 1)
work_time('2022-04-25', '2022-06-26', 0, 4)
work_time('2022-05-14', '2022-05-24', 1, 95)

"""[2022-04-20, 2022-04-23, 1, 1]  -->  [2022-04-20, 2022-04-22]
[2022-04-25, 2022-06-26, 0, 4]  -->  []
[2022-05-14, 2022-05-24, 1, 95] -->   [2022-05-14]
"""
