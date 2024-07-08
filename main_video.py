import cv2
from simple_facerec import SimpleFacerec
import time
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Dictionary to keep track of last announcement time
last_announced = {}

# Interval time in seconds for announcing the same name
announce_interval = 3


recognized_names = set()  # To keep track of already recognized names


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    current_time = time.time()
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

         # Beep if the name is "Ori Aboudi"
        # if name == "Ori Aboudi":
            # winsound.Beep(1000, 500)  # Frequency 1000 Hz, Duration 500 ms

         # Announce the name using TTS if enough time has passed since the last announcement
        if name not in last_announced or current_time - last_announced[name] >= announce_interval:
            engine.say(name)
            engine.runAndWait()
            last_announced[name] = current_time


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()