import os
import csv

path = os.path.join(os.getcwd(), "goemotions", "data")
print(path)

emotions = []

emotion_map = {
    "anger": "anger",
    "annoyance": "anger",
    "disapproval": "anger",
    "disgust": "disgust",
    "fear": "fear",
    "nervousness": "fear",
    "joy": "joy", 
    "amusement": "joy", 
    "approval": "joy", 
    "excitement": "joy", 
    "gratitude": "joy",  
    "love": "joy", 
    "optimism": "joy", 
    "relief": "joy", 
    "pride": "joy", 
    "admiration": "joy", 
    "desire": "joy", 
    "caring": "joy",
    "sadness": "sadness", 
    "disappointment": "sadness",
    "embarrassment": "sadness",
    "grief": "sadness",
    "remorse": "sadness",
    "surprise": "surprise",
    "realization": "surprise",
    "confusion": "surprise",
    "curiosity": "surprise",
    "neutral": "neutral"
}

with open(os.path.join(path, "emotions.txt"), 'r') as f:
    for line in f:
        emotions.append(line.strip())

    print(emotions)


# ----------------
# TRAINING DATA
# ----------------

output_file = open(os.path.join(path, "train.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "train.tsv"), 'r') as f_text:
    for line in f_text:
        parts = line.split("	")

        e_index = parts[1].split(",")[0]

        emotion = emotions[int(e_index)]

        writer.writerow([emotion_map[emotion], parts[0].strip()])

output_file.close()


# ----------------
# TESTING DATA
# ----------------

output_file = open(os.path.join(path, "test.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "test.tsv"), 'r') as f_text:
    for line in f_text:
        parts = line.split("	")

        e_index = parts[1].split(",")[0]

        emotion = emotions[int(e_index)]

        writer.writerow([emotion_map[emotion], parts[0].strip()])

output_file.close()


# ----------------
# VALIDATION DATA
# ----------------

output_file = open(os.path.join(path, "valid.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "dev.tsv"), 'r') as f_text:
    for line in f_text:
        parts = line.split("	")

        e_index = parts[1].split(",")[0]

        emotion = emotions[int(e_index)]

        writer.writerow([emotion_map[emotion], parts[0].strip()])

output_file.close()