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

# 2020-01-01 ~ 2020-12-31
kor_sr = get_data('../ch05/data/covid_kor.csv')
kor_index = kor_sr.index

# 2020-03-01 ~ 2021-12-31
hi_sr = get_data('./hi_data.csv')
hi_index = hi_sr.index

# -> 2020-01-01 ~ 2021-12-31
data_index = kor_index.union(hi_index)

#인구비율구하기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
rate = 20.13

df = pd.DataFrame(
    {
        '대한민국': kor_sr,
        '하와이': hi_sr * rate,
    },
    index=data_index
)
df.plot.line()
plt.show()
