import csv
import matplotlib.pyplot as plt

"""
plt.title('legend')
plt.plot([10, 20 , 30, 40],color='r', linestyle='--', label='asc')  #linestyle == ls
plt.plot([40,30,20,10], 'g:', label='desc')
plt.legend()
plt.show()

"""

plt.title('marker')
plt.plot([10,20,30,40], 'r.', label='circle')
plt.plot([40,30,20,10], 'g^-', label='triangle up')       ###  <색상><마커모양><선모양> 순으로 동시 설정가능
plt.legend()
plt.show()