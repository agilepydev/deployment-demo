import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/final_data.csv')

app = dash.Dash()



app.layout = html.Div(children=[
    dcc.Link('Navigate to "/"', href='index.html'),
    html.H1(children='Games Dashboard'),
    dcc.Dropdown(id='features1-dropdown',
                 options=[{'label': 'revenue', 'value': 'revenue'},
                          {'label': 'price', 'value': 'price'}],
                          
                 value= "currency"),
    
    dcc.Dropdown(id='features2-dropdown',
                 options=[{'label': 'revenue', 'value': 'revenue'},
                          {'label': 'price', 'value': 'price'}],
                          
                 value= "currency"),
    dcc.Graph(id='graph')
])




@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='features1-dropdown', component_property='value'),
    Input(component_id='features2-dropdown', component_property='value')
)
def update_graph(val1, val2):

    x = df[val1].iloc[:10]
    y = df[val2].iloc[:10]

    fig =px.bar(df,x= x, y=y)
    
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
    
    
