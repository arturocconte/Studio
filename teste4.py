from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions'] = True


pd.read_csv("bcdata.divida.csv")
df = pd.read_csv("bcdata.divida.csv", sep = ';',decimal=',')
df.columns = ["Data","Valor"]
fig_divida = px.line(df, x="Data", y="Valor",  title='Dívida líquida do setor público consolidado.')
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
df= df.set_index(['Data'])

pd.read_csv("bcdata.atividadebc.csv")
df2 = pd.read_csv("bcdata.atividadebc.csv", sep = ';',decimal=',')
df2.columns = ["Data","Valor"]
fig_atividade = px.line(df2, x="Data", y="Valor",  title='Índice de atividade econômica do banco central.')
df2['Data'] = pd.to_datetime(df2['Data'],dayfirst=True)
#df2['Data'] = df2['Data'].dt.year
df2= df2.set_index(['Data'])

pd.read_csv("bcdata.transacoes.csv")
df3 = pd.read_csv("bcdata.transacoes.csv", sep = ';',decimal=',')
df3.columns = ["Data","Valor"]
fig_transacoes = px.line(df3, x="Data", y="Valor",  title='Transações Correntes acumulado em 12 meses - mensal.')

pd.read_csv("dados_pib.csv")
df4 = pd.read_csv("dados_pib.csv")
df4.columns = ["Data","pib_mensal","ipca","100","deflator","pib_real"]
df4['Data'] = pd.to_datetime(df4['Data'],dayfirst=True)
dff4 = df4.set_index(['Data'])






tab1 = html.Div([
        html.H3('Divida Líquida'),
        dcc.DatePickerRange(
            id="date-picker",
            start_date=datetime(2001, 12, 1),
            end_date=datetime.today(),
            display_format="DD/MM/YYYY",
            clearable=False,
            number_of_months_shown=2
        ),
        dcc.Graph(
            id='divida'
        #    figure=fig_divida
        ),
        html.H6('Fonte: Banco Central do Brasil')
        ])

tab2 = html.Div([
        html.H3('Índice de atividade'),
        dcc.Graph(
            id='atividade'
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
            min=2003,
            max=2022,
            value=[2003,2022]
            ),
        html.H6('Fonte: Banco Central do Brasil')
        ])

tab3 = html.Div([
            html.H3('PIB'),
            dcc.RadioItems(
                    id='radio',
                    options=[
                             {'label': 'pib mensal', 'value': 'pib_mensal'},
                             {'label': 'pib real', 'value': 'pib_real'},
                    ],
                    value='pib',
                    style={"width": "60%"}
                ),
            dcc.Graph(
                id='pib',
            ),
            html.H6('Fonte: Banco Central do Brasil')
        ])





app.layout = html.Div([
    html.H1('Economic Studio', style={'textAlign': 'center'}),

        html.Div(children='''
        Data, information and forecast.
    ''', style={'textAlign': 'center'}),

    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Dívida', value='tab-1-example-graph'),
        dcc.Tab(label='Atividade BC', value='tab-2-example-graph'),
        dcc.Tab(label='PIB', value='tab-3-example-graph')
    ]),
    html.Div(id='tabs-content-example-graph', children=[tab1,tab2,tab3])

])


#callback tabs
@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
#TABS
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return tab1
    elif tab == 'tab-2-example-graph':
        return tab2
    elif tab == 'tab-3-example-graph':
        return tab3


@app.callback(
    Output('divida', 'figure'),
    [Input('date-picker', 'start_date'),
    Input('date-picker', 'end_date')],
    )
def update_graph(start_date, end_date):
    dff = df.loc[start_date: end_date]
    fig = px.line(dff,  y="Valor",
                    title='Dívida líquida do setor público consolidado.'
            )
    fig.update_layout(transition_duration=500)
    return fig
    
@app.callback(
    Output('atividade','figure'),
    [Input('my-range-slider','value')]
)
def update_graph(years):
    dff2 = df2.loc[years[1]:years[0]]
    #dff2=df[(df2['Data']>=years[0])&(df2['Data']<=years[1])]
    fig2 = px.scatter(dff2, y="Valor",
                    title='Índice de atividade econômica do banco central.')
    fig2.update_layout(transition_duration=500)
    return fig2

@app.callback(
    Output('pib', 'figure'),
    [Input(component_id='radio', component_property='value')]
)
def update_graph(value):
    if value == 'pib_mensal':
        return px.line(dff4, y="pib_mensal", color=px.Constant("pib mensal"))
    else:
        value == 'pib_real'
        return px.line(dff4, y="pib_real", color=px.Constant("pib real"))
    









if __name__ == '__main__':
    app.run_server(debug=True)