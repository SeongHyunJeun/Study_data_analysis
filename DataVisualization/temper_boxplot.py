import csv

import matplotlib.pyplot as plt
import numpy as np


"""
위치값을 알고싶을 때
result = np.array(result)
print("1/4: " +str(np.percentile(result,25)))      # 1/4 위치의 값
print("2/4: " +str(np.percentile(result,50)))      # 2/4 위치의 값
print("3/4: " +str(np.percentile(result,75)))      # 3/4 위치의 값
"""

f = open('seoul.csv')
data = csv.reader(f)
next(data)
month = [[], [], [], [], [], [], [], [], [], [], [], []]



for row in data :
    if row[-1] != '' and row[-2] !='':
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))

plt.style.use('ggplot')  #그래프 스타일 지정
plt.figure(figsize=(10,5), dpi=200)    #그래프 크기 수정
plt.boxplot(month, showfliers=False)       #아웃라이어 값(이상치) 생략
#plt.boxplot(month)

plt.show()

