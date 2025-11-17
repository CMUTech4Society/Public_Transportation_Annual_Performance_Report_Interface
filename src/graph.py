import plotly.express as px
import pandas as pd

def graph(PlotStruct):
    df = pd.merge(PlotStruct.x_axis.dataframe, PlotStruct.y_axis.dataframe, on=['department', 'year'], suffixes=('_x', '_y'))
    fig = px.scatter(
        df,
        x=f'{PlotStruct.x_axis.label}_x',
        y=f'{PlotStruct.y_axis.label}_y',
        color='department',
        title=f'{PlotStruct.y_axis.label} vs {PlotStruct.x_axis.label} by Department',
        labels={
            f'{PlotStruct.x_axis.label}_x': PlotStruct.x_axis.label,
            f'{PlotStruct.y_axis.label}_y': PlotStruct.y_axis.label}
    )
    fig.show()