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
    app.run_server(debug=True)
    
    
