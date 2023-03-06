from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from datetime import datetime
import dash_bootstrap_components as dbc
import dash

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)
#app.config['suppress_callback_exceptions'] = True
dash.register_page(__name__, name='PIB TESTE') # '/' is home page

# page 1 data
# pd.read_csv("bcdata.atividadebc.csv")
# df2 = pd.read_csv("bcdata.atividadebc.csv", sep = ';',decimal=',')
# df2.columns = ["Data","Valor"]
# fig_atividade = px.line(df2, x="Data", y="Valor",  title='Índice de atividade econômica do banco central.')
# df2['Data'] = pd.to_datetime(df2['Data'],dayfirst=True)
# #df2['Data'] = df2['Data'].dt.year
# df2= df2.set_index(['Data'])

pd.read_csv("dados_pib.csv")
df4 = pd.read_csv("dados_pib.csv")
df4.columns = ["Data","pib_mensal","ipca","100","deflator","pib_real"]
df4['Data'] = pd.to_datetime(df4['Data'],dayfirst=True)
df4['Data'] = df4['Data'].dt.year
df4 = df4.set_index(['Data'])




layout = html.Div([
        html.H3('PIB - SLIDER'),
        dcc.Graph(
            id='pib2'
            #figure=fig_atividade
            ),
        dcc.RangeSlider(
            id='my-range-slider',
            marks={
                2003: '2003',     # key=position, value=what you see
                2004: '2004',
                2005: '2005',
                2006: '2006',
                2007: '2007',
                2008: '2008',
                2009: '2009',
                2010: '2010',
                2011: '2011',
                2012: '2012',
                2013: '2013',
                2014: '2014',
                2015: '2015',
                2016: '2016',
                2017: '2017',
                2018: '2018',
                2019: '2019',
                2020: '2020',
                2021: '2021',
                2022: '2022',
            },
            step=1,
            min=1990,
            max=2023,
            value=[1990,2023]
            ),
        html.H6('Fonte: Banco Central do Brasil')
        ])


@callback(
    Output('pib2','figure'),
    [Input('my-range-slider','value')]
)
# def update_graph(years):
#     dfff4 = dff4.loc[years[1]:years[0]]
#     #dff2=df[(df2['Data']>=years[0])&(df2['Data']<=years[1])]
#     fig2 = px.scatter(dfff4, y="pib_real",
#                     title='Índice de atividade econômica do banco central.')
#     fig2.update_layout(transition_duration=500)
#     return fig2
def update_graph(years):
    dff4 = df4.loc['1990':'2023']
    #dff4=df4[(df4['Data']>=years[0])&(df4['Data']<=years[1])]
    fig2 = px.scatter(dff4, y="pib_real",
                    title='Índice de atividade econômica do banco central.')
    fig2.update_layout(transition_duration=500)
    return fig2
