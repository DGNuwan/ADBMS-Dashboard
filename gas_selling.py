import pandas as pd
import plotly.graph_objects as go

def create_gas_sales_chart():
    # Sample list data
    daily_sales = [150, 180, 170, 200, 160, 140, 190]  # 7 days
    weekly_sales = [1050, 980, 1120, 990]  # 4 weeks
    monthly_sales = [4200, 4500, 4300, 4600, 4400, 4700]  # 6 months

    # Create DataFrames
    df_daily = pd.DataFrame({'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 'Sales': daily_sales})
    df_weekly = pd.DataFrame({'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'], 'Sales': weekly_sales})
    df_monthly = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 'Sales': monthly_sales})

    # Create figure with daily by default
    fig = go.Figure()

    fig.add_trace(go.Bar(x=df_daily['Day'], y=df_daily['Sales'], name="Daily", visible=True))
    fig.add_trace(go.Bar(x=df_weekly['Week'], y=df_weekly['Sales'], name="Weekly", visible=False))
    fig.add_trace(go.Bar(x=df_monthly['Month'], y=df_monthly['Sales'], name="Monthly", visible=False))

    # Add dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(label="Daily", method="update",
                         args=[{"visible": [True, False, False]},
                               {"title": "Daily Gas Cylinder Sales"}]),
                    dict(label="Weekly", method="update",
                         args=[{"visible": [False, True, False]},
                               {"title": "Weekly Gas Cylinder Sales"}]),
                    dict(label="Monthly", method="update",
                         args=[{"visible": [False, False, True]},
                               {"title": "Monthly Gas Cylinder Sales"}]),
                ]),
                direction="down",
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.15,
                yanchor="top"
            ),
        ],
        title="Daily Gas Cylinder Sales",
        yaxis_title="Cylinders Sold",
        xaxis_title="Time Period",
        height=600
    )

    return fig

