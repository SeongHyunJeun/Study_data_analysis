import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []
low = []

for row in data :
    if int(row[0].split('-')[0]) >=1980  :
        if row[0].split('-')[1] == '08' and row[0].split('-')[2] == '30':
            if row[-1] != '' and row[-2] != '':
                high.append(float(row[-1]))
                low.append(float(row[-2]))


plt.rc('font', family='Malgun Gothic')         #맑은 고딕을 기본 글꼴로 설정
plt.rcParams['axes.unicode_minus'] = False   #마이너스 기호 깨짐 방지
#  plt.figure(figsize= (10, 2))                그래프 크기조절, 맨 앞에.
plt.title("내 생일의 기온 변화 그래프")
plt.plot(high, 'r', label="최고기온")
plt.plot(low, 'g', label="최저기온")
plt.legend()
plt.show()

plt.show()