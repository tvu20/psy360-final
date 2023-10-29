import os
import json
import csv

path = os.path.join(os.getcwd(), "dailydialog")
print(path)

emotion_map = {
    0: "neutral",
    1: "anger",
    2: "disgust", 
    3: "fear", 
    4: "joy", 
    5: "sadness", 
    6: "surprise"
}

# ----------------
# TRAINING DATA
# ----------------

output_file = open(os.path.join(path, "train.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "train", "dialogues_train.txt"), 'r') as f_text, open(os.path.join(path, "train", "dialogues_emotion_train.txt"), 'r') as f_emotion:

    index = 0
    emotions = [line.rstrip() for line in f_emotion]

    for line in f_text:
        sentences = line.split("__eou__")

        line_emotions = emotions[index].split(" ")

        for i in range(len(sentences) - 1):

            writer.writerow([emotion_map[int(line_emotions[i])], sentences[i].strip()])

        index += 1

output_file.close()

    
# ----------------
# TESTING DATA
# ----------------

output_file = open(os.path.join(path, "test.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "test", "dialogues_test.txt"), 'r') as f_text, open(os.path.join(path, "test", "dialogues_emotion_test.txt"), 'r') as f_emotion:

    index = 0
    emotions = [line.rstrip() for line in f_emotion]

    for line in f_text:
        sentences = line.split("__eou__")

        line_emotions = emotions[index].split(" ")

        for i in range(len(sentences) - 1):

            writer.writerow([emotion_map[int(line_emotions[i])], sentences[i].strip()])

        index += 1

output_file.close()

    


# ----------------
# VALIDATION DATA
# ----------------

output_file = open(os.path.join(path, "validation.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "validation", "dialogues_validation.txt"), 'r') as f_text, open(os.path.join(path, "validation", "dialogues_emotion_validation.txt"), 'r') as f_emotion:

    index = 0
    emotions = [line.rstrip() for line in f_emotion]

    for line in f_text:
        sentences = line.split("__eou__")

        line_emotions = emotions[index].split(" ")

        for i in range(len(sentences) - 1):

            writer.writerow([emotion_map[int(line_emotions[i])], sentences[i].strip()])

        index += 1

output_file.close()