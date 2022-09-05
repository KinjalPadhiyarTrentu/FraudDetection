import face_recognition
import cv2
import numpy
import os
import pickle
import glob
from flask import Flask, redirect, url_for , request,render_template,session
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import datetime
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'project'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)


@app.route('/')
@cross_origin()
def detect():

    #Classname return from AJAX
    className = str(request.args.get('className'))
    print(type(className))
    print("class:",className)
    unique_set=set()
    print("type:",type(unique_set))

    video_capture = cv2.VideoCapture(1)
    print("Camera opened:",video_capture.isOpened())

    print("pickle loading starts:", datetime.datetime.now())

    face_locations = []
    face_encodings = []
    face_names = []
    image_names = []
    testing=[]

    file = open("load_image.txt",'rb')
    trained_encodings = pickle.load(file)

    for file in os.listdir(r"C:\Users\Dishant\eclipse-workspace\.metadata\.plugins\org.eclipse.wst.server.core\tmp0\wtpwebapps\Designing"):
        if file.endswith(".jpg"):
            print(file)
            testing.append(file)

    print("testing type",type(testing))
    print("dataset:",testing)
    print("pickle loading ends:", datetime.datetime.now())
 #   process_this_frame = True
    # i = 0
    while True:
        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if ret:
            print("face detection starts:", datetime.datetime.now())
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame,face_locations)
            print("faceLocations",face_locations)
           # print("faceEncod:",face_encodings)

            for face_encoding in face_encodings:
                print("face matching starts:", datetime.datetime.now())
                match = face_recognition.compare_faces(trained_encodings,face_encoding,tolerance=0.5)
                print(match)
                name = "Unknown"
                im = 0
                for im, m in enumerate(match):
                    print("m:", m)
                    if m:
                        #print("im", im)
                        #print("m", m)
                        #name = os.path.split(testing[im])
                        name=testing[im].split(".")[0]
                        print("name:",name)
                        unique_set.add(str(name))
                print("face matching ends:", datetime.datetime.now())
                face_names.append(name)
                print("face list::",face_names)
            print("face detection ends:", datetime.datetime.now())

        if len(face_locations)!=0:
            for (top, right, bottom, left), name in zip(face_locations,face_names[-1:]):
                print("face labelling starts:", datetime.datetime.now())
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, face_names[-1], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                print("face labelling ends:", datetime.datetime.now())

        print("face Show starts:", datetime.datetime.now())
        cv2.imshow('Video', frame)
        print("Matched Faces:",unique_set)
        print("face Show ends:",datetime.datetime.now())
        if cv2.waitKey(1) & 0xFF == 27:
            break

    video_capture.release()
    cv2.destroyAllWindows()

    unique_list = list(unique_set)

    cur = mysql.connection.cursor()


    cur.execute("DELETE FROM matchedfaces")

    for i in range(len(unique_list)):
        cur.execute("INSERT INTO matchedfaces(studentname,classname) VALUES(%s,%s)",(unique_list[i],className))
        print("matched faces inserted")

    print("class",className)
    cur.execute("select classId from classmaster WHERE className='{}'".format(className))
    current_class = cur.fetchone()
    print("current classs",type(current_class))
    print(current_class[0])
    current_class_string = str(current_class[0])
    print(type(current_class_string))
    cur.execute("select studentUsername from studentregistration WHERE cvo_classId='{}'".format(current_class_string))
    o = cur.fetchall()
    original_student_list = list(o)
    print("original type",type(original_student_list))
    cur.execute("select studentname from matchedfaces WHERE classname='{}'".format(className))
    c = cur.fetchall()
    current_student_list = list(c)

    print("original:",original_student_list)
    print("type of original",type(original_student_list))
    print("current:",current_student_list)

    cur.execute("DELETE FROM report")

    #absentstudent =[]
    for c in original_student_list:
        if c not in current_student_list:
            print("Absent Students",c)
            #absentstudent.append(c)
            cur.execute("INSERT INTO report(absentstudent,className) VALUES(%s,%s)", (c, className))
            print("INSERTED")

    mysql.connection.commit()
    cur.close()

    print("GRAPH STARTED")
    o_l = len(original_student_list)
    print("orig len",o_l)
    c_l = len(current_student_list)
    print("curr len",c_l)
    a_l = o_l-c_l
    #
    objects = ('Total', 'Present', 'Absent')
    print("objs")
    y_pos = numpy.arange(len(objects))
    print("y_pos")
    performance = [o_l, c_l, a_l]
    print("perfor")
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    print("bar")
    plt.xticks(y_pos, objects)
    print("xtricks")
    plt.xlabel('Student')
    print("label")
    plt.title('Student Chart')
    print("cahrt")
    plt.savefig('F:/Studies/project/Designing/WebContent/AdminResources/images/graph.jpg')
    #plt.savefig('C:/Users/Dishant/Desktop/graph.jpg')
    print("show")
    return "hello"

if __name__=='__main__':
    app.run(debug='True',threaded=True)
