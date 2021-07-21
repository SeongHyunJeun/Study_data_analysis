import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)

size = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data:
    if name in row[0]:
        m = 0
        f = 0
        for i in range(101) :
            m += int(row[i+3])
            f += int(row[i+106])
        break

size.append(m)
size.append(f)

plt.rc('font', family='Malgun Gothic')       #한글 사용시 깨질때
label = ['남자','여자']
color = ['crimson', 'darkcyan']
plt.axis('equal')  #동그란 원

plt.pie(size, labels = label, autopct='%.1f%%', colors=color, startangle=90)   #autopct = auto percent
plt.title(name+' 지역의 남녀 성별 비율')
plt.legend()
plt.show()