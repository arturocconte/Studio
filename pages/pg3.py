from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from datetime import datetime
import dash_bootstrap_components as dbc
import dash
from plotly.subplots import make_subplots

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = Dash(__name__, external_stylesheets=external_stylesheets)
#app.config['suppress_callback_exceptions'] = True
dash.register_page(__name__, name='PIB-IPCA') # '/' is home page

# page 1 data
pd.read_csv("dados_pib.csv")
df5 = pd.read_csv("dados_pib.csv")
df5.columns = ["Data","pib_mensal","ipca","100","deflator","pib_real"]
df5['Data'] = pd.to_datetime(df5['Data'],dayfirst=True)
dff5 = df5.set_index(['Data'])

checklist2 = dcc.Checklist(
                    id='checklist2',
                    options=[
                             {'label': 'PIB Mensal', 'value': 'pib_mensal'},
                             {'label': 'PIB Real', 'value': 'pib_real'},
                    ],
                    value=['pib_mensal','pib_real'],
                    style={"width": "60%"}
                )

checklist_ipca = dcc.Checklist(
                    id='checklist_ipca',
                    options=[
                             {'label': 'IPCA', 'value': 'ipca'}
                    ],
                    value=['ipca'],
                    style={"width": "60%"}
                )



layout = html.Div([
        html.H3('PIB'),
        dcc.DatePickerRange(
            id="date-picker3",
            start_date=datetime(1990, 1, 1),
            end_date=datetime(2023, 1 ,1),
            display_format="DD/MM/YYYY",
            clearable=False,
            number_of_months_shown=1
        ),
        dbc.Container([checklist2,checklist_ipca]),
        dcc.Graph(
            id='pib4'),
        html.H6('Fonte: Banco Central do Brasil')
        ])



@callback(
    Output('pib4', 'figure'),
    [Input('checklist2','value'),
     Input('checklist_ipca','value'),
    Input('date-picker3', 'start_date'),
    Input('date-picker3', 'end_date')]
)
def update(checklist2,checklist_ipca,start_date,end_date):
    dfff5 = dff5.loc[start_date: end_date]
    subfig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig6 =  px.line(
        dfff5, y=checklist2, labels={
        "Data": "Data",
        "value": "Valor (milhões de reais)"
        },
    )

    fig7 =  px.line(
        dfff5, y=checklist_ipca, labels={
        "Data": "Data",
        "value": "Valor (milhões de reais)"
        },
    )
    fig7.update_traces(yaxis="y2")


    subfig.add_traces(fig6.data + fig7.data)
    subfig.layout.xaxis.title="Data"
    subfig.layout.yaxis.title="Valor (em milhões)"
    subfig.layout.yaxis2.title="Índice"
    subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))

    subfig.update_layout(legend_title="PIB", margin=dict(t=20),
                       template="plotly")

    return subfig
