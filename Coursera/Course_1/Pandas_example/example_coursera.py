"""# Библиотека PANDAS #"""
"""
    Data frame
"""

import pandas as pd

# frame = pd.DataFrame({'Numbers': range(10),
#                       'Name': ['Maksim', 'Leonid',
#                                 'Natasha', 'Andrey',
#                                 'Aleftina', 'Albina',
#                                 'Aleksandr', 'Maria',
#                                 "Ivan", 'Leva']})
#
# print(frame)

frame = pd.read_csv('Teoria_txt', header=0, sep=',')
print(frame)
# print(frame.columns)


new_line = {'first_name': 'fuck',
            'last_name': 'you',
            'modul1': 120,
            'modul2': 120,
            'modul3': 120}

"""Игнор индекс - не так важно под каким номером добавиться наша строчка."""
""" 
методо append в pandas не изменяет таблицу, метод вносит изменения для отображения, и возвращает таблицу
до изменений.
"""
# print(frame.append(new_line, ignore_index=True))
# print(frame)

'''Следовательно нужно изменить саму переменную frame) '''
frame = frame.append(new_line, ignore_index=True)
print(frame)

''' Добавление нового столбца можно сравнить с диктом. '''
frame['New_tabl'] = ['YES']*2 + ['NO']
print(frame)

''' удаление столбоц '''
frame = frame.drop([2], axis=0)
print(frame)

frame.to_csv('update_dataset_Teoria', sep='\t', header=True, index=None)