"""Main entry point – runs real-time emotion detection + logging + alerts."""
import cv2
from detector import EmotionDetector
from logger import EmotionLogger
from alert import EmotionAlert

# Initialize components
detector = EmotionDetector()
logger = EmotionLogger()
alerter = EmotionAlert()

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Webcam not accessible.")
    exit()

print("[INFO] EmotionGuard started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Frame capture failed.")
        break

    # Detect emotion
    try:
        emotion = detector.detect(frame)
    except Exception as e:
        print(f"[ERROR] Detection failed: {e}")
        continue

    # Log to CSV
    logger.log(emotion)

    # Check for alert condition
    alerting = alerter.update(emotion)
    if alerting:
        cv2.putText(frame, f"ALERT: {emotion.upper()} detected too long!",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    else:
        cv2.putText(frame, f"Emotion: {emotion}",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Show webcam frame
    cv2.imshow("EmotionGuard", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("[INFO] EmotionGuard exited.")
