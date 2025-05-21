import pandas as pd
import plotly.express as px

def create_income_chart():
    income_data = pd.DataFrame({
        'Company': [
            'IFS', 'Sysco LABS', 'WSO2', 'MillenniumIT ESP', '99x Technology',
            'CodeGen', 'Zone24x7', 'Virtusa', 'IFS Sri Lanka', 'hSenid'
        ],
        'Annual Income (LKR Millions)': [3200, 2800, 2600, 2400, 2000, 1800, 1700, 1500, 1400, 1300]
    })
    fig = px.bar(
        income_data,
        x='Company',
        y='Annual Income (LKR Millions)',
        title='Annual Income of Leading Sri Lankan Software Companies',
        color='Company',
        labels={'Annual Income (LKR Millions)': 'Income (LKR Millions)'},
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig
