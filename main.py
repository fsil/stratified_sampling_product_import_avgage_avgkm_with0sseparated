import pandas as pd
import numpy as np

# reads the file
df_main = pd.read_csv("C:\\Users\\ACER\\Desktop\\strata\\pop.csv", low_memory=False)

#delete duplicates
df = df_main.drop_duplicates(subset=['vin_or_lp'], keep='first', inplace=False)

# define n0 as the number of unique vins ("name".shape[0] function counts rows// .shape[1] counts columns)
n0 = df.shape[0]

print('Unique number of VINs is', n0)
print('Share of VHRs and ICRs:',
      df['product'].value_counts(dropna=False, normalize=True))

vhr_notimp = df[(df["product"] == "VHR") & (df["import"] == 0)]
icr_imp = df[(df["product"] == "ICR") & (df["import"] != 0)]
vhr_imp = df[(df["product"] == "VHR") & (df["import"] != 0)]
icr_notimp = df[(df["product"] == "ICR") & (df["import"] == 0)]

print('Number of VHR and not imports is', vhr_notimp.shape[0], 'and share in total VINs is', (vhr_notimp.shape[0]/n0))
print('Number of VHR and imports is', vhr_imp.shape[0], 'and share in total VINs is', (vhr_imp.shape[0]/n0))
print('Number of ICR and not imports is', icr_notimp.shape[0], 'and share in total VINs is', (icr_notimp.shape[0]/n0))
print('Number of ICR and imports is', icr_imp.shape[0], 'and share in total VINs is', (icr_imp.shape[0]/n0))

print('Average age for ICRs excluding 0Age is {}'.format(df[(df['product']=='ICR')&(df['vehicleage']!=0)]['vehicleage'].mean()))
print('Average age for VHRs excluding 0Age is {}'.format(df[(df['product']=='VHR')&(df['vehicleage']!=0)]['vehicleage'].mean()))
print('Avg mileage for ICRs excluding 0km is {}'.format(df[(df['product']=='ICR')&(df['lastodometerreading']!=0)]['lastodometerreading'].mean()))
print('Avg mileage for VHRs excluding 0km is {}'.format(df[(df['product']=='VHR')&(df['lastodometerreading']!=0)]['lastodometerreading'].mean()))

#set sample size
N = 10

#set the criteria use + count rows - "print(n1)" when you want to see how many VINS are ın each category
df_icr_import_0_0 = df[
    (df['product'] == 'ICR') & (df['import'] == 1) & (df['lastodometerreading'] == 0) & (df['vehicleage'] == 0)]
n1 = df_icr_import_0_0.shape[0]
df_icr_import_1_0 = df[
    (df['product'] == 'ICR') & (df['import'] == 1) & (df['lastodometerreading'] != 0) & (df['vehicleage'] == 0)]
n2 = df_icr_import_1_0.shape[0]
df_icr_import_0_1 = df[
    (df['product'] == 'ICR') & (df['import'] == 1) & (df['lastodometerreading'] == 0) & (df['vehicleage'] != 0)]
n3 = df_icr_import_0_1.shape[0]
df_icr_import_1_1 = df[
    (df['product'] == 'ICR') & (df['import'] == 1) & (df['lastodometerreading'] != 0) & (df['vehicleage'] != 0)]
n4 = df_icr_import_1_1.shape[0]
df_icr_notimport_0_0 = df[
    (df['product'] == 'ICR') & (df['import'] == 0) & (df['lastodometerreading'] == 0) & (df['vehicleage'] == 0)]
n5 = df_icr_notimport_0_0.shape[0]
df_icr_notimport_1_0 = df[
    (df['product'] == 'ICR') & (df['import'] == 0) & (df['lastodometerreading'] != 0) & (df['vehicleage'] == 0)]
n6 = df_icr_notimport_1_0.shape[0]
df_icr_notimport_0_1 = df[
    (df['product'] == 'ICR') & (df['import'] == 0) & (df['lastodometerreading'] == 0) & (df['vehicleage'] != 0)]
n7 = df_icr_notimport_0_1.shape[0]
df_icr_notimport_1_1 = df[
    (df['product'] == 'ICR') & (df['import'] == 0) & (df['lastodometerreading'] != 0) & (df['vehicleage'] != 0)]
n8 = df_icr_notimport_1_1.shape[0]
df_vhr_import_0_0 = df[
    (df['product'] == 'VHR') & (df['import'] == 1) & (df['lastodometerreading'] == 0) & (df['vehicleage'] == 0)]
n9 = df_vhr_import_0_0.shape[0]
df_vhr_import_1_0 = df[
    (df['product'] == 'VHR') & (df['import'] == 1) & (df['lastodometerreading'] != 0) & (df['vehicleage'] == 0)]
n10 = df_vhr_import_1_0.shape[0]
df_vhr_import_0_1 = df[
    (df['product'] == 'VHR') & (df['import'] == 1) & (df['lastodometerreading'] == 0) & (df['vehicleage'] != 0)]
n11 = df_vhr_import_0_1.shape[0]
df_vhr_import_1_1 = df[
    (df['product'] == 'VHR') & (df['import'] == 1) & (df['lastodometerreading'] != 0) & (df['vehicleage'] != 0)]
n12 = df_vhr_import_1_1.shape[0]
df_vhr_notimport_0_0 = df[
    (df['product'] == 'VHR') & (df['import'] == 0) & (df['lastodometerreading'] == 0) & (df['vehicleage'] == 0)]
n13 = df_vhr_notimport_0_0.shape[0]
df_vhr_notimport_1_0 = df[
    (df['product'] == 'VHR') & (df['import'] == 0) & (df['lastodometerreading'] != 0) & (df['vehicleage'] == 0)]
n14 = df_vhr_notimport_1_0.shape[0]
df_vhr_notimport_0_1 = df[
    (df['product'] == 'VHR') & (df['import'] == 0) & (df['lastodometerreading'] == 0) & (df['vehicleage'] != 0)]
n15 = df_vhr_notimport_0_1.shape[0]
df_vhr_notimport_1_1 = df[
    (df['product'] == 'VHR') & (df['import'] == 0) & (df['lastodometerreading'] != 0) & (df['vehicleage'] != 0)]
n16 = df_vhr_notimport_1_1.shape[0]

# based on population how many from each category should sample have / int() turns float variable into integer + round() rounds
r1 = int(round((n1/n0), 1) * N)
r2 = int(round((n2/n0), 1) * N)
r3 = int(round((n3/n0), 1) * N)
r4 = int(round((n4/n0), 1) * N)
r5 = int(round((n5/n0), 1) * N)
r6 = int(round((n6/n0), 1) * N)
r7 = int(round((n7/n0), 1) * N)
r8 = int(round((n8/n0), 1) * N)
r9 = int(round((n9/n0), 1) * N)
r10 = int(round((n10/n0), 1) * N)
r11 = int(round((n11/n0), 1) * N)
r12 = int(round((n12/n0), 1) * N)
r13 = int(round((n13/n0), 1) * N)
r14 = int(round((n14/n0), 1) * N)
r15 = int(round((n15/n0), 1) * N)
r16 = int(round((n16/n0), 1) * N)

import random

# pick samples from each category based on stratas
ra_df_icr_import_0_0 = df_icr_import_0_0.sample(r1)
ra_df_icr_import_1_0 = df_icr_import_1_0.sample(r2)
ra_df_icr_import_0_1 = df_icr_import_0_1.sample(r3)
ra_df_icr_import_1_1 = df_icr_import_1_1.sample(r4)
ra_df_icr_notimport_0_0 = df_icr_notimport_0_0.sample(r5)
ra_df_icr_notimport_1_0 = df_icr_notimport_1_0.sample(r6)
ra_df_icr_notimport_0_1 = df_icr_notimport_0_1.sample(r7)
ra_df_icr_notimport_1_1 = df_icr_notimport_1_1.sample(r8)
ra_df_vhr_import_0_0 = df_vhr_import_0_0.sample(r9)
ra_df_vhr_import_1_0 = df_vhr_import_1_0.sample(r10)
ra_df_vhr_import_0_1 = df_vhr_import_0_1.sample(r11)
ra_df_vhr_import_1_1 = df_vhr_import_1_1.sample(r12)
ra_df_vhr_notimport_0_0 = df_vhr_notimport_0_0.sample(r13)
ra_df_vhr_notimport_1_0 = df_vhr_notimport_1_0.sample(r14)
ra_df_vhr_notimport_0_1 = df_vhr_notimport_0_1.sample(r15)
ra_df_vhr_notimport_1_1 = df_vhr_notimport_1_1.sample(r16)

final = pd.DataFrame()
final = final.append([ra_df_icr_import_0_0, ra_df_icr_import_1_0, ra_df_icr_import_0_1, ra_df_icr_import_1_1,ra_df_icr_notimport_0_0, ra_df_icr_notimport_1_0, ra_df_icr_notimport_0_1, ra_df_icr_notimport_1_1, ra_df_vhr_import_0_0, ra_df_vhr_import_1_0, ra_df_vhr_import_0_1, ra_df_vhr_import_1_1, ra_df_vhr_notimport_0_0, ra_df_vhr_notimport_1_0, ra_df_vhr_notimport_0_1, ra_df_vhr_notimport_1_1])
final.to_csv(r'C:\Users\ACER\Desktop\export_dataframe.csv', index=False, header=True)
