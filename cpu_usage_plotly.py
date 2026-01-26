import psutil
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
import plotly.express as px
x_vals = []
y_vals_cpu = []

def cpu_usage():
    # Initialize the Dash app
    app = Dash("cpu_usage",assets_folder='assets_download')

    # Layout of the app
    app.layout = html.Div([
        dcc.Graph(id='graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds (1 second)
            n_intervals=0
        )
    ])

    @app.callback(Output("graph", 'figure'),
                  [Input('interval-component', 'n_intervals')])
    def update_line_chart(n):
        current_time = datetime.now()
        cpu_usage_val = psutil.cpu_percent(interval=0.1)

        x_vals.append(current_time)
        y_vals_cpu.append(cpu_usage_val)

        # Keep last 20
        x_vals[:] = x_vals[-20:]
        y_vals_cpu[:] = y_vals_cpu[-20:]

        df = pd.DataFrame({"Time": x_vals, "Usage": y_vals_cpu})

        # 1. Create the base line plot
        fig = px.line(df, x="Time", y="Usage", title="CPU Usage")

        # 2. Match the Matplotlib 'animate' styling
        fig.update_traces(
            mode="lines",
            line=dict(shape="linear", width=1,color='#7FDBFF')
        )

        fig.update_layout(
            plot_bgcolor='#0e1117',
            paper_bgcolor='#0e1117',
            font_color='white',
            title_x=0.5,
            margin=dict(t=40, b=40, l=40, r=40),

            yaxis=dict(
                title="Usage (%)",
                range=[0, 100],
                fixedrange=True,
                gridcolor='#333333',
                showgrid=True,
                zeroline=True
            ),

            # Simplified X-axis dictionary
            xaxis=dict(
                type="date",
                title="Time",
                tickformat="%H:%M:%S",  # Force the format
                gridcolor='#333333',
                showgrid=True,
                showticklabels=True,  # Explicitly ensure labels are on
            )
        )

        fig.update_xaxes(
                gridwidth=0.5,
                griddash='dash'
        )

        fig.update_yaxes(
                gridwidth=0.5,
                griddash='dash',
                range=[0, 100],
                tickmode="linear",
                tick0=0,
                dtick=20
        )

        return fig
    return app  # You return the app object here