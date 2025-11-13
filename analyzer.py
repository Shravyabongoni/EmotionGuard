"""EmotionAnalyzer – displays emotion frequency chart from the CSV log."""
import pandas as pd
import matplotlib.pyplot as plt

def show_emotion_summary(csv_path: str = "emotion_log.csv"):
    try:
        df = pd.read_csv(csv_path)
        counts = df["emotion"].value_counts()
        counts.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Emotion Frequency")
        plt.xlabel("Emotion")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"[ERROR] Could not read or plot: {e}")

# Run directly
if __name__ == "__main__":
    show_emotion_summary()
