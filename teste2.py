from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


pd.read_csv("bcdata.divida.csv")
df = pd.read_csv("bcdata.divida.csv", sep = ';',decimal=',')
df.columns = ["Data","Valor"]
fig_divida = px.line(df, x="Data", y="Valor",  title='Dívida líquida do setor público consolidado.')


pd.read_csv("bcdata.atividadebc.csv")
df2 = pd.read_csv("bcdata.atividadebc.csv", sep = ';',decimal=',')
df2.columns = ["Data","Valor"]
fig_atividade = px.line(df2, x="Data", y="Valor",  title='Índice de atividade econômica do banco central.')

pd.read_csv("bcdata.transacoes.csv")
df3 = pd.read_csv("bcdata.transacoes.csv", sep = ';',decimal=',')
df3.columns = ["Data","Valor"]
fig_transacoes = px.line(df3, x="Data", y="Valor",  title='Transações Correntes acumulado em 12 meses - mensal.')




app.layout = html.Div([
    html.H1('Economic Studio', style={'textAlign': 'center'}),

        html.Div(children='''
        Data, information and forecast.
    ''', style={'textAlign': 'center'}),

    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Dívida', value='tab-1-example-graph'),
        dcc.Tab(label='Atividade BC', value='tab-2-example-graph'),
        dcc.Tab(label='Transações', value='tab-3-example-graph')
    ]),
    html.Div(id='tabs-content-example-graph')

])

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.H3('Divida Líquida'),
            dcc.Graph(
            id='divida',
            figure=fig_divida
            ),
            dcc.RangeSlider(min=df['Data'].min().day,
                            max=df['Data'].max().day,
                            step=  1,
                            value=df['Data'].min().day, id='my-range-slider'),
            html.H6('Fonte: Banco Central do Brasil')
        ])

    


    elif tab == 'tab-2-example-graph':
        return html.Div([
            html.H3('Índice de atividade'),
            dcc.Graph(
                id='atividade',
                figure=fig_atividade
            ),
            html.H6('Fonte: Banco Central do Brasil')
        ])
    
    elif tab == 'tab-3-example-graph':
        return html.Div([
            html.H3('Transações Correntes'),
            dcc.Graph(
                id='atividade',
                figure=fig_transacoes
            ),
            html.H6('Fonte: Banco Central do Brasil')
        ])



if __name__ == '__main__':
    app.run_server(debug=True)