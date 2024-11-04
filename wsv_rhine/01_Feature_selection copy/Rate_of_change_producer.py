import pandas as pd
import os


def rateofchange_column_add(df, columnname):
        rate_of_change=df[columnname].diff()
        df['Rate of change '+ columnname]=rate_of_change
        return df

attribute_list_flow_obs = ['ANDER/flow.bc',
                           'MENDE/flow.bc',
                           'OPLAD/flow.bc',
                           'NEUBR/flow.bc',
                           'RUHRW/flow.bc',
                           'SCHER/flow.bc',
                           'BONN/flow.obs',
                           'KOELN/flow.obs',
                           'DUESS/flow.obs',
                           'DUISB/flow.obs',
                           'WESEL/flow.obs',
                           'REES/flow.obs',
                           'EMMER/flow.obs']

directory_list = [
    os.path.join('..', 'Inputs_outputs_excels', 'wsv_rhine_export - segment_16_4_2024.xlsx'),
    os.path.join('..', 'Inputs_outputs_excels', 'wsv_rhine_export - balanced_16_4_2024.xlsx'),
    os.path.join('..', 'Inputs_outputs_excels', 'wsv_rhine_export - pseudo_huber_29_4_2024.xlsx')
]

length=len(attribute_list_flow_obs)

df_segment = pd.read_excel(directory_list[0])
for j in range (0,length):
    rateofchange_column_add(df_segment,attribute_list_flow_obs[j])

df_balance = pd.read_excel(directory_list[1])
for j in range (0,length):
    rateofchange_column_add(df_balance,attribute_list_flow_obs[j])

df_pseudo = pd.read_excel(directory_list[2])
for j in range (0,length):
    rateofchange_column_add(df_pseudo,attribute_list_flow_obs[j])

df_segment.to_excel('C:/Projects/WSV/kisters.water.rto_ipopt/Visualizations/Excels/df_segment.xlsx',index=False)
df_balance.to_excel('C:/Projects/WSV/kisters.water.rto_ipopt/Visualizations/Excels/df_balance.xlsx',index=False)
df_pseudo.to_excel('C:/Projects/WSV/kisters.water.rto_ipopt/Visualizations/Excels/df_pseudo.xlsx',index=False)
