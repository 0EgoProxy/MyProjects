import pandas as pd

frame = pd.read_csv('dataset.tsv', header=0, sep='\t')

"""
    Если нам нужна фильтрация. Например будем фильтровать по дате рождения из таблицы.
"""
frame.Birth = frame.Birth.apply(pd.to_datetime)
frame.fillna('разнорабочий', inplace=True)
# print(frame[frame.Birth >= pd.datetime(1985, 1, 1)])

""" Несколько условий и их пересечение. ( все условия логические) """
# print(frame[(frame.Birth >= pd.datetime(1985, 1, 1)) & (frame.City != 'Москва')])   # '&' = 'и' используем знаки... а не
#                                                                                   # привычное нам 'and' -'пересечение'
''' Теперь попробуем обьединение условий - 'or' '''
# print(frame[(frame.Birth >= pd.datetime(1985, 1, 1)) | (frame.City == 'Волгоград')])
