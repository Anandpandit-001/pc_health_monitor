import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_disk_usage_anim():
    fig, ax = plt.subplots(figsize=(6, 6), facecolor='#0e1117')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)

    colors = ['#FF5733', '#33FF57']
    labels = ['Used', 'Free']

    def animate(i):

        usage = psutil.disk_usage('/')
        values = [usage.used, usage.free]
        total_gb = usage.total / (1024 ** 3)
        used_percent = usage.percent

        ax.clear()
        ax.axis('equal')

        wedges, texts, autotexts = ax.pie(
            values,
            labels=labels,
            colors=colors,
            startangle=90,
            autopct='%1.1f%%',
            pctdistance=0.85,
            wedgeprops=dict(width=0.3, edgecolor='#0e1117'),
            textprops={'color': "w", 'weight': 'bold'}
        )

        ax.set_title(f"Disk Usage Overview\nTotal Capacity: {total_gb:.1f} GB",
                     color='white', fontsize=14, pad=20)

        ax.text(0, 0, f"{used_percent}% \nUsed",
                ha='center', va='center', color='white',
                fontsize=16, fontweight='bold')

    ani = FuncAnimation(fig, animate, interval=2000, cache_frame_data=False)

    return fig, ani


