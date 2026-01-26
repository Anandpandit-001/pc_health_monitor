import psutil
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

def battery_percentage_plotly():
    app = Dash("battery_percentage")

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
        battery = psutil.sensors_battery()
        battery_level = battery.percent

        fig = px.pie(
            values=[battery_level, 100 - battery_level],
            names=["Charged", "Remaining"],
            hole=0.6
        )

        fig.update_traces(
            textinfo="none",
            hoverinfo="none",  # Disables the hover tooltip for a cleaner "gauge" feel
            hole=0.7,  # Makes the ring thinner and more modern
            marker=dict(
                colors=["#00cc00", "#1a1a1a"],  # Uses a sharper green and dark grey
                line=dict(width=0)
            )
        )

        fig.update_layout(
            title=dict(
                text="Battery Percentage",
                y=0.80,  # Positions title slightly lower from the very top edge
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

            annotations=[dict(
                text=f"{battery_level}%",
                x=0.5,
                y=0.5,
                font_size=28,  # Slightly larger text for readability
                font_weight="bold",  # Makes the number pop
                showarrow=False
            )]
        )
        return fig

    return app
