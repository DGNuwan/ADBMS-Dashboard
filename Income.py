import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

def create_income_dashboard():
    # Dummy data
    dummy_data = {
        'daily': pd.DataFrame({
            'period': pd.date_range(start='2025-05-01', periods=10, freq='D'),
            'income': [150, 200, 180, 220, 210, 190, 205, 215, 230, 225]
        }),
        'weekly': pd.DataFrame({
            'period': ['2025-W18', '2025-W19', '2025-W20', '2025-W21'],
            'income': [1200, 1350, 1250, 1400]
        }),
        'monthly': pd.DataFrame({
            'period': ['2025-02', '2025-03', '2025-04', '2025-05'],
            'income': [4800, 5200, 5000, 5600]
        })
    }

    # Initialize app
    app = dash.Dash(__name__)
    app.title = "Income Dashboard"

    # Layout
    app.layout = html.Div([
        html.H1("Income Over Time (Dummy Data)", style={'textAlign': 'center'}),

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
    ])

    # Callback
    @app.callback(
        Output('line-chart', 'figure'),
        Input('time-selector', 'value')
    )
    def update_chart(time_value):
        df = dummy_data[time_value]
        fig = px.line(df, x='period', y='income', markers=True,
                      title=f"Income ({time_value.capitalize()})")
        fig.update_layout(xaxis_title="Period", yaxis_title="Income")
        return fig

    # Run server
    app.run_server(debug=True)

# Call the function if this script is run directly
# if __name__ == '__main__':
#     create_income_dashboard()
