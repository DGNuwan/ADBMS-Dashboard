import plotly.express as px

def show_empty_cylinder_stock_figure():
    data = dict(
        number=[50, 30, 20],
        stage=["12.5kg", "5kg", "2.5kg"]
    )
    fig = px.funnel(data, x='number', y='stage')
    return fig
