import csv
from collections import Counter

def generate_emotion_feedback(log_file="emotion_log.csv"):
    try:
        with open(log_file, mode='r') as file:
            reader = csv.DictReader(file)
            emotions = [row['Emotion'] for row in reader]  # Capital 'E'

        if not emotions:
            return "No emotions recorded. Please run the detection first."

        emotion_counts = Counter(emotions)
        total = sum(emotion_counts.values())
        most_common = emotion_counts.most_common()

        feedback = "🎯 Emotion Summary:\n\n"
        for emotion, count in most_common:
            percentage = (count / total) * 100
            feedback += f"• {emotion.capitalize()}: {percentage:.1f}%\n"

        dominant = most_common[0][0]

        interpretation = {
            "happy": "The person appeared positive and engaged.",
            "neutral": "The person remained calm and neutral.",
            "sad": "The person seemed less engaged or possibly upset.",
            "angry": "Signs of frustration or disagreement were observed.",
            "surprise": "They showed alertness and attentiveness.",
            "fear": "There were signs of nervousness or stress.",
            "disgust": "Moments of discomfort or disapproval were seen."
        }

        feedback += f"\n📝 Feedback:\n{interpretation.get(dominant, 'No specific interpretation available.')}"
        return feedback

    except FileNotFoundError:
        return "emotion_log.csv not found. Please run the main detection script first."


if __name__ == "__main__":
    summary = generate_emotion_feedback()
    print(summary)
