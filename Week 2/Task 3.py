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
    df['Age'].value_counts().sort_index().plot(kind='bar')
    plt.title("Age-wise Count")
    save_plot(fig1, "bar_plot")

    fig2 = plt.figure()
    if df.select_dtypes(include='number').shape[1] > 1:
        sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)
        plt.title("Correlation Heatmap")
        save_plot(fig2, "heatmap")
    else:
        plt.close(fig2)

if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame({
        "Name": ["Ali", "Sara", "Zain", "Arooj"],
        "Age": [25, 28, 30, 22],
        "Score": [88, 92, 85, 90]
    })
    visualize_data(df)
    print("Plots generated and saved.")
