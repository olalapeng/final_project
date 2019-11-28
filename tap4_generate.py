
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc

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



def get_tab4():
    tap4 = html.Div(
        [

            # page 4
            html.Div([
                # create the first dropdown
                html.Label('Player One'),
                dcc.Dropdown(
                    id="player1",
                    options=[{'label': i, 'value': df1.index(i)} for i in df1],
                    value=0,
                    style={'width': '300px'}
                )
            ], style={'padding': 20}),
            html.Div([
                # create the second dropdown
                html.Label('Player Two'),
                dcc.Dropdown(
                    id="player2",
                    options=[{'label': i, 'value': df1.index(i)} for i in df1],
                    value=1,
                    style={'width': '300px'}
                )
            ],
                style={'padding': 20}),
            html.Div([
                # design the displayed table
                dash_table.DataTable(
                    id='table',
                    # styling the table and cells
                    style_table={
                        'border': 'thin lightgrey solid'
                    },
                    style_cell={
                        'height': 'auto',
                        'minWidth': '0px', 'maxWidth': '150px',
                        'whiteSpace': 'normal'
                    },
                    # highlight win rate
                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(248, 248, 248)'
                        },
                        {
                            'if': {'column_id': 'win_rate'},
                            'backgroundColor': 'steelblue',
                            'color': 'white',
                        }
                    ],
                    # styling header
                    style_header={
                        'backgroundColor': 'rgb(230, 230, 230)',
                        'fontWeight': 'bold'
                    },
                    columns=[{"name": i, "id": i} for i in df3.columns],
                    data=data1.to_dict('records')
                )
            ],
                style={'padding': 20}),
            dcc.Graph(
                id='plot1'
            ),
            dcc.Graph(
                id='plot2'
            ),
            dcc.Graph(
                id='plot3'
            )
        ],
        className="page",
    )
    return tap4