import plotly.express as pe
import pandas as pd
df = pd.read_csv('Copy+of+data+-+data.csv')
fig = pe.scatter(df, x = 'date', y = 'cases', color = 'country', title = 'Covid cases in countries')
fig.show()