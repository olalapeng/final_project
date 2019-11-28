import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from tap4_generate import get_tab4
from utils import Header
import pandas as pd
import pathlib


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 4

            get_tab4()



        ],
        className="page",
    )
