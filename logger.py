"""EmotionLogger – appends <timestamp, emotion> rows to a CSV."""
import os
import pandas as pd
from datetime import datetime

class EmotionLogger:
    def __init__(self, csv_path: str = "emotion_log.csv"):
        self.csv_path = csv_path
        if not os.path.exists(self.csv_path):
            # Create file with header once
            pd.DataFrame(columns=["timestamp", "emotion"]).to_csv(self.csv_path, index=False)

    def log(self, emotion: str):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pd.DataFrame([[ts, emotion]], columns=["timestamp", "emotion"]).to_csv(
            self.csv_path, mode="a", header=False, index=False
        )
