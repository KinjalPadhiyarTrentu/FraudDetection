import face_recognition
import cv2
import numpy
import os
video_capture = cv2.VideoCapture(r'C:\Users\Dishant\PycharmProjects\face_recognition-master\sample video\song.mp4')
print(video_capture.isOpened())


g=1
files = os.listdir("video_training_images")
print(files)
training_face_encoding=[]
for file in files:
    print(file)
    training_image = face_recognition.load_image_file('video_training_images/'+file)
    training_face_encoding.append(face_recognition.face_encodings(training_image)[0])
    print(g)
    g += 1
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
i = 0
while True:
    ret, frame = video_capture.read()
    #frame=cv2.flip(frame, 1)
    small_frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
    # small_frame = cv2.resize(frame, (640,480))

    if i < 2:
        process_this_frame=False
        i += 1
        print("if",i)
    else:
        i = 0
        print(i)
    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(training_face_encoding, face_encoding,tolerance=0.5)
            name = "Unknown"
            print(match)
            print(files)

            i = 0
            for m in match:
                 if m:
                     name = files[i]
                 i += 1
            face_names.append(name)

    process_this_frame = not process_this_frame
    print(process_this_frame )
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4

        cv2.rectangle(small_frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(small_frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(small_frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', small_frame)
    print("break")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
