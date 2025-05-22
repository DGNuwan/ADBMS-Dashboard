import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

def display_cylinders_sold():
    # Dummy sales data
    dummy_data = [
        {'date': '2025-05-21', 'size': '12kg', 'quantity': 10},
        {'date': '2025-05-21', 'size': '5kg', 'quantity': 7},
        {'date': '2025-05-21', 'size': '2.5kg', 'quantity': 4},

        {'date': '2025-05-20', 'size': '12kg', 'quantity': 12},
        {'date': '2025-05-20', 'size': '5kg', 'quantity': 9},
        {'date': '2025-05-20', 'size': '2.5kg', 'quantity': 5},

        {'date': '2025-05-19', 'size': '12kg', 'quantity': 15},
        {'date': '2025-05-19', 'size': '5kg', 'quantity': 6},
        {'date': '2025-05-19', 'size': '2.5kg', 'quantity': 8},

        {'date': '2025-05-18', 'size': '12kg', 'quantity': 9},
        {'date': '2025-05-18', 'size': '5kg', 'quantity': 10},
        {'date': '2025-05-18', 'size': '2.5kg', 'quantity': 3},

        {'date': '2025-05-17', 'size': '12kg', 'quantity': 14},
        {'date': '2025-05-17', 'size': '5kg', 'quantity': 8},
        {'date': '2025-05-17', 'size': '2.5kg', 'quantity': 6},
    ]

    # Convert to DataFrame
    df = pd.DataFrame(dummy_data)

    # Create Dash app
    app = dash.Dash(__name__)
    app.title = "Shell Gas Cylinder Sales"

    # App layout
    app.layout = html.Div([
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

        dcc.Graph(id='sales-pie-chart')
    ])

    # Callback to update pie chart
    @app.callback(
        Output('sales-pie-chart', 'figure'),
        Input('time-filter', 'value')
    )
    def update_pie_chart(time_filter):
        df['date'] = pd.to_datetime(df['date'])

        # Group data
        resampled = df.groupby([pd.Grouper(key='date', freq=time_filter), 'size'])['quantity'].sum().reset_index()
        latest_date = resampled['date'].max()
        filtered = resampled[resampled['date'] == latest_date]

        fig = px.pie(
            filtered,
            names='size',
            values='quantity',
            title=f'Sales Distribution for {latest_date.strftime("%Y-%m-%d")} ({time_filter})'
        )
        return fig

    return app

# Run app only when file is executed directly
if __name__ == '__main__':
    app = display_cylinders_sold()
    app.run_server(debug=True)
