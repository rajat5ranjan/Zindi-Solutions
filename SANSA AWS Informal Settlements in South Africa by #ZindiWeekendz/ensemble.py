import pandas as pd
import numpy as np
from scipy.stats import rankdata

# Make sure max probablity is 1

#RUN 1
#submission_kf0.47.ipynb
kv1=pd.read_csv('Zindi_sub_20_kf10.csv')
#RUN 2
#submission_kf0.4667.ipynb
kv2=pd.read_csv('Zindi_sub_22_kf10.csv')
kv1['Label']=kv1['Label']*0.3+kv2['Label']*0.7

kv1.to_csv('ensemble_1.csv',index=False) #0.461481443181872

#RUN 3
#Sub_kf0.447_resnet18.ipynb
kv1=pd.read_csv('Sub_kf0.447_resnet18.csv')
kv2=pd.read_csv('ensemble_1.csv')
kv1['Label']=kv1['Label']*0.7+kv2['Label']*0.3

print(kv1.shape)
kv1.to_csv('447_ensemble_1.csv',index=False) #0.443360297881889


#RUN 4
#Sub_kf10_dense_bs16_3lac.ipynb
kv1=pd.read_csv('Sub_kf10_dense_bs16_3lac.csv') #0.506526666372627
kv2=pd.read_csv('447_ensemble_1.csv') #0.443360297881889
#RUN 5
#Sub_resnet18_4Lac.ipynb
kv3=pd.read_csv('Sub_resnet18_4Lac.csv') #0.506362593355399
kv1['Label']=kv1['Label']*0.15+kv2['Label']*0.7+kv3['Label']*0.15
print(kv1.shape)
kv1.to_csv('447ensemble_res184lac_dense3lac.csv',index=False) #0.446524669571776

#leak-------get ipynb file
kv2=pd.read_csv('447_ensemble_1.csv') #0.443360297881889
kv3=pd.read_csv('leak.csv') #0.589179530943973
kv1=pd.read_csv('447ensemble_res184lac_dense3lac.csv') #0.446524669571776

kv2['Label']=kv2['Label']*0.6+kv3['Label']*0.05+kv1['Label']*0.4
print(kv2.describe())
kv2.to_csv('leak_ensemble_best.csv',index=False) #0.430574450073715


kv2=pd.read_csv('447_ensemble_1.csv') #0.443360297881889
kv3=pd.read_csv('leak.csv') #0.589179530943973
kv1=pd.read_csv('leak_ensemble_best.csv') #0.430574450073715
kv4=pd.read_csv('submission_skf0.4667_res18_bs16_4lac.csv') #0.475065208071544


kv2['Label']=kv2['Label']*0.25+kv3['Label']*0.05+kv1['Label']*0.7+kv4['Label']*0.05
print(kv2.describe())
kv2.to_csv('leak_ensemble_best_1.csv',index=False) #0.424303721145037



kv2=pd.read_csv('447_ensemble_1.csv') #0.443360297881889
kv3=pd.read_csv('leak.csv') #0.589179530943973
kv1=pd.read_csv('leak_ensemble_best.csv') #0.430574450073715
kv4=pd.read_csv('leak_ensemble_best_1.csv') #0.424303721145037


kv2['Label']=kv2['Label']*0.1+kv3['Label']*0.05+kv1['Label']*0.2+kv4['Label']*0.66
print(kv2.describe())
kv2.to_csv('ensemble_new_last.csv',index=False) #0.422227579430734


#kv1=pd.read_csv('ensemble_new_last.csv') #0.422227579430734
#kv2=pd.read_csv('leak_ensemble_best_1.csv') #0.424303721145037
#kv3=pd.read_csv('Best_resnet18_skf.csv') #0.505927681127314
#
#kv2['Label']=kv2['Label']*0.52+kv3['Label']*0.4+kv3['Label']*0.1
#print(kv2.describe())
#kv2.to_csv('ensemble_3level_best.csv',index=False) #0.422922620541361
