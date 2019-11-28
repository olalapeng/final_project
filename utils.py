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
                "Summary",
                href="/final_project/tap1",
                className="tab",
            ),
            dcc.Link(
                "PLot And Table",
                href="/final_project/tap2",
                className="tab",
            ),
            dcc.Link(
                "tap3",
                href="/final_project/tap3",
                className="tab"
            ),
            dcc.Link(
                "Player Comparision",
                href="/final_project/tap4",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )