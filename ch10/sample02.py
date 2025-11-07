import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib

init_matplotlib()

#전달받은 파일명에 해당하는 Data리턴 함수
def get_data(filename):
    df_raw = pd.read_csv(filename)
    df_raw.set_index('date', inplace=True)

    return df_raw['total_cases']
#end-def

#kor_sr = get_data('../ch05/data/covid_kor.csv')
hi_sr = get_data('./hi_data.csv')

'''
index_data = kor_data.index
df = pd.DataFrame(
    {
        '대한민국': kor_data,
        '미국': usa_data,
    },
    index=index_data
)
df.plot.line()
plt.show()
'''