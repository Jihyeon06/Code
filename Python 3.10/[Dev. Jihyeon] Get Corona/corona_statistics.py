# pip install pandas
# pip install openpyxl
#import pandas as pd
#import warnings
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import requests
from bs4 import BeautifulSoup

"""
warnings.simplefilter("ignore")

data_pd = pd.read_excel('test.xlsx')
data_np = pd.DataFrame.to_numpy(data_pd)

for Row_i in range(2, data_np.shape[0]):
    for Column_i in range(1, data_np.shape[1]):
        print(data_np[Row_i][Column_i], end = ' ')
    print()
"""

font_path = "./NanumGothicLight.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# median(중앙값, 중간값) 함수 작성
def median(l):
  l=sorted(l)
  # median 반환하는 함수 작성
  size = len(l)
  if size % 2 == 0:
    return (l[size//2-1] + l[size//2]) / 2
  else:
    return l[size//2]

def count_digits(s:str) -> int:
    d = ""
    for i in s:
        if i.isdigit():
            d += i
    return int(d)

plt.figure("CORONA SIATISTICS", figsize=(14,6))

url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do' # 사이트 링크

response = requests.get(url) 

if response.status_code == 200:
    date_of_corona_list, corona_patient_list, corona_death_list = [], [], []
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    for i in range(2, 9):
        date_of_corona = soup.select_one(f'#content > div > div:nth-child(14) > table > thead > tr > th:nth-child({str(i)})')
        corona_patient = soup.select_one(f'#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child({str(i)})')
        corona_death = soup.select_one(f'#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child({str(i)})')
        date_of_corona_list.append(date_of_corona.get_text())
        corona_patient_list.append(count_digits(corona_patient.get_text()) / 100)
        corona_death_list.append(count_digits(corona_death.get_text()))
        
    bar_width = 0.25
    
    index = np.arange(7)

    plt.bar(date_of_corona_list, corona_patient_list, bar_width, alpha=0.4, color='red', label='확진자 수')
    plt.plot(index, corona_patient_list, alpha=0.8, color='red', linewidth=1.2, linestyle=":")
    
    plt.bar(index + 0.125, corona_death_list, bar_width, alpha=0.4, color='black', label='사망자 수')
    plt.plot(index + 0.125, corona_death_list, alpha=0.8, color='black', linewidth=1.2, linestyle=":")

    for i in range(0, 7):
      plt.text(i, corona_patient_list[i] + 1.3, f"확진자 수\n{corona_patient_list[i]} (백명)", color='red', horizontalalignment='center', verticalalignment='bottom')
      plt.text(i + 0.125, corona_death_list[i] + 1.3, f"사망자 수\n{corona_death_list[i]} (명)", color='black', horizontalalignment='center', verticalalignment='bottom')

    # x축, y축 이름 및 범례 설정
    plt.title('코로나 확진자수', fontsize=18)
    plt.gca().set_facecolor('#E6F0F8')
    plt.xlabel('WEEK', size = 13)
    plt.ylabel('NUMBER', size = 13)
    plt.legend()
    plt.savefig('./corona.png')
    plt.show()
else :
    print(response.status_code)

