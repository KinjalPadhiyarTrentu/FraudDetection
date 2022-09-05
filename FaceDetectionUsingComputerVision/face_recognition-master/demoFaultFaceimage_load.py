import pickle
import face_recognition
import os
#training_image = face_recognition.load_image_file('training_images/1.jpg')
# training_face_encoding = face_recognition.face_encodings(training_image)[0]

files = os.listdir("training_images")
print(files)
training_face_encoding=[]
for file in files:
    #print(file)
    training_image = face_recognition.load_image_file('training_images/'+file)
    training_face_encoding.append(face_recognition.face_encodings(training_image)[0])
   # print(face_recognition.face_encodings(training_image)[0])
    # face_locations = face_recognition.face_locations(r"C:\Users\Dishant\PycharmProjects\face_recognition-master\training_images\{}".format(file))
    # print("loc", face_locations)
    #
    # face_encodings = face_recognition.face_encodings(r"C:\Users\Dishant\PycharmProjects\face_recognition-master\training_images\{}".format(file), face_locations, num_jitters=2)
    # print("enc",face_encodings)
filename = "load_image.txt"
file= open(filename,'wb')
pickle.dump(training_face_encoding,file)
print(training_face_encoding)
