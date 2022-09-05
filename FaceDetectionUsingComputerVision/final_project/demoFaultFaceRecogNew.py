import face_recognition
import cv2
import numpy
import os
import pickle
import glob


video_capture = cv2.VideoCapture(0)

# files = os.listdir("training_images")
# print(files)
training_face_encoding=[]
face_locations = []
face_encodings = []
face_names = []
image_names = []
unique_set=set()

file = open("load_image.txt",'rb')
trained_encodings = pickle.load(file)


testing = glob.glob('C:\\Users\\Dishant\\PycharmProjects\\face_recognition-master\\training_images\\*')
print("testing:",testing)

process_this_frame = True
i = 0
while True:
    ret, frame = video_capture.read()
    #frame=cv2.flip(frame, 1)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    if i < 4:
        process_this_frame=False
        i += 1
        print("if",i)
    else:
        i = 0
        print(i)

    if ret:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        print("f",face_locations)

        #face_names = []

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(trained_encodings, face_encoding)
            print(match)
            name = "Unknown"
            im = 0
            for im,m in enumerate(match):
                #name = "Unknown"
                if m:
                    print("im", im)
                    print("m", m)
                    name = os.path.split(testing[im])[-1]
                    print("face:",name)
                    unique_set.add(name)
            face_names.append(name)
            print("face list::",face_names)
                # else:
                #     name="UnKnOwN"
                #     #name_of_face="UnKnOwN"
                #     #face_names.append(name)

    #process_this_frame = not process_this_frame
   # print("process frame:",process_this_frame)
    for (top, right, bottom, left), name in zip(face_locations,face_names[-1]):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        print("nnaammeessss:",face_names[-1])
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, face_names[-1], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    print("break")
    print("SSSSSSEEEEEETTTTTTTT:",unique_set)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
