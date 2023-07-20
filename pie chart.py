import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv('modified_file.csv')


combined_hashtags = pd.concat([df[col] for col in df.columns if col.startswith('hashtag')])


hashtags_counts = combined_hashtags.value_counts()


top_10_hashtags = hashtags_counts.head(10)


app = dash.Dash(__name__)


app.layout = html.Div([
    
    dcc.Graph(
        id='top-10-hashtags-pie',
        figure={
            'data': [
                go.Pie(labels=top_10_hashtags.index, values=top_10_hashtags.values)
            ],
            'layout': go.Layout(title='Top 10 Hashtags (Pie Chart)')
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
