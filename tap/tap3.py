import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header
import pandas as pd
import pathlib




def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Plot1"], className="subtitle padded")],
                                className="twelve columns",
                            ),
                            # plot here example

                            # dcc.Graph(
                            #     id='example-graph',
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
                        className="rows",
                    ),
                    # Row 2
                    html.Br([]),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["plot2"],
                                        className="subtitle padded",
                                    ),
                                    # plot here example

                                    # dcc.Graph(
                                    #     id='example-graph2',
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
                                className=" twelve columns",
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
                                        ["plot3"],
                                        className="subtitle padded",
                                    ),
                                    # plot here example

                                    # dcc.Graph(
                                    #     id='example-graph3',
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
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
