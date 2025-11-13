"""EmotionAlert – raises a flag when a negative emotion persists."""
import time
from typing import Iterable

class EmotionAlert:
    def __init__(self, negative_emotions: Iterable[str] = ("sad", "angry"), threshold_seconds: int = 10):
        self.neg_set = set(negative_emotions)
        self.threshold = threshold_seconds
        self.current_emotion = None
        self.start_time = time.time()

    def update(self, emotion: str) -> bool:
        """Return True if alert condition is met, else False."""
        now = time.time()
        if emotion != self.current_emotion:
            # Emotion changed → reset timer
            self.current_emotion = emotion
            self.start_time = now
            return False

        # Same emotion continues
        if emotion in self.neg_set and (now - self.start_time) >= self.threshold:
            return True  # Alert!
        return False
