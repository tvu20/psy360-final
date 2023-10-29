import os
import csv

path = os.path.join(os.getcwd(), "AffectiveText")
print(path)

emotion_map = {
    0: "anger",
    1: "disgust",
    2: "fear",
    3: "joy", 
    4: "sadness", 
    5: "surprise"
}

# ----------------
# TRAINING DATA
# ----------------

output_file = open(os.path.join(path, "train.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "AffectiveText.test", "affectivetext_test.txt"), 'r') as f_text, open(os.path.join(path, "AffectiveText.test", "affectivetext_test.emotions.gold"), 'r') as f_emotion:

    index = 0
    emotions = [line.rstrip() for line in f_emotion]

    for line in f_text:
        sentences = line.split(">")

        line_emotions = emotions[index].split(" ")[1:]

        emotion = line_emotions.index(max(line_emotions))

        writer.writerow([emotion_map[int(emotion)], sentences[1].strip()])

        index += 1

output_file.close()

  
# ----------------
# TESTING DATA
# ----------------

output_file = open(os.path.join(path, "test.csv"), 'w+')

writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

writer.writerow(["emotion", "text"])

with open(os.path.join(path, "AffectiveText.trial", "affectivetext_trial.txt"), 'r') as f_text, open(os.path.join(path, "AffectiveText.trial", "affectivetext_trial.emotions.gold"), 'r') as f_emotion:

    index = 0
    emotions = [line.rstrip() for line in f_emotion]

    for line in f_text:
        sentences = line.split(">")

        line_emotions = emotions[index].split(" ")[1:]

        emotion = line_emotions.index(max(line_emotions))

        writer.writerow([emotion_map[int(emotion)], sentences[1].strip()])

        index += 1

output_file.close()