# Import packages
from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objs as go
import re
from urllib.parse import urlparse
# Incorporate data
#Yatin if you find time then please make a README, it would make it a bit easier for the next folks who see this code to understand it -Somaansh
df2 = pd.read_csv(
    'https://raw.githubusercontent.com/yatinlakkaraju123/linkedin-scrapping-latest/main/linkedinscrapper/data/postspider/modified_file_3.csv')
df = pd.read_csv(
    'https://raw.githubusercontent.com/yatinlakkaraju123/linkedin-scrapping-latest/main/linkedinscrapper/data/postspider/modified_file_4.csv')
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
def extract_content_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    content = path.split("/")[-1] if path.endswith("/") else path.split("/")[-1]
    return content
most_liked_hashtag = top_5_hashtags.iloc[0].hashtag
# Remove commas from 'likes' column
df['likes'] = df['likes'].str.replace(',', '')
df['likes'] = pd.to_numeric(df['likes'])
df['content'] = df['post'].apply(extract_content_from_url)

#-------------------- New Function to Clean the labels for the tabs --------------------
def CleanPostObject(PostObject):
    pattern = r'[0-9]'
    pattern2 = r'[A-z]*$'
    new_string = re.sub(pattern, '', PostObject)
    new_string = re.sub(pattern2, '', new_string)
    return new_string.replace("-", " ")
#-------------------- END --------------------
def LinkCardMaker(LikesObject,PostsObject,UrlObject):
    return  dbc.Card(
        [
            dbc.CardBody(
                [   
                    #most hashtags                 
                    dbc.ListGroup(
                        [
                            dbc.ListGroupItem(
                                [
                                    #added the above method here
                                    html.H6(CleanPostObject(post)),
                                    html.Small("Likes:" + str(likes), className="text-muted"),
                                ],
                                href=url,action=True,
                                ) for post,likes,url in zip(PostsObject,LikesObject,UrlObject)
                        ]   
                    )
                ]
            ),
        ],
    )
    
    
top_5_posts = df[df['hashtag1'] == most_liked_hashtag].nlargest(5, 'likes')[
    'content']
top_5_urls = df[df['hashtag1'] == most_liked_hashtag].nlargest(5, 'likes')[
    'post']
top_5_posts_likes = df[df['hashtag1'] == most_liked_hashtag].nlargest(5, 'likes')[
    'likes']
second_most_liked_hashtag = top_5_hashtags.iloc[1].hashtag
# df['likes'] = df['likes'].str.replace(',', '')  # Remove commas from 'likes' column
# df['likes'] = pd.to_numeric(df['likes'])
top_5_posts_for_second_most = df[df['hashtag1'] ==
                                 second_most_liked_hashtag].nlargest(5, 'likes')['content']
top_5_urls_for_second_most = df[df['hashtag1'] == second_most_liked_hashtag].nlargest(5, 'likes')[
    'post']
top_5_posts_for_second_most_likes = df[df['hashtag1'] ==
                                       second_most_liked_hashtag].nlargest(5, 'likes')['likes']
third_most_liked_hashtag = top_5_hashtags.iloc[2].hashtag
top_5_posts_for_third_most = df[df['hashtag1'] ==
                                third_most_liked_hashtag].nlargest(5, 'likes')['content']
top_5_urls_for_third_most = df[df['hashtag1'] == third_most_liked_hashtag].nlargest(5, 'likes')[
    'post']
top_5_posts_for_third_most_likes = df[df['hashtag1'] ==
                                      third_most_liked_hashtag].nlargest(5, 'likes')['likes']
fourth_most_liked_hashtag = top_5_hashtags.iloc[3].hashtag
top_5_posts_for_fourth_most = df[df['hashtag1'] ==
                                 fourth_most_liked_hashtag].nlargest(5, 'likes')['content']
top_5_urls_for_fourth_most = df[df['hashtag1'] == fourth_most_liked_hashtag].nlargest(5, 'likes')[
    'post']
top_5_posts_for_fourth_most_likes = df[df['hashtag1'] ==
                                       fourth_most_liked_hashtag].nlargest(5, 'likes')['likes']
fifth_most_liked_hashtag = top_5_hashtags.iloc[4].hashtag
top_5_posts_for_fifth_most = df[df['hashtag1'] ==
                                fifth_most_liked_hashtag].nlargest(5, 'likes')['content']
top_5_urls_for_fifth_most = df[df['hashtag1'] == fifth_most_liked_hashtag].nlargest(5, 'likes')[
    'post']
top_5_posts_for_fifth_most_likes = df[df['hashtag1'] ==
                                      fifth_most_liked_hashtag].nlargest(5, 'likes')['likes']
# hashtags_likes_1 = hashtags_likes
# hashtags_likes_1.loc[hashtags_likes_1['likes']<likes_top_5[4],'hashtag'] = 'Other hashtags'
combined_hashtags = pd.concat(
    [df[col] for col in df.columns if col.startswith('hashtag')])

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
#-------------------- ADDING THE LINKS CARD FOR THE PAGE --------------------
#links for the hashtags (just change the parameters here itself, i think it would be easier this way)


card5 = LinkCardMaker(top_5_posts_likes,top_5_posts,top_5_urls)

card6 = LinkCardMaker(top_5_posts_for_second_most_likes,top_5_posts_for_second_most,top_5_urls_for_second_most)

card7 = LinkCardMaker(top_5_posts_for_third_most_likes,top_5_posts_for_third_most,top_5_urls_for_third_most)

card8 = LinkCardMaker(top_5_posts_for_fourth_most_likes,top_5_posts_for_fourth_most,top_5_urls_for_fourth_most)

card9 = LinkCardMaker(top_5_posts_for_fifth_most_likes,top_5_posts_for_fifth_most,top_5_urls_for_fifth_most)

#making the tabs for the cards
hashtags_top_5 = hashtags_top_5.drop_duplicates().dropna()

# Print the cleaned labels to verify the changes

tabs = dcc.Tabs(
    [
        dcc.Tab(card5, label=(hashtags_top_5.iloc[0])),
        dcc.Tab(card6, label=(hashtags_top_5.iloc[1])),
        dcc.Tab(card7, label=(hashtags_top_5.iloc[2])),
        dcc.Tab(card8, label=(hashtags_top_5.iloc[3])),
        dcc.Tab(card9, label=(hashtags_top_5.iloc[4])),
    ]
)
# Print the cleaned labels for troubleshooting

#-------------------- THE LINKS CARD FOR THE PAGE HAS BEEN ADDED --------------------

#Making the dash Web Page layout from here, the app variable is used for initializing the app, and then we set some parameters for our bar chart and then
#we move on to the app.layout variable which is being used as something similar to HTML,
#documentation for the different methods used can be found on plotly,dash and dash-bootstrap-components' respective documentations
#the start page for the affortmentioned documentations are here:-
# DASH BOOTSTRAP COMPONENTS: https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/
# DASH: https://dash.plotly.com/

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
bar_chart = px.bar(top_5_hashtags, x='hashtag', y='likes',
                   color_discrete_sequence=[bar_color])
bar_chart.update_yaxes(title_text="No of occurences")
# App layout, below column width is for "width" parameter used for the hashtags part which i have commented so this isn't really being used but if you want to
#change anything back then you can keep this in mind
column_width = "auto"

app.layout = html.Div([
    dbc.Row([dbc.Col([html.Header(style={'background-color': '#000', 'color': '#fff', 'text-align': 'center', 'padding': '20px', 'margin': '0'},
                children=[
                    html.Img(src="https://www.bostonindia.in/assets/images/logoW30y.png", alt="Logo", style={'width': '120px', 'float': 'left'}),
                    html.H1("LinkedIn Posts Analytics Dashboard", style={'font-size': '24px', 'display': 'inline-block', 'margin-left': '10px'})
                ]
    ),])
            ], ),
    #heading of the page
   
    # Add the LinkedIn logo and align it to the left
    dbc.Row([html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjoFrGy1SjTOXrd0EbOvODvgiI0dVRY2bESA&usqp=CAU',
             style={'width': '300px','margin-top': '40px','margin-left': '70px' }),], ), #added  a margin here as well ------------------------------

    #the bar graph is added here
    dbc.Row([dcc.Graph(
        figure=bar_chart,
        # Adjust the margin-top value as needed
        style={ }
    ),], ),

#the pie chart is added here
 dbc.Row([   
        dcc.Graph(
            id='top-10-hashtags-pie',
            figure={
                'data': [
                    go.Pie(labels=top_10_hashtags.index,
                        values=top_10_hashtags.values, hole=0.5)
                ],
                'layout': go.Layout(title='Top 10 Hashtags')
            }
        )
    ], 
    justify="around"),
#the Code under here is for a few cards i mentioned earlier when i talked about the column_width variable

# dbc.Row([dbc.Col(card,width=column_width),dbc.Col(card1,width=column_width ),dbc.Col(card2,width=column_width ),dbc.Col(card3,width=column_width),dbc.Col(card4, width=column_width)],justify="evenly"),

#    dbc.Row([dbc.Col(card2, )
#             ], justify="around"),
#    dbc.Row([dbc.Col(card3,),
#             ], justify="around"),
#    dbc.Row([dbc.Col(card4, ),
#             ], justify="around"),

#-------- Added Margins Over here as well --------
dbc.Row([html.H5('Top 5 Posts of Each Hashtag')],style={ 'margin': '70px'}),

dbc.Row([
    dbc.Col(tabs),
],
style={ 'margin': '70px'}
),
#-------- End --------
dbc.Row([
    dbc.Col(  html.Footer(style={'background-color': '#000', 'color': '#fff', 'text-align': 'center', 'padding': '10px', 'position': 'relative', 'bottom': '0', 'left': '0', 'width': '100%'},
                children=[
                    html.P(" 2023 Boston IT Solutions (India) Private Limited")
                ]
    )),
]),


], style={ 'margin': '0 auto'}

)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

#Above Code has been made as an internship project by Somaansh Virmani, Lakkraju Yatin, Shubhi Goel, Shaurya Pandey and Surya Kiran
#Students of MIT Bengaluru
#This app was made as part of an internship held by BOSTON IT Solutions

