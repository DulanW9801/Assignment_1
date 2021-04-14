import pandas as pd
import argparse
from datetime import date
df = pd.read_csv('owid-covid-data.csv')
cols = list(df.columns.values)
df = df[ cols[2:6] + cols[7:9]]
df['date'] = pd.to_datetime(df['date'], dayfirst = True)
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
new_df = df[df['year'] == 2020]
new_cols = list(new_df.columns.values)
new_df = new_df[ [new_cols[0]] + [new_cols[-1]] + new_cols[2:6]+ [new_cols[1]]]
grpd_df = new_df.groupby(['location', 'month']).sum().reset_index()
grpd_df['case_fatality_rate'] = (grpd_df['total_deaths']/grpd_df['total_cases'])
final_df = grpd_df.sort_values(['location','month'], ascending = True)
final_df.to_csv('owid-covid-data-2020-monthly.csv', index = False)
print(final_df.head(5))
