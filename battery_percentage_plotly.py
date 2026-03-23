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
            hoverinfo="none",  
            hole=0.7,  
            marker=dict(
                colors=["#00cc00", "#1a1a1a"],  
                line=dict(width=0)
            )
        )

        fig.update_layout(
            title=dict(
                text="Battery Percentage",
                y=0.80, 
                x=0.5, 
                xanchor='center',
                yanchor='top'
            ),
            showlegend=False,

           
            margin=dict(t=80, b=20, l=20, r=20),

            
            height=300,

            plot_bgcolor="#0e1117",
            paper_bgcolor="#0e1117",
            font_color="white",

            annotations=[dict(
                text=f"{battery_level}%",
                x=0.5,
                y=0.5,
                font_size=28, 
                font_weight="bold",  
                showarrow=False
            )]
        )
        return fig

    return app
