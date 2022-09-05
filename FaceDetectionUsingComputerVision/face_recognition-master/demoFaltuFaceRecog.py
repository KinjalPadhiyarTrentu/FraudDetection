import face_recognition
import cv2
import numpy
import os
import pickle
import glob

video_capture = cv2.VideoCapture(2)

trained_encodings = []
file = open("load_image.txt",'rb')
trained_encodings = pickle.load(file)
#print(trained_encodings)

face_locations = []
face_encodings = []
face_names = []
image_names = []

testing = glob.glob('C:\\Users\\Dishant\\PycharmProjects\\face_recognition-master\\training_images\\*')
print("testing:",testing)
process_this_frame = True
i=0

for file in range(5000):
    #image_names = os.path.split(file)[-1]
    #print("\t name:" , image_names)

    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # if i < 4:
    #     process_this_frame=False
    #     i += 1
    # else:
    #     i = 0
    if process_this_frame:

        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        #face_names = []

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(trained_encodings, face_encoding,tolerance=0.5)
            name = "Unknown"
            print(match)
            #print(image_names)

            j = 0
            for im,m in enumerate(match):
                if m:
                    name = os.path.split(testing[im])[-1]
                    #                j += 1
                    print("face:",name)
                    face_names.append(name)

    # process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


