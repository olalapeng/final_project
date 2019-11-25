import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 4

        #write here



        ],
        className="page",
    )
