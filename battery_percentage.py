import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def battery_percentage_anim():
    fig1, ax = plt.subplots(figsize=(4, 4))
    colors1 = ['#4CAF50', (0, 0, 0, 0)]

    def animate(i):
        battery = psutil.sensors_battery()
        battery_level = battery.percent
        values = [battery_level, 100 - battery_level]

        ax.clear()
        wedges, texts, autotexts = ax.pie(
            values,
            colors=colors1,
            startangle=90,
            autopct='%.0f%%',
            textprops=dict(color="#0e1117"),
            counterclock=False,
            wedgeprops={'width': 0.3, 'edgecolor': 'black', 'linewidth': 1}
            # This creates the donut hole
        )

        ax.axis('equal')

        ax.set_title(f"Battery", color='white', ha='center', va='center', fontsize=14, pad=20)
        ax.text(0, 0, f"{battery_level}% \nCharged",
                ha='center', va='center', color='white',
                fontsize=16, fontweight='bold')
        fig1.set_facecolor('#0e1117')

    ani = FuncAnimation(fig1,animate, interval=1000,cache_frame_data=False)

    return fig1, ani


