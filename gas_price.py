import plotly.graph_objects as go
from plotly.subplots import make_subplots

def gas_price():
    # Sample data
    suppliers = ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D', 'Supplier E']
    prices_12_5kg = [4500, 4600, 4400, 4550, 4700]
    prices_5kg = [2000, 2100, 1950, 2050, 2150]
    prices_2_5kg = [1100, 1150, 1080, 1120, 1180]

    # Create subplot with 1 row, 3 columns
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=("12.5kg Gas Prices", "5kg Gas Prices", "2.5kg Gas Prices")
    )

    # Add bar charts to each subplot
    fig.add_trace(go.Bar(x=suppliers, y=prices_12_5kg, name='12.5kg', marker_color='tomato'), row=1, col=1)
    fig.add_trace(go.Bar(x=suppliers, y=prices_5kg, name='5kg', marker_color='dodgerblue'), row=1, col=2)
    fig.add_trace(go.Bar(x=suppliers, y=prices_2_5kg, name='2.5kg', marker_color='seagreen'), row=1, col=3)

    # Update layout and styling
    fig.update_layout(
        #title_text="Gas Prices by Supplier",
        showlegend=False,
        height=500,
        width=1500,
        margin=dict(t=40, b=20, l=20, r=20)
    )

    return fig
