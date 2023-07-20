# Import packages
from dash import Dash, html, dcc,dash_table
import pandas as pd
import plotly.express as px

# Incorporate data
df2 = pd.read_csv('https://raw.githubusercontent.com/yatinlakkaraju123/post-scrapping/main/linkedinscrapper/data/postspider/modified_file.csv')
df =pd.read_csv('https://raw.githubusercontent.com/yatinlakkaraju123/post-scrapping/main/linkedinscrapper/data/postspider/modified_file1.csv')
df = df._append(df2, ignore_index = True)
df.drop(df.columns[[ 1]], axis=1, inplace=True)

# Reshape the data to get all hashtags
hashtag_columns = ['hashtag1', 'hashtag2', 'hashtag3', 'hashtag4', 'hashtag5', 'hashtag6', 'hashtag7', 'hashtag8', 'hashtag9', 'hashtag10']
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
df['likes'] = df['likes'].str.replace(',', '')  # Remove commas from 'likes' column
df['likes'] = pd.to_numeric(df['likes'])
top_5_posts = df[df['hashtag1'] == most_liked_hashtag].nlargest(5, 'likes')['post']

second_most_liked_hashtag = top_5_hashtags.iloc[1].hashtag
#df['likes'] = df['likes'].str.replace(',', '')  # Remove commas from 'likes' column
#df['likes'] = pd.to_numeric(df['likes'])
top_5_posts_for_second_most =  df[df['hashtag1'] == second_most_liked_hashtag].nlargest(5, 'likes')['post']

third_most_liked_hashtag =top_5_hashtags.iloc[2].hashtag
top_5_posts_for_third_most = df[df['hashtag1'] == third_most_liked_hashtag].nlargest(5, 'likes')['post']
fourth_most_liked_hashtag =top_5_hashtags.iloc[3].hashtag
top_5_posts_for_fourth_most = df[df['hashtag1'] == fourth_most_liked_hashtag].nlargest(5, 'likes')['post']
fifth_most_liked_hashtag =top_5_hashtags.iloc[4].hashtag
top_5_posts_for_fifth_most = df[df['hashtag1'] == fifth_most_liked_hashtag].nlargest(5, 'likes')['post']

#hashtags_likes_1 = hashtags_likes
#hashtags_likes_1.loc[hashtags_likes_1['likes']<likes_top_5[4],'hashtag'] = 'Other hashtags'


bar_color = '#A7EDE7'

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    # Add the LinkedIn logo and align it to the left
    html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjoFrGy1SjTOXrd0EbOvODvgiI0dVRY2bESA&usqp=CAU', style={'width': '300px', }),

    dcc.Graph(
        figure=px.bar(top_5_hashtags, x='hashtag', y='likes', color_discrete_sequence=[bar_color]),
        style={'height': '400px', 'margin-top': '80px'}  # Adjust the margin-top value as needed
    ),
    dcc.Graph(
       
        figure=px.pie(hashtags_likes,values='likes',names='hashtag',title='pie chart',hole=.3),
        style = {'height':'300px'}
    ),

html.Div(children=hashtags_top_5[0]+"\t"+"\t"+str(likes_top_5[0])),
    html.Div(children=hashtags_top_5[1]+"\t"+"\t"+str(likes_top_5[1])),
    html.Div(children=hashtags_top_5[2]+"\t"+"\t"+str(likes_top_5[2])),
    html.Div(children=hashtags_top_5[3]+"\t"+"\t"+str(likes_top_5[3])),
    html.Div(children=hashtags_top_5[4]+"\t"+"\t"+str(likes_top_5[4])),
       html.H2('Top 5 Posts of Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post,href=post)) for post in top_5_posts]),
           html.H2('Top 5 Posts of Second Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post,href=post)) for post in top_5_posts_for_second_most]),
               html.H2('Top 5 Posts of Third Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post,href=post)) for post in top_5_posts_for_third_most]),
               html.H2('Top 5 Posts of Fourth Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post,href=post)) for post in top_5_posts_for_fourth_most]),
               html.H2('Top 5 Posts of Fifth Most Liked Hashtag'),
    html.Ul([html.Li(html.A(post,href=post)) for post in top_5_posts_for_fifth_most]),


  
], style={'max-width': '1300px', 'margin': '0 auto'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
