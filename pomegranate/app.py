"""Web application for pomegranate."""

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import Dash, dcc, html, Input, Output
from tabs.seeMotif import motifVisualisationTab

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

sidebar = html.Div(
    id="sidebar",
    children= [
        html.H3("Find a protein"),
        html.Hr(),
        html.P(
            "A placeholder for searching a protein of interest"
        ),
        html.Button("Button")
    ]
)

content = html.Div(
    children= [
        dcc.Tabs(id="tab-container", value='single-motif-view', children=[
            dcc.Tab(label='Visualisation', value='single-motif-view'),
            dcc.Tab(label='Compare Motifs', value='multi-motif-view'),
            dcc.Tab(label='Proteome View', value='clustering'),
            dcc.Tab(label='Help', value='documentation'),
        ]),
        html.Div(id='tabs-content'),
    ]
)

app.layout = html.Div([
	html.H1('POMEGRANATE'),
    html.H2('PhOsphosite Motif Explorer -- GRAph Network Abstraction Through Embeddings'),
    html.Div(id="content-grid", children=[sidebar,content])
    
])

@app.callback(Output('tabs-content', 'children'),
              Input('tab-container', 'value'))
def render_content(tab):
    if tab == 'single-motif-view':
        return motifVisualisationTab()
    elif tab == 'multi-motif-view':
        return html.Div([
            html.H3('Placeholder graph'),
            dcc.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'clustering':
        return html.H3('Look how cool our clusters are')
    elif tab == 'documentation':
        return html.H3('Documentation')


if __name__ == '__main__':
    app.run_server(debug=True)
