# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from tap import (
    tap1,
    tap2,
    tap3,
    tap4,
)

app = dash.Dash(__name__)

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


if __name__ == "__main__":
    app.run_server(debug=True)
