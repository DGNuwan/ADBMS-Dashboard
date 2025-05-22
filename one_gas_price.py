import plotly.graph_objects as go

def one_gas_price():
    # Cylinder sizes and their prices
    labels = ['12.5kg', '5kg', '2.5kg']
    values = [4500, 2000, 1100]  # Example prices

    # Define pull-out for each slice (0 = no pull, up to 1 = full pull)
    pull = [0.1, 0.1, 0.1]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        pull=pull,
        marker=dict(line=dict(color='white', width=2)),
        textinfo='label+percent+value',
        hole=0,  # For donut style, set hole=0.4
    )])

    fig.update_layout(
        
        height=600,
        width=600
    )

    return fig
