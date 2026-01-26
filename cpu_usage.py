import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

def cpu_usage_anim():
    fig, ax = plt.subplots( figsize=(12, 5))
    x_vals = []
    y_vals_cpu = []

    def animate(i):
        current_time = datetime.now().strftime("%H:%M:%S")
        cpu_usage = psutil.cpu_percent(interval=None)
        x_vals.append(current_time)
        y_vals_cpu.append(cpu_usage)

        x_vals[:] = x_vals[-20:]
        y_vals_cpu[:] = y_vals_cpu[-20:]

        ax.clear()
        ax.plot(x_vals, y_vals_cpu, linewidth=1, color='skyblue')
        ax.set_title("CPU Usage")
        ax.set_ylabel("Usage (%)")
        ax.set_ylim(0, 100)
        ax.grid(True)
        ax.grid(color='#333333', linestyle='--', linewidth=0.5)
        ax.tick_params(axis='x', rotation=45)
        ax.set_facecolor('#0e1117')

        plt.tight_layout()

    ani = FuncAnimation(fig, animate, interval=1000,cache_frame_data=False)

    return fig, ani


