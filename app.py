# Import packages
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/yatinlakkaraju123/post-scrapping/main/linkedinscrapper/data/postspider/modified_file.csv')
df.drop(df.columns[[0, 1, 3]], axis=1, inplace=True)

# Reshape the data to get all hashtags
hashtag_columns = ['hashtag1', 'hashtag2', 'hashtag3', 'hashtag4', 'hashtag5', 'hashtag6', 'hashtag7', 'hashtag8', 'hashtag9', 'hashtag10']
hashtags = df[hashtag_columns].values.flatten()
hashtags_series = pd.Series(hashtags).dropna()

# Calculate the sum of likes for each hashtag
hashtags_likes = hashtags_series.value_counts().reset_index()
hashtags_likes.columns = ['hashtag', 'likes']
hashtags_likes.sort_values(by='likes', ascending=False, inplace=True)
top_5_hashtags = hashtags_likes.head(10)

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='LINKEDIN DASHBOARD'),
    dcc.Graph(
        figure=px.bar(top_5_hashtags, x='hashtag', y='likes'),
    ),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
