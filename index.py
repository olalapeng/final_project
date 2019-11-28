# -*- coding: utf-8 -*-
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from tap import (
    tap1,
    tap2,
    tap3,
    tap4,
)


# read data
df = pd.read_excel('https://s3.amazonaws.com/programmingforanalytics/NBA_data.xlsx')
# create list for dropdown
df1 = list(df.iloc[:, 0])

# wrangle data for displayed table
df2 = df
# create two new columns
df2['win_rate'] = round(df2['Wins'] / df2['Games_played'], 2)
df2['3P_goal_rate'] = round(df2['3P_made_per_game'] / df2['3P_attempted_per_game'], 2)
# extract required data
df3 = df2.iloc[:, [0, 1, 2, 3, 7, 10, 14, 16, 17, 18]]
# adjust the order of columns
col_name = df3.columns.tolist()
col_name.insert(5, col_name.pop(col_name.index('win_rate')))
col_name.insert(7, col_name.pop(col_name.index('3P_goal_rate')))
df3 = df3.loc[:, col_name]
# transfer data into other type
df3['Field_goal_percentage'] = round(df3['Field_goal_percentage'] / 100, 2)
# create initial data frame for dispalyed data
data1 = df3.iloc[[0, 1], :]

# wrangle data for draw bar chart
df4 = df.loc[:, ['Name', 'Field_goals_made_per_game', '3P_made_per_game']]
#data2 = df4.iloc[[0, 1], :]
goal = ['field_goal', '3P_made']


app = dash.Dash(__name__,suppress_callback_exceptions=True)

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/final_project/tap1":
        return tap1.create_layout(app)
    elif pathname == "/final_project/tap2":
        return tap2.create_layout(app)
    elif pathname == "/final_project/tap3":
        return tap3.create_layout(app)
    elif pathname == "/final_project/tap4":
        return tap4.create_layout(app)
    else:
        return tap1.create_layout(app)




# call back table
@app.callback(
    Output('table', 'data'),
    [Input('player1', 'value'),
     Input('player2', 'value')]
)
def create_table(player1_value, player2_value):
    return df3.iloc[[player1_value, player2_value], :].to_dict('records')


# call back bar chart
@app.callback(
    Output('plot1', 'figure'),
    [Input('player1', 'value'),
     Input('player2', 'value')]
)
def create_goal_graph(player1_value, player2_value):
    data2 = df4.iloc[[player1_value, player2_value], :]
    fig = go.Figure(data=[
        go.Bar(x=goal, y=[data2.iloc[0, 1], data2.iloc[0, 2]], name=data2.iloc[0, 0], marker_color='indianred'),
        go.Bar(x=goal, y=[data2.iloc[1, 1], data2.iloc[1, 2]], name=data2.iloc[1, 0], marker_color='lightsalmon')
    ])
    fig.update_layout(
        title={'text': '<b>Goal Comparison<b>',
               'y': 0.9,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        xaxis=dict(title='Goal types'),
        yaxis=dict(title='Goal numbers'),
        barmode='group'
    )
    return fig


# callback the pie chart
@app.callback(
    Output('plot2', 'figure'),
    [Input('player1', 'value'),
     Input('player2', 'value')]
)
def creat_win_graph(player1_value, player2_value):
    data3 = df.iloc[[player1_value, player2_value], [0, 4, 5]]
    labels = ['win', 'loss']
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(
        labels=labels,
        values=[data3.iloc[0, 1], data3.iloc[0, 2]],
        name=data3.iloc[0, 0]
    ), 1, 1)
    fig.add_trace(
        go.Pie(
            labels=labels,
            values=[data3.iloc[1, 1], data3.iloc[1, 2]],
            name=data3.iloc[1, 0]
        ), 1, 2)
    fig.update_traces(hole=.3, hoverinfo="label+percent+name")

    fig.update_layout(
        title={'text': '<b>win rate<b>',
               'y': 0.9,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'},
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=data3.iloc[0, 0], x=0.18, y=1.1, font_size=15, showarrow=False),
                     dict(text=data3.iloc[1, 0], x=0.80, y=1.1, font_size=15, showarrow=False)])
    return fig


# callback the scatter chart
@app.callback(
    Output('plot3', 'figure'),
    [Input('player1', 'value'),
     Input('player2', 'value')]
)
def creat_salary_graph(player1_value, player2_value):
    data4 = df.iloc[[player1_value, player2_value], :].loc[:, ['Name', 'Salary']]
    fig = px.scatter(data4, x="Name", y="Salary", size="Salary", color="Name",
                     size_max=60)
    fig.update_layout(
        title={'text': '<b>Salary Comparison<b>',
               'y': 1,
               'x': 0.5,
               'xanchor': 'center',
               'yanchor': 'top'}
    )

    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
