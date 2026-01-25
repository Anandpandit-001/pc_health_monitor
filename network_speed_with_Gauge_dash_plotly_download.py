import psutil
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

last_net_stat = psutil.net_io_counters(pernic=True, nowrap=True)["Wi-Fi"]
def network_download_speed_app():
    # Initialize the Dash app
    app = Dash("download_app",assets_folder='assets_download')

    # Layout of the app
    app.layout = html.Div([
        dcc.Graph(id='live-gauge'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds (1 second)
            n_intervals=0
        )
    ])

    @app.callback(Output('live-gauge', 'figure'),
                  [Input('interval-component', 'n_intervals')])
    def update_gauge(n):
        global last_net_stat

        # Get current stats
        current_net_stat = psutil.net_io_counters(pernic=True, nowrap=True)["Wi-Fi"]

        # Calculate download speed (Change to bytes_sent for upload)
        ds = (current_net_stat.bytes_recv - last_net_stat.bytes_recv) / 1024

        # Update global var
        last_net_stat = current_net_stat

        fig = go.Figure(go.Indicator(
            mode="gauge+number",

            value=ds,
            domain={'x': [0, 1], 'y': [0.15, 1]},
            title={
                   'text': "Download Speed (kB/s)",
                   'font': {'size': 20},
                   'align': 'center'
                   },
            gauge={
                'axis': {'range': [None, 1000]},
                'bar': {'color': "Green"},
                'borderwidth': 2,
            }))
        fig.update_layout(paper_bgcolor="#0e1117", margin=dict(t=5, b=0, l=0, r=0), font={'color': "White", 'family': "Arial"})
        return fig
    return app  # You return the app object here