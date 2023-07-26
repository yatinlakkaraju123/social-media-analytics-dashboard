import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('modified_file.csv')

combined_hashtags = pd.concat([df[col] for col in df.columns if col.startswith('hashtag')])

hashtags_counts = combined_hashtags.value_counts()

top_10_hashtags = hashtags_counts.head(10)


colors = ['#9ACD32', '#FFA07A', '#FFB6C1', '#ADD8E6', '#FFD700', '#DA70D6', '#FFC0CB', '#BC8F8F', '#A9A9A9', '#AFEEEE']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='top-10-hashtags-Area',
        figure={
            'data': [
                go.Scatter(
                    x=top_10_hashtags.index,
                    y=top_10_hashtags.values,
                    mode='lines+markers',
                    name=hashtag,
                    line=dict(color=colors[i], width=2, shape='linear', smoothing=1.3),
                    fill='tozeroy',
                    fillcolor=colors[i],  
                    marker=dict(color=colors[i], size=8),
                    hovertemplate='<b>Hashtag: %{x}</b><br>Likes: %{y}',
                ) for i, hashtag in enumerate(top_10_hashtags.index)
            ] + [
                go.Scatter(
                    x=top_10_hashtags.index,
                    y=[0] * len(top_10_hashtags.index),
                    mode='lines',
                    fill='tozeroy',
                    fillcolor='white', 
                    showlegend=False,
                )
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
