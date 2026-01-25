from disk_space_calculation import *
from battery_percentage import *
from cpu_usage import *
from ram_usage import *
from network_speed_with_Gauge_dash_plotly_upload import *
from network_speed_with_Gauge_dash_plotly_download import *
import multiprocessing
import streamlit as st

# Define App 1
def run_app1():
    app1 = network_upload_speed_app()
    app1.run(port=8050, debug=False, use_reloader=False)

# Define App 2
def run_app2():
    app2 = network_download_speed_app()
    app2.run(port=8051, debug=False, use_reloader=False)

# This embeds your Dash app into the Streamlit page

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    with st.container(border=True):
        # 1. Reduce height to match the actual content
        # If your Gauge is square, 350-450 is usually perfect.
        st.components.v1.iframe("http://127.0.0.1:8051", height=350, scrolling=False)

        # 2. Add a negative margin to pull the second one up (Optional hack)
        st.markdown('<div style="margin-top: -200px;"></div>', unsafe_allow_html=True)

        st.components.v1.iframe("http://127.0.0.1:8050", height=350, scrolling=False)

# Place this CSS at the top of your script (not inside the loop)
st.markdown("""
    <style>
    /* This targets the spacing between elements inside containers */
    div[data-testid="stVerticalBlock"] > div.element-container {
        margin-bottom: 0rem;
        margin-top: 0rem;/* Reduces the default Streamlit gap */
    }
    iframe {
        display: block; /* Removes tiny default inline-block spacing */
    }
    </style>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    fig1, cpu_usage_anim = cpu_usage_anim()
    fig2, disk_usage_anim = create_disk_usage_anim()
    fig3, battery_percentage_anim = battery_percentage_anim()
    fig4, ram_usage_anim = ram_usage_anim()
    plt.show()
    # Create processes
    p1 = multiprocessing.Process(target=run_app1)
    p2 = multiprocessing.Process(target=run_app2)
    # Start processes
    p1.start()
    p2.start()
    # Join processes to keep them running
    p1.join()
    p2.join()

