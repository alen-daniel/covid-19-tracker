import dash_bootstrap_components as dbc


def create_layout():
    return dbc.Alert(
        "Hello, World!", className="m-5"
    )
