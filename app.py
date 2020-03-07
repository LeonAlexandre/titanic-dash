import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_daq as daq

import sys
import pathlib
import copy

import numpy as np
import pandas as pd

app = dash.Dash(
    __name__
    )
server = app.server

# Load Data from storage
data_path = (pathlib.Path(__file__).parent).joinpath("data").resolve()
df = pd.read_csv(data_path.joinpath("train.csv"), low_memory=False)



# Create common layout for boxes

# Table style
table_style = dict(
    overflowY='scroll'
)
cell_style = dict(
    overflow='hidden',
    textOverflow='ellipsis',
    maxWidth=0,
)


#Copy using the copy lib layout_pie = copy.deepcopy(layout)

def serve_layout():
    main_layout = html.Div([
        html.H1(children='Blank Page'),
        dash_table.DataTable(
                        id='table1',
                        columns=[{"name": i, "id": i, "selectable": True} for i in df_no_heroes.columns],
                        data=df_no_heroes.to_dict('records'),
                        row_selectable="single",
                        selected_rows=[0],
                        style_table=table_style,
                        style_cell=cell_style,
    ])

    return main_layout

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)