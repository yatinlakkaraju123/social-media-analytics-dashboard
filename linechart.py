import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('modified_file.csv')

combined_hashtags = pd.concat([df[col] for col in df.columns if col.startswith('hashtag')])

hashtags_counts = combined_hashtags.value_counts()

top_10_hashtags = hashtags_counts.head(10)


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'cyan']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='top-10-hashtags-Line',
        figure={
            'data': [
                go.Scatter(
                    x=top_10_hashtags.index,
                    y=top_10_hashtags.values,
                    mode='lines+markers',  
                    name=hashtag,
                    line=dict(color=colors[i], width=2),  
                    marker=dict(color=colors[i], size=8),  
                    hovertemplate='<b>Hashtag: %{x}</b><br>Likes: %{y}',
                ) for i, hashtag in enumerate(top_10_hashtags.index)
            ],
            'layout': go.Layout(
                title='Top 10 Hashtags',
                xaxis={'title': 'Hashtags', 'showgrid': False},  
                yaxis={'title': 'Likes', 'showgrid': True, 'gridcolor': '#f0f0f0'},  
                hovermode='closest',  
                font=dict(family='Arial, sans-serif', size=12),  
                plot_bgcolor='#f9f9f9',  
                paper_bgcolor='#ffffff',  
                margin={'l': 50, 'r': 50, 't': 80, 'b': 50},  
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
