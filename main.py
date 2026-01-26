from disk_space_plotly import *
from battery_percentage_plotly import *
from cpu_usage_plotly import *
from ram_usage_plotly import *
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

def run_app3():
    app3 = cpu_usage()
    app3.run(port=8052, debug=False, use_reloader=False)

def run_app4():
    app4 = ram_usage()
    app4.run(port=8053, debug=False, use_reloader=False)

def run_app5():
    app5 = battery_percentage_plotly()
    app5.run(port=8054, debug=False, use_reloader=False)

def run_app6():
    app6 = disk_space_plotly()
    app6.run(port=8055, debug=False, use_reloader=False)


row2_col0 , row2_col1, row2_col2 = st.columns([1,3,1])

with row2_col2:
    with st.container():
        # 1. Reduce height to match the actual content
        # If your Gauge is square, 350-450 is usually perfect.
        st.components.v1.iframe("http://127.0.0.1:8051", height=350, scrolling=False)

        # 2. Add a negative margin to pull the second one up (Optional hack)
        st.markdown('<div style="margin-top: -200px;"></div>', unsafe_allow_html=True)

        st.components.v1.iframe("http://127.0.0.1:8050", height=350, scrolling=False)

with row2_col1:
    with st.container():
        st.components.v1.iframe("http://127.0.0.1:8052", height=350, scrolling=False)
        st.markdown('<div style="margin-top: -200px;"></div>', unsafe_allow_html=True)
        st.components.v1.iframe("http://127.0.0.1:8053", height=350, scrolling=False)
        st.markdown('<div style="margin-top: -200px;"></div>', unsafe_allow_html=True)

with row2_col0:
    with st.container():
        st.components.v1.iframe("http://127.0.0.1:8054", height=350, scrolling=False)
        st.markdown('<div style="margin-top: -200px;"></div>', unsafe_allow_html=True)
        st.components.v1.iframe("http://127.0.0.1:8055", height=350, scrolling=False)
        st.markdown('<div style="margin-top: -200px;"></div>', unsafe_allow_html=True)

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
    p1 = multiprocessing.Process(target=run_app1)
    p2 = multiprocessing.Process(target=run_app2)
    p3 = multiprocessing.Process(target=run_app3)
    p4 = multiprocessing.Process(target=run_app4)
    p5 = multiprocessing.Process(target=run_app5)
    p6 = multiprocessing.Process(target=run_app6)
    # Start processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    # Join processes to keep them running
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()