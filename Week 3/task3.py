# visualize_data.py
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

def save_plot(fig, name):
    os.makedirs("plots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fig.savefig(f"plots/{name}_{timestamp}.png")

def visualize_data(df):
    fig1 = plt.figure()
    df['category'].value_counts().plot(kind='bar')
    plt.title("Category-wise Count")
    save_plot(fig1, "bar_plot")

    fig2 = plt.figure()
    sns.heatmap(df.corr(), annot=True)
    plt.title("Correlation Heatmap")
    save_plot(fig2, "heatmap")
