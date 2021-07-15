import csv

max_temp = 30
max_date = ''

f = open('seoul.csv')
data = csv.reader(f)        #pandas 이용시 pd.read_csv('파일명.csv')
header = next(data)

for row in data:
    if (row[-1] == ''):
        row[-1] = -999

    row[-1] = float(row[-1])

    if (row[-1] > max_temp):
        max_temp = row[-1]
        max_date = row[0]

f.close()

print('서울의 가장 더웠던 날은', max_date, '일, ', max_temp, '도 입니다.')
