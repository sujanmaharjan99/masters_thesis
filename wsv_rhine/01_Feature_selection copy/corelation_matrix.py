import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

directory_list = [os.path.join('..', 'Inputs_outputs_excels', 'rate_of_change_df.xlsx')]

# Load the DataFrame
df = pd.read_excel('C:/Projects/WSV/kisters.water.rto_ipopt/Visualizations/Excels/df_pseudo.xlsx')

# Specify original column names for x and y axes
columns_for_x_axis = [
    'Rate of change ANDER/flow.bc',
    'Rate of change BONN/flow.obs',
    'Rate of change KOELN/flow.obs',
    'Rate of change DUESS/flow.obs',
    'Rate of change DUISB/flow.obs',
    'Rate of change WESEL/flow.obs',
    'Rate of change REES/flow.obs',
    'Rate of change EMMER/flow.obs'
]

# The y-axis should include both the renamed and original columns
columns_for_y_axis = columns_for_x_axis + [
    'BONN/flow.bc',
    'KOELN/flow.bc',
    'DUESS/flow.bc',
    'DUISB/flow.bc',
    'WESEL/flow.bc',
    'REES/flow.bc',
    'EMMER/flow.bc'
]

# Mapping dictionary for renaming the axes
rename_mapping_x = {
    'Rate of change ANDER/flow.bc': 'Rate of change Andernach',
    'Rate of change BONN/flow.obs': 'Rate of change Bonn',
    'Rate of change KOELN/flow.obs': 'Rate of change Köln',
    'Rate of change DUESS/flow.obs': 'Rate of change Düsseldorf',
    'Rate of change DUISB/flow.obs': 'Rate of change Duisburg',
    'Rate of change WESEL/flow.obs': 'Rate of change Wesel',
    'Rate of change REES/flow.obs': 'Rate of change Rees',
    'Rate of change EMMER/flow.obs': 'Rate of change Emmerich'
}

rename_mapping_y = {
    'BONN/flow.bc': 'Bonn MBC',
    'KOELN/flow.bc': 'Köln MBC',
    'DUESS/flow.bc': 'Düsseldorf MBC',
    'DUISB/flow.bc': 'Duisburg MBC',
    'WESEL/flow.bc': 'Wesel MBC',
    'REES/flow.bc': 'Rees MBC',
    'EMMER/flow.bc': 'Emmerich MBC'
}

# Renaming the DataFrame columns for both axes
df_renamed = df.rename(columns={**rename_mapping_x, **rename_mapping_y})

# The y-axis should include both the renamed columns and original flow.bc columns
y_axis_labels = list(rename_mapping_x.values()) + list(rename_mapping_y.values())

# Compute the correlation matrix using the renamed columns
correlation_matrix = df_renamed[y_axis_labels].corr()

# Slice the correlation matrix for the x-axis with renamed columns and y-axis with both renamed and original columns
correlation_slice = correlation_matrix.loc[y_axis_labels, rename_mapping_x.values()]

# Create a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_slice, annot=True, cmap='coolwarm_r', center=0)

plt.xticks(rotation=45, ha='right')
plt.title('Correlation Heatmap')
plt.show()
