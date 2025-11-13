"""EmotionDetector – wraps DeepFace for single‑frame emotion inference and logs results."""
from deepface import DeepFace
import csv
from datetime import datetime
import os

class EmotionDetector:
    def __init__(self):
        self.log_file = "emotion_log.csv"

        # If log file doesn't exist, write header
        if not os.path.isfile(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Emotion"])

    def detect(self, frame):
        """Return the dominant emotion string for a BGR frame (OpenCV format)."""
        result = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
        emotion = result[0]["dominant_emotion"]

        # Log the emotion with timestamp
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), emotion])

        return emotion
