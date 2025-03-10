import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np

students = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Попов', 'Смирнов', 'Васильев', 'Михайлов', 'Новиков', 'Федоров']
subjects = ['Информатика', 'Математика', 'Физика', 'Химия', 'История']
data = {'Студент': students}
for subject in subjects:
    data[subject] = [random.choices([2, 3, 4, 5], k=random.randint(1, 10)) for _ in range(len(students))]

df = pd.DataFrame(data)
#print(df)
#print(df.head())
#print(df.loc[0])
summa = 0
length = 0
total_summa = [0,0,0,0,0]
total_length = [0,0,0,0,0]
with open('result.txt', 'w', encoding='utf-8') as f:
    for i in range(len(students)):
        for j in range(len(subjects)):
            summa += np.sum(df.loc[i][subjects[j]])
            length += len(df.loc[i][subjects[j]])
            total_summa[j] += summa
            total_length[j] += length
            print(f'{df.loc[i]["Студент"]} {subjects[j]} {np.round(summa/length,2)}') #  {summa} {length} {summa/length}')
            f.write(f'{df.loc[i]["Студент"]} {subjects[j]} {np.round(summa/length,2)}\n')
            summa = 0
            length = 0
    for i in range(len(subjects)):
        print(f'Общая средняя оценка по предмету {subjects[i]}: {np.round(total_summa[i]/total_length[i],2)}')
        f.write(f'Общая средняя оценка по предмету {subjects[i]}: {np.round(total_summa[i]/total_length[i],2)}\n')

    all_results = [0,0,0,0,0]
    for i in range(len(subjects)): #df[subjects[i]] = print(df[subjects[i]].apply(lambda x: np.mean(x)))
        all_results[i] = [item for sublist in df[subjects[i]] for item in sublist]#преобразование в одномерный список

        #all_results[i] = sorted(all_results[i])
        #print(all_results[i])
    for i in range(len(subjects)):
        df1 = pd.Series(all_results[i])
        print(f'{subjects[i]}: медиана {df1.median()}')
        f.write(f'{subjects[i]}: медиана {df1.median()}\n')

    math_q1 = np.quantile(pd.Series(all_results[1]), 0.25)
    math_q3 = np.quantile(pd.Series(all_results[1]), 0.75)
    print(f'1-квартиль по математике: {math_q1}, 3-квартиль по математике: {math_q3}')
    f.write(f'1-квартиль по математике: {math_q1}, 3-квартиль по математике: {math_q3}\n')
    math_iqr = math_q3 - math_q1
    print(f'Интерквартильный размах по математике: {math_iqr}')
    f.write(f'Интерквартильный размах по математике: {math_iqr}\n')
    std_math = np.std(pd.Series(all_results[1]))
    print(f'Среднеквадратичное отклонение по математике: {std_math}')
    f.write(f'Среднеквадратичное отклонение по математике: {std_math}\n')

