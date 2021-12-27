import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('final_data.csv')

app = dash.Dash()



app.layout = html.Div(children=[
    html.H1(children='Games Dashboard'),
    dcc.Dropdown(id='features-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in df['currency'].unique()],
                 value= "EUR"),
    dcc.Graph(id='revenue-graph')
])

@app.callback(
    Output(component_id='revenue-graph', component_property='figure'),
    Input(component_id='features-dropdown', component_property='value')
)
def update_graph(selected_currency):
    filtered_games = df[df['currency'] == selected_currency]
    line_fig = px.scatter(filtered_games,
                       x='release date', y='revenue',
                       color='currency',
                       title=f'Game Revenue in {selected_currency}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)
    
    
