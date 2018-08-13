import talib
import pandas as pd
import time
import numpy as np

class demo:

    def __init__(self):
        self.h5_path = 'F:/data/stock_data_py'
    def 加载数据(self,name,var):
        print('加载数据'+self.h5_path+'/'+var+'/'+name)
        df = pd.read_hdf(self.h5_path+'/'+var+'/'+name+'.h5')
        return df
    def demo_run(self,strategy_name):
        t = time.time()
        stocklist=self.加载数据('stocklist','list')
        stocklist['codenum'] = stocklist['code'].apply(lambda x:x[:6])
        closef_pd=self.加载数据('closef_pd','day')
        openf_pd=self.加载数据('openf_pd','day')
        highf_pd = self.加载数据('highf_pd','day')
        lowf_pd = self.加载数据('lowf_pd','day')
        amt_pd=self.加载数据('amt_pd','day')

        def MACD():
            t=time.time()
            print('MACD run')
            p=(12,26,9)
            def get_macd(x):
                print('MACD run')
                # DIF, DEA, MACD = talib.MACD(closef_pd,p[0],p[1],p[2])
                return 12

        ind = eval(strategy_name + '()')




if __name__=='__main__':
    self=demo()
    listMACD=self.demo_run(strategy_name='MACD')

