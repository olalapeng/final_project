import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
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
                                        ["Plot1"], className="subtitle padded"
                                    ),
                                    # plot here example

                                    # dcc.Graph(
                                    #     id='example-graph5',
                                    #     figure={
                                    #         'data': [
                                    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar',
                                    #              'name': u'Montréal'},
                                    #         ],
                                    #         'layout': {
                                    #             'title': 'Dash Data Visualization'
                                    #         }
                                    #     }
                                    # )

                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["plot2"],
                                        className="subtitle padded",
                                    ),

                                    # Scatter plot of player's salaries
                                    dcc.Graph(
                                        id='graph-scatter',
                                        className='my_graph',
                                        figure={
                                            'data': [{
                                                'x': df['Name'],
                                                'y': df['Salary'],
                                                'type': 'scatter',
                                                'mode': 'markers',

                                            }],
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
                                    html.H6("plot3", className="subtitle padded"),
                                    # plot here example

                                    # dcc.Graph(
                                    #     id='example-graph7',
                                    #     figure={
                                    #         'data': [
                                    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar',
                                    #              'name': u'Montréal'},
                                    #         ],
                                    #         'layout': {
                                    #             'title': 'Dash Data Visualization'
                                    #         }
                                    #     }
                                    # )

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
                                            # table here example

                                            # make_dash_table
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),

                    # end
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )

