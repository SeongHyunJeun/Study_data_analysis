import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)

m = []
w = []

for row in data :
    if '장수서창동' in row[0] :
        for i in range(0, 101) :
            m.append(-int(row[3+i]))
            w.append(int(row[-(i+1)]))

w.reverse()

plt.rc('font', family='Malgun Gothic')       #한글 사용시 깨질때
plt.rcParams['axes.unicode_minus'] = False   #마이너스가 깨질때
plt.style.use('ggplot')

plt.barh(range(101), m, label='남성')
plt.barh(range(101), w, label='여성')
plt.legend()
plt.show()
