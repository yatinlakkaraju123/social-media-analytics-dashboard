# Import packages
from dash import Dash, html, dash_table,dcc
import pandas as pd
import plotly.express as px
# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/yatinlakkaraju123/post-scrapping/main/linkedinscrapper/data/postspider/postspider_2023-07-05T10-57-40.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='LINKEDIN DASHBOARD'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='hashtag1', y='likes', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
