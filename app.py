# Import packages
from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objs as go

# Incorporate data
df2 = pd.read_csv(
    'https://raw.githubusercontent.com/yatinlakkaraju123/post-scrapping/main/linkedinscrapper/data/postspider/modified_file.csv')
df = pd.read_csv(
    'https://raw.githubusercontent.com/yatinlakkaraju123/post-scrapping/main/linkedinscrapper/data/postspider/modified_file1.csv')
df = df._append(df2, ignore_index=True)
df.drop(df.columns[[1]], axis=1, inplace=True)

# Reshape the data to get all hashtags
hashtag_columns = ['hashtag1', 'hashtag2', 'hashtag3', 'hashtag4',
                   'hashtag5', 'hashtag6', 'hashtag7', 'hashtag8', 'hashtag9', 'hashtag10']
hashtags = df[hashtag_columns].values.flatten()
hashtags_series = pd.Series(hashtags).dropna()

# Calculate the sum of likes for each hashtag
hashtags_likes = hashtags_series.value_counts().reset_index()
hashtags_likes.columns = ['hashtag', 'likes']

hashtags_likes.sort_values(by='likes', ascending=False, inplace=True)
top_5_hashtags = hashtags_likes.head(10)
hashtags_top_5 = hashtags_likes.head(5).hashtag
likes_top_5 = hashtags_likes.head(5).likes

most_liked_hashtag = top_5_hashtags.iloc[0].hashtag
# Remove commas from 'likes' column
df['likes'] = df['likes'].str.replace(',', '')
df['likes'] = pd.to_numeric(df['likes'])
top_5_posts = df[df['hashtag1'] == most_liked_hashtag].nlargest(5, 'likes')[
    'post']
top_5_posts_likes = df[df['hashtag1'] == most_liked_hashtag].nlargest(5, 'likes')['likes']
second_most_liked_hashtag = top_5_hashtags.iloc[1].hashtag
# df['likes'] = df['likes'].str.replace(',', '')  # Remove commas from 'likes' column
# df['likes'] = pd.to_numeric(df['likes'])
top_5_posts_for_second_most = df[df['hashtag1'] ==
                                 second_most_liked_hashtag].nlargest(5, 'likes')['post']
top_5_posts_for_second_most_likes = df[df['hashtag1'] ==
                                 second_most_liked_hashtag].nlargest(5, 'likes')['likes']
third_most_liked_hashtag = top_5_hashtags.iloc[2].hashtag
top_5_posts_for_third_most = df[df['hashtag1'] ==
                                third_most_liked_hashtag].nlargest(5, 'likes')['post']
top_5_posts_for_third_most_likes = df[df['hashtag1'] ==
                                third_most_liked_hashtag].nlargest(5, 'likes')['likes']
fourth_most_liked_hashtag = top_5_hashtags.iloc[3].hashtag
top_5_posts_for_fourth_most = df[df['hashtag1'] ==
                                 fourth_most_liked_hashtag].nlargest(5, 'likes')['post']
top_5_posts_for_fourth_most_likes = df[df['hashtag1'] ==
                                 fourth_most_liked_hashtag].nlargest(5, 'likes')['likes']
fifth_most_liked_hashtag = top_5_hashtags.iloc[4].hashtag
top_5_posts_for_fifth_most = df[df['hashtag1'] ==
                                fifth_most_liked_hashtag].nlargest(5, 'likes')['post']
top_5_posts_for_fifth_most_likes = df[df['hashtag1'] ==
                                fifth_most_liked_hashtag].nlargest(5, 'likes')['likes']
# hashtags_likes_1 = hashtags_likes
# hashtags_likes_1.loc[hashtags_likes_1['likes']<likes_top_5[4],'hashtag'] = 'Other hashtags'
combined_hashtags = pd.concat([df[col] for col in df.columns if col.startswith('hashtag')])

hashtags_counts = combined_hashtags.value_counts()

top_10_hashtags = hashtags_counts.head(10)

bar_color = '#A7EDE7'

# bootstrap cards
card = dbc.Card(
    [

        dbc.CardBody(
            [
                
                
                html.Div(
                    html.Div(
                        children=hashtags_top_5[0]+"\t"+"\t"+str(likes_top_5[0])),
                    
                        className="card-text",
                ),


            ]
        ),
    ],
    style={"width": "18rem"},
)
card1 = dbc.Card(
    [

        dbc.CardBody(
            [
                
                
                html.Div(
                    html.Div(
                        children=hashtags_top_5[1]+"\t"+"\t"+str(likes_top_5[1])),
                    
                        className="card-text",
                ),


            ]
        ),
    ],
    style={"width": "18rem"},
)
card2 = dbc.Card(
    [

        dbc.CardBody(
            [
                
                
                html.Div(
                    html.Div(
                        children=hashtags_top_5[2]+"\t"+"\t"+str(likes_top_5[2])),
                    
                        className="card-text",
                ),


            ]
        ),
    ],
    style={"width": "18rem"},
)
card3 = dbc.Card(
    [

        dbc.CardBody(
            [
                
                
                html.Div(
                    html.Div(
                        children=hashtags_top_5[3]+"\t"+"\t"+str(likes_top_5[3])),
                    
                        className="card-text",
                ),


            ]
        ),
    ],
    style={"width": "18rem"},
)
card4 = dbc.Card(
    [

        dbc.CardBody(
            [
               
                
                html.Div(
                    html.Div(
                        children=hashtags_top_5[4]+"\t"+"\t"+str(likes_top_5[4])),
                    
                        className="card-text",
                ),


            ]
        ),
    ],
    style={"width": "18rem"},
)

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
bar_chart = px.bar(top_5_hashtags, x='hashtag', y='likes',
                      color_discrete_sequence=[bar_color])
bar_chart.update_yaxes(title_text="No of occurences")
# App layout
app.layout = html.Div([
    # Add the LinkedIn logo and align it to the left
    html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjoFrGy1SjTOXrd0EbOvODvgiI0dVRY2bESA&usqp=CAU',
             style={'width': '300px', }),

    dcc.Graph(
        figure=bar_chart,
        # Adjust the margin-top value as needed
        style={'height': '400px', 'margin-top': '80px'}
    ),
       dbc.Row([dbc.Col(card, width=2),
             ], justify="around"),
              dbc.Row([dbc.Col(card1, width=2),
             ], justify="around"),
              dbc.Row([dbc.Col(card2, width=2)
             ], justify="around"),
              dbc.Row([dbc.Col(card3, width=2),
             ], justify="around"),
              dbc.Row([dbc.Col(card4, width=2),
             ], justify="around"),


    html.Div(children=hashtags_top_5[0]+"\t"+"\t"+str(likes_top_5[0])),
    html.Div(children=hashtags_top_5[1]+"\t"+"\t"+str(likes_top_5[1])),
    html.Div(children=hashtags_top_5[2]+"\t"+"\t"+str(likes_top_5[2])),
    html.Div(children=hashtags_top_5[3]+"\t"+"\t"+str(likes_top_5[3])),
    html.Div(children=hashtags_top_5[4]+"\t"+"\t"+str(likes_top_5[4])),
    html.H2('Top 5 Posts of Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post, href=post)) for post in top_5_posts]),
    html.Ul([html.Li(html.A(post)) for post in top_5_posts_likes]),
    html.H2('Top 5 Posts of Second Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post, href=post))
            for post in top_5_posts_for_second_most]),
            html.Ul([html.Li(html.A(post)) for post in top_5_posts_for_second_most_likes]),
    html.H2('Top 5 Posts of Third Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post, href=post))
            for post in top_5_posts_for_third_most]),
    html.Ul([html.Li(html.A(post)) for post in top_5_posts_for_third_most_likes]),
    html.H2('Top 5 Posts of Fourth Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post, href=post))
            for post in top_5_posts_for_fourth_most]),
            html.Ul([html.Li(html.A(post)) for post in top_5_posts_for_fourth_most_likes]),
    html.H2('Top 5 Posts of Fifth Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post, href=post))
            for post in top_5_posts_for_fifth_most]),
            html.Ul([html.Li(html.A(post)) for post in top_5_posts_for_fifth_most_likes]),

 
                 dcc.Graph(
        id='top-10-hashtags-pie',
        figure={
            'data': [
                go.Pie(labels=top_10_hashtags.index, values=top_10_hashtags.values, hole=0.5)
            ],
            'layout': go.Layout(title='Top 10 Hashtags')
        }
    )


], style={'max-width': '1300px', 'margin': '0 auto'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


