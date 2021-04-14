import pandas as pd
import argparse
import matplotlib.pyplot as plt

df = pd.read_csv('owid-covid-data-2020-monthly.csv')
cols = list(df.columns.values)
df = df[[cols[0]] + cols[2:4] + [cols[4]]]
df = df.groupby(cols[0]).sum().reset_index()
df['case_fatality_rate'] = df['total_deaths']/df['total_cases']
nc = df['new_cases']
cfr = df['case_fatality_rate']
plt.xlabel('New Cases by Location in 2020')
plt.ylabel('Case Fatalitly Rate')
scatter_a = plt.scatter(nc, cfr)
plt.savefig('scatter_a.png')
plt.xscale('log')
scatter_b = plt.scatter(nc,cfr)
plt.savefig('scatter_b.png')