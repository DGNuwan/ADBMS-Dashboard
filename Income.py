import pandas as pd
import plotly.express as px

def create_income_dashboard(time_value='daily'):
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

    df = dummy_data[time_value]
    fig = px.line(df, x='period', y='income', markers=True,
                  title=f"Income ({time_value.capitalize()})")
    fig.update_layout(xaxis_title="Period", yaxis_title="Income")
    return fig
