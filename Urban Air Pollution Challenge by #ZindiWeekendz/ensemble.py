import pandas as pd
import numpy as np
from scipy.stats import rankdata

kv1=pd.read_csv('colab_cbfolds5_try6.csv') #30.50
kv2=pd.read_csv('zindi_colab_try2_lgbm2.csv') #30.53
kv3=pd.read_csv('zindi_colab_trylgbm12.csv') #30.45
kv4=pd.read_csv('cb_6_lgbm_12_lgbm2_2.csv') #30.31
kv5=pd.read_csv('cb_6_lgbm_12_lgbm2_2_try2.csv') #30.31


#kv1['target']=(kv1['target']+kv2['target']+kv3['target'])/3
#kv1.to_csv('cb_6_lgbm_12_lgbm2_2.csv',index=False) //30.31


#kv1['target']=kv1['target']*0.3+kv2['target']*0.2+kv3['target']*0.5
#kv1.to_csv('cb_6_lgbm_12_lgbm2_2_try2.csv',index=False)

kv4['target']=kv4['target']*0.5+kv5['target']*0.5
kv4.to_csv('cb_6_lgbm_12_lgbm2_2_try3.csv',index=False) #30.31
