import os
import json
import csv

path = os.path.join(os.getcwd(), "new_vegas")
print(path)

emotion_map = {
    "Happy": "joy",
    "Sad": "sadness",
    "Anger": "anger",
    "Disgust": "disgust",
    "Fear": "fear",
    "Neutral": "neutral",
    "Surprise": "surprise",
}

with open(os.path.join(path, "new_vegas.json"), 'r') as f:
    data = json.load(f)
    test = data['test']
    train = data['train']
    valid = data['valid']
    print(data.keys())

    # ----------------
    # TRAINING DATA
    # ----------------

    output_file = open(os.path.join(path, "train.csv"), 'w+')

    writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='')

    # writer.writerow(["emotion", "text"])

    for item in train:
        emotion = item["emotion"]

        if emotion == "Pained": 
            continue

        writer.writerow([emotion_map[emotion], item["text"]])

    output_file.close()

    # ----------------
    # TESTING DATA
    # ----------------

    output_file = open(os.path.join(path, "test.csv"), 'w+')

    writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

    # writer.writerow(["emotion", "text"])

    for item in test:
        emotion = item["emotion"]

        if emotion == "Pained": 
            continue

        writer.writerow([emotion_map[emotion], item["text"]])

    output_file.close()

    # ----------------
    # VALIDATION DATA
    # ----------------

    output_file = open(os.path.join(path, "valid.csv"), 'w+')

    writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

    # writer.writerow(["emotion", "text"])

    for item in valid:
        emotion = item["emotion"]

        if emotion == "Pained": 
            continue

        writer.writerow([emotion_map[emotion], item["text"]])

    output_file.close()


