import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [

            html.Div(
                [
                    html.Div(
                        [html.H5("National Basketball Association Dash Web")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            html.A(
                                html.Button("Learn More", id="learn-more-button"),
                                href="https://www.nba.com/",
                            ),
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header

# tap click to
def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "tap1",
                href="/final_project/tap1",
                className="tab",
            ),
            dcc.Link(
                "tap2",
                href="/final_project/tap2",
                className="tab",
            ),
            dcc.Link(
                "tap3",
                href="/final_project/tap3",
                className="tab"
            ),
            dcc.Link(
                "tap4",
                href="/final_project/tap4",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
