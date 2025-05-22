from dash import Dash, html, dcc, Input, Output
from cylinders_sold import get_cylinder_sales_figure, dummy_data
from gas_selling import create_gas_sales_chart
from Income import create_income_dashboard
import pandas as pd

df = pd.DataFrame(dummy_data)

app = Dash(__name__)

app.layout = html.Div([

    # First Div: Dropdown + Line chart
    html.Div([
        html.H1("Income Dashboard Example", style={'textAlign': 'center'}),

        dcc.Dropdown(
            id='time-selector',
            options=[
                {'label': 'Daily', 'value': 'daily'},
                {'label': 'Weekly', 'value': 'weekly'},
                {'label': 'Monthly', 'value': 'monthly'},
            ],
            value='daily',
            clearable=False,
            style={'width': '50%', 'margin': 'auto'}
        ),

        dcc.Graph(id='line-chart')
    ]),

    # Second Div: Dropdown + Cylinder Sales Pie Chart
    html.Div([
        html.H2("Shell Gas Cylinder Sales", style={'textAlign': 'center'}),

        dcc.Dropdown(
            id='time-filter',
            options=[
                {'label': 'Daily', 'value': 'D'},
                {'label': 'Weekly', 'value': 'W'},
                {'label': 'Monthly', 'value': 'M'}
            ],
            value='D',
            clearable=False,
            style={'width': '200px', 'margin': '0 auto'}
        ),

        dcc.Graph(id='cylinders-pie-chart')  # <-- dynamic graph here
    ]),

    html.Div([

          html.H2("Shell Gas Cylinder Sales", style={'textAlign': 'center'}),

           dcc.Graph(figure=create_gas_sales_chart()),

       ]),



   

])

# Callback for income dashboard line chart
@app.callback(
    Output('line-chart', 'figure'),
    Input('time-selector', 'value')
)
def update_line_chart(selected_time):
    return create_income_dashboard(selected_time)


# Callback to update cylinder sales pie chart dynamically
@app.callback(
    Output('cylinders-pie-chart', 'figure'),
    Input('time-filter', 'value')
)
def update_cylinder_sales_pie(time_filter):
    return get_cylinder_sales_figure(time_filter)


if __name__ == '__main__':
    app.run(debug=True)
