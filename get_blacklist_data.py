import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Function to get blacklist data
def get_blacklist_data():
    return {
        'Type': ['Supplier', 'Customer'],
        'Count': [3, 7]  
    }

# Function that returns the Plotly donut chart figure
def create_blacklist_donut_chart_figure():
    data = get_blacklist_data()
    df = pd.DataFrame(data)

    fig = px.pie(
        df,
        values='Count',
        names='Type',
        hole=0.5,
        title="Blacklisted Suppliers vs Customers",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig.update_traces(textinfo='percent+label')
    fig.update_layout(margin=dict(t=40, b=20, l=20, r=20), height=400)

    return fig

# Optional Dash app to display the figure
def run_app():
    fig = create_blacklist_donut_chart_figure()
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H2("Blacklist Donut Chart", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
    app.run_server(debug=True)

# Run the app if the script is executed directly
if __name__ == '__main__':
    run_app()
