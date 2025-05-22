import pandas as pd
import plotly.express as px

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

df = pd.DataFrame(dummy_data)
df['date'] = pd.to_datetime(df['date'])

def get_cylinder_sales_figure(time_filter):
    """
    Returns the pie chart figure for cylinder sales based on the given time filter.
    :param time_filter: str ('D' for Daily, 'W' for Weekly, 'M' for Monthly)
    :return: plotly pie chart figure
    """
    resampled = df.groupby([pd.Grouper(key='date', freq=time_filter), 'size'])['quantity'].sum().reset_index()
    latest_date = resampled['date'].max()
    filtered = resampled[resampled['date'] == latest_date]

    fig = px.pie(
        filtered,
        height=600,
        names='size',
        values='quantity',
        title=f"Sales Distribution for {latest_date.strftime('%Y-%m-%d')} ({time_filter})"
    )
    return fig
