# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options







pd.read_csv("bcdata.divida.csv")
df = pd.read_csv("bcdata.divida.csv", sep = ';',decimal=',')
df.columns = ["Data","Valor"]

fig = px.line(df, x="Data", y="Valor",  title='Dívida líquida do setor público consolidado.')


app.layout = html.Div(children=[
    html.H1(children='Economic Studio'),

    html.Div(children='''
        Data, information and forecast.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])






if __name__ == '__main__':
    app.run_server(debug=True)