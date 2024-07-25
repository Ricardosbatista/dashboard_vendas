import dash
import dash_bootstrap_components as dbc
from dash import html, dcc , Input, Output
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import calendar
import locale

#Importando Dados________________________________

df = pd.read_csv('bases/dados_competos.csv')


#Criando App ________________________________

app = dash.Dash(__name__)




#Montando Layout_________________________________

linha_cabecalho = html.Div([
 html.Div([
     dcc.Dropdown(
            id='dropdown_clientes',
            options=df['Cliente'].unique(),
            placeholder='Clientes',
            style={'font-family': 'Century Gothic'}
                            )  
                            ], style = {'width': '25%'})])

app.layout = html.Div([linha_cabecalho])













#Callbacks_________________________________



#Subindo Servidor_________________________________

if __name__ == '__main__' : app.run_server(debug=True)