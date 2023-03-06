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
dash.register_page(__name__, path='/', name='PIB') # '/' is home page

# page 1 data
pd.read_csv("dados_pib.csv")
df4 = pd.read_csv("dados_pib.csv")
df4.columns = ["Data","pib_mensal","ipca","100","deflator","pib_real"]
df4['Data'] = pd.to_datetime(df4['Data'],dayfirst=True)
dff4 = df4.set_index(['Data'])

checklist = dcc.Checklist(
                    id='checklist',
                    options=[
                             {'label': 'pib mensal', 'value': 'pib_mensal'},
                             {'label': 'pib real', 'value': 'pib_real'},
                    ],
                    value=['pib_mensal','pib_real'],
                    style={"width": "60%"}
                )



layout = html.Div([
        html.H3('PIB'),
        dcc.DatePickerRange(
            id="date-picker2",
            start_date=datetime(1990, 1, 1),
            end_date=datetime(2023, 1 ,1),
            display_format="DD/MM/YYYY",
            clearable=False,
            number_of_months_shown=1
        ),
        dbc.Container([checklist]),
        dcc.Graph(
            id='pib'),
        html.H6('Fonte: Banco Central do Brasil')
        ])



@callback(
    Output('pib', 'figure'),
    [Input('checklist','value'),
    Input('date-picker2', 'start_date'),
    Input('date-picker2', 'end_date')]
)
def update(checklist,start_date,end_date):
    dfff4 = dff4.loc[start_date: end_date]
    fig4 = px.line(
        dfff4, y=checklist,
    )
    fig4.update_layout(legend_title="PIB", margin=dict(t=20),transition_duration=500,
                       template="plotly_dark")
    return fig4
