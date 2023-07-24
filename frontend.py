import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Header(style={'background-color': '#000', 'color': '#fff', 'text-align': 'center', 'padding': '20px', 'margin': '0'},
                children=[
                    html.Img(src="newlogo.png", alt="Logo", style={'width': '120px', 'float': 'left'}),
                    html.H1("LinkedIn Posts Analytics Dashboard", style={'font-size': '24px', 'display': 'inline-block', 'margin-left': '10px'})
                ]
    ),
    html.Footer(style={'background-color': '#000', 'color': '#fff', 'text-align': 'center', 'padding': '10px', 'position': 'absolute', 'bottom': '0', 'left': '0', 'width': '100%'},
                children=[
                    html.P("&copy; 2023 Boston IT Solutions (India) Private Limited")
                ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
