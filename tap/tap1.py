import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header

import pandas as pd
import pathlib



def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("NBA Summary"),
                                    html.Br([]),
                                    html.P(
                                        # summary here
                                        "The National Basketball Association (NBA) is a men's professional basketball league in North America, composed of 30 teams (29 in the United States and 1 in Canada). It is one of the four major professional sports leagues in the United States and Canada, and is widely considered to be the premier men's professional basketball league in the world. The league was founded in New York City on June 6, 1946, as the Basketball Association of America (BAA).[1][2] It changed its name to the National Basketball Association on August 3, 1949, after merging with the competing National Basketball League (NBL). The NBA's regular season runs from October to April, with each team playing 82 games. Its playoffs extend into June. NBA players are the world's best paid athletes by average annual salary per player.[3][4]. The NBA is an active member of USA Basketball (USAB),[5] which is recognized by FIBA (also known as the International Basketball Federation) as the national governing body for basketball in the United States. The league's several international as well as individual team offices are directed out of its head offices in Midtown Manhattan, while its NBA Entertainment and NBA TV studios are directed out of offices located in Secaucus, New Jersey.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Br([]),
                                    html.H6(
                                        ["2020 Season"],
                                        className="subtitle tiny-header padded",
                                    ),
                                    html.Div(
                                        [
                                            html.Img(
                                                src='https://images.wallpaperscraft.com/image/nba_national_basketball_association_basketball_81187_1920x1080.jpg',
                                                style={
                                                    'height': '100%',
                                                    'width': '100%',
                                                    'float': 'right',
                                                    'position': 'relative',
                                                    'padding-top': 0,
                                                    'padding-right': 0
                                                })
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
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
