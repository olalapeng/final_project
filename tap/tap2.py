import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, generate_table
import pandas as pd
import pathlib


df = pd.read_excel('https://s3.amazonaws.com/programmingforanalytics/NBA_data.xlsx')

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Team Location"], className="subtitle padded"
                                    ),
                                    # scatter geo plot of nba teams' location
                                    dcc.Graph(
                                        id='scatter_geo',
                                        className='my_graph',
                                        figure={
                                            'data': [{
                                                # Setting coordinate and description for each team
                                                'lon': [-98.37, -97.52, -87.90, -75.16, -118.24, -122.27, -79.38,
                                                        -112.07, -90.07, -122.675, -80.84, -77.04, -83.05, -93.265, -71,
                                                        -111.89, -87.63],
                                                'lat': [29.76, 35.47, 43, 39.95, 34.05, 37.8, 43.65, 33.45, 29.95, 45.5,
                                                        35.23, 38.91, 42.33, 44.98, 42.37, 40.76, 41.88],
                                                'text': ['HOU, Houston Rocket', 'OKC, Oklahoma Thunder',
                                                         'MIL, Milwaukee Bucks,', 'PHI, Philadelphia 76ers',
                                                         'LAL, Los Angeles Lakers'
                                                    , 'GSW, Golden State Warriors', 'TOR, Toronto Raptors',
                                                         'PHX, Phoenix Suns', 'NOP, New Orleans Pelicans',
                                                         'POR, Portland Trail Blazers',
                                                         'CHA, Charlotte Hornets', 'WAS, Washington Wizards',
                                                         'DET, Detroit Pistons', 'MIN, Minnesota Timberwolves'
                                                    , 'BOS, Boston Celtics', 'UTA, Utah Jazz', 'CHI, Chicago Bulls'],
                                                'type': 'scattergeo',
                                                'mode': 'markers',
                                                "marker": {
                                                    "size": 10,
                                                    "opacity": 10.0,
                                                },

                                            }],
                                            'layout': {
                                                'title': 'NBA teams location',
                                                'height': 600,
                                                'yaxis': {'hoverformat': '.2%'},
                                                'margin': {'l': 35, 'r': 35, 't': 50, 'b': 80},
                                                "geo": {
                                                    "scope": "usa",
                                                    'showframe': True,
                                                    'showcoastlines': True,
                                                },
                                                "colorbar": True,

                                            }
                                        },
                                        config={
                                            'displayModeBar': True
                                        }

                                    )


                                ],
                                className="six columns",
                            ),

                            html.Div(
                                [
                                    html.H6(
                                        ["Salary Distribution"],
                                        className="subtitle padded",
                                    ),

                                    # Scatter plot of player's salaries
                                    dcc.Graph(
                                        id='graph-scatter',
                                        className='my_graph',
                                        figure={
                                            'data': [{
                                                # Name of each player on x axis and their corresponding salary on y axis
                                                'x': df['Name'],
                                                'y': df['Salary'],
                                                'type': 'scatter',
                                                'mode': 'markers',

                                            }],
                                            # Description of the plot
                                            'layout': {
                                                'title': 'Distribution of NBA players salaries',
                                                'height': 600,
                                                'yaxis': {'hoverformat': '.2%'},
                                                'margin': {'l': 35, 'r': 35, 't': 50, 'b': 80},

                                            }
                                        },
                                        config={
                                            'displayModeBar': False
                                        }

                                    )

                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("LeBron James choose Lakers", className="subtitle padded"),
                                    # Plot image from web for a overall sleek design
                                    html.Img(
                                        src='https://i.pinimg.com/originals/9f/15/98/9f15989577e13555c75031ee72d9c9a5.jpg',
                                        style={
                                            'height': '100%',
                                            'width': '100%',
                                            'float': 'right',
                                            'position': 'relative',
                                            'padding-top': 0,
                                            'padding-right': 0
                                        })


                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "plot4"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            generate_table(df)
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),

                  #end
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )



