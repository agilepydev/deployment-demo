import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
import os

app = dash.Dash(__name__)
server = app.server


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "games.db"))
df = []
engine = sqlalchemy.create_engine(database_file)
DBSession = sessionmaker(bind=engine)
session = DBSession()

inspector = inspect(engine)

# Get table information
print(inspector.get_table_names())

with engine.connect() as connection:
    df = pd.read_sql("games", connection)
        
 

app = dash.Dash()



app.layout = html.Div(children=[
    html.H1(children='Games Dashboard'),
    dcc.Dropdown(id='features1-dropdown',
                 options=[{'label': 'revenue', 'value': 'revenue'},
                          {'label': 'price', 'value': 'price'},
                          {'label': 'currency', 'value': 'currency'},
                          {'label': 'name', 'value': 'name'},
                          {'label': 'positive reviews', 'value': 'total_positive_reviews'},
                          {'label': 'negative reviews', 'value': 'total_negative_reviews'},
                          {'label': 'amount reviews', 'value': 'number_reviews'},
                          {'label': 'release date', 'value': 'release date'},
                          {'label': 'id', 'value': 'id'}],
                 
                          
                 value= "currency"),
    
    dcc.Dropdown(id='features2-dropdown',
                 options=[{'label': 'revenue', 'value': 'revenue'},
                          {'label': 'price', 'value': 'price'},
                          {'label': 'currency', 'value': 'currency'},
                          {'label': 'name', 'value': 'name'},
                          {'label': 'positive reviews', 'value': 'total_positive_reviews'},
                          {'label': 'negative reviews', 'value': 'total_negative_reviews'},
                          {'label': 'amount reviews', 'value': 'number_reviews'},
                          {'label': 'release date', 'value': 'release_date'},
                          {'label': 'id', 'value': 'id'}],
                          
                 value= "currency"),
    dcc.Graph(id='revenue-graph')
])




@app.callback(
    Output(component_id='revenue-graph', component_property='figure'),
    Input(component_id='features1-dropdown', component_property='value'),
    Input(component_id='features2-dropdown', component_property='value')
)
def update_graph(val1, val2):

    x = df[val1].iloc[:10]
    y = df[val2].iloc[:10]

    fig =px.bar(df,x= x, y=y)
    
    return fig



if __name__ == '__main__':
    port = os.environ.get('PORT') if os.environ.get('PORT') is not None else 5000
    print("PORT:",port)

    app.run_server(host = "0.0.0.0", port = port, debug=True)