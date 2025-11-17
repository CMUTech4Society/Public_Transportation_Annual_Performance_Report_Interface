import plotly.express as px
import pandas as pd

def graph(PlotStruct):
    df = pd.merge(PlotStruct.x_axis.dataframe, PlotStruct.y_axis.dataframe, on=['department', 'year'], suffixes=('_x', '_y'))
    fig = px.scatter(
        df,
        x=PlotStruct.x_axis.label,
        y=PlotStruct.y_axis.label,
        color='department',
        title=f'{PlotStruct.y_axis.label} vs {PlotStruct.x_axis.label} by Department',
        labels={
            PlotStruct.x_axis.label: PlotStruct.x_axis.label,
            PlotStruct.y_axis.label: PlotStruct.y_axis.label}
    )
    fig.show()