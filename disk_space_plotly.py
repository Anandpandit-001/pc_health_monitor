import psutil
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

def disk_space_plotly():
    app = Dash("disk_space_plotly")

    app.layout = html.Div([
        dcc.Graph(id='graph'),
        dcc.Interval(
            id='interval-component',
            interval=1000,
            n_intervals=0
        )
    ])

    @app.callback(Output("graph", "figure"),
                  Input("interval-component", "n_intervals"))
    def generate_chart(n):
        usage = psutil.disk_usage('/')
        used_percent = usage.percent
        total_gb = round(usage.total / (1024 ** 3), 2)
        used_gb = usage.used / (1024 ** 3)

        fig = px.pie(
            values=[used_percent, 100 - used_percent],
            names=["Used", "Free"],
            hole=0.7
        )

        fig.update_traces(
            #textinfo="none",
            hoverinfo="none",  # Disables the hover tooltip for a cleaner "gauge" feel
            hole=0.7,  # Makes the ring thinner and more modern
            marker=dict(
                colors=["#E74C3C", "#1a1a1a"],  # Uses a sharper green and dark grey
                line=dict(width=0)
            )
        )

        fig.update_layout(
            title=dict(
                text=f"Disk Usage<br><span style='font-size: 14px; color: #aaaaaa'>Total Capacity: {total_gb} GB</span>",
                y=0.85,  # Positions title slightly lower from the very top edge
                x=0.5,  # Centers the title horizontally
                xanchor='center',
                yanchor='top'
            ),
            showlegend=False,

            # FIX: Increase top margin to 40 or 50 to give the title room
            margin=dict(t=80, b=20, l=20, r=20),

            # FIX: Set a fixed height so it acts like a widget, not a full-page plot
            height=300,

            plot_bgcolor="#0e1117",
            paper_bgcolor="#0e1117",
            font_color="white",

        )
        return fig

    return app
