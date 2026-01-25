import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

def ram_usage_anim():
    fig, ax = plt.subplots( figsize=(12, 5))
    x_vals = []
    y_vals_ram = []

    def animate(i):
        current_time = datetime.now().strftime("%H:%M:%S")
        mem_info = psutil.virtual_memory()
        ram_usage = mem_info.percent
        x_vals.append(current_time)
        y_vals_ram.append(ram_usage)

        x_vals[:] = x_vals[-20:]
        y_vals_ram[:] = y_vals_ram[-20:]

        ax.clear()
        ax.plot(x_vals, y_vals_ram, color='green', linewidth=1)
        ax.set_title("RAM Usage")
        ax.set_ylabel("Usage (%)")
        ax.set_ylim(0, 100)
        ax.grid(True)
        ax.grid(color='#333333', linestyle='--', linewidth=0.5)
        ax.tick_params(axis='x', rotation=45)
        ax.set_facecolor('#0e1117')

        plt.tight_layout()

        plt.tight_layout()

    ani = FuncAnimation(fig, animate, interval=1000)

    return fig, ani


