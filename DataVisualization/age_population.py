import csv
import matplotlib.pyplot as plt

f = open("age.csv")
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

for row in data :
    if name in row[0] :
        for i in row[3:] :
            result.append(int(i.replace(',','')))

plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')


plt.title(name + ' 지역의 인구 구조')

# plt.plot(result)
#plt.barh(range(101),result)       수평방향 막대그래프
plt.bar(range(101),result)
plt.show()
