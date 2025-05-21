import pandas as pd
import plotly.express as px

def create_salary_chart():
    salary_data = pd.DataFrame({
        'Job Position': [
            'Junior Developer', 'Mid-Level Developer', 'Senior Developer',
            'Team Lead', 'Tech Architect', 'Engineering Manager'
        ],
        'Average Salary (LKR/month)': [120000, 200000, 300000, 400000, 500000, 600000]
    })
    fig = px.pie(
        salary_data,
        names='Job Position',
        values='Average Salary (LKR/month)',
        title='Software Engineer Salary by Job Position in Sri Lanka'
    )
    fig.update_traces(textinfo='label+percent+value', pull=[0.03]*len(salary_data))
    return fig
