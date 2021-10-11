#imports
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

#means
data_df = pd.read_csv('data.csv')
level_df = data_df.groupby('level')
level_mn = data_df.groupby(['student_id','level'], as_index=False)['attempt'].mean()
print(level_mn)
level_mn.info()


#plots
scatter = px.scatter(level_mn, x='student_id', y='level', color='attempt', size = 'attempt')
scatter.show()