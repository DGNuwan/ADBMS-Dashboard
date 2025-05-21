from dash import Dash, html, dcc
from test import create_salary_chart  # Import the function from charts.py
from test2 import create_income_chart


app = Dash(__name__)

app.layout = html.Div([
    html.H2("Software Engineer Salary in Sri Lanka", style={'textAlign': 'center'}),
    dcc.Graph(figure=create_salary_chart()),  # Call the imported function here

    dcc.Graph(figure=create_income_chart()),
])

if __name__ == '__main__':
    app.run(debug=True)

