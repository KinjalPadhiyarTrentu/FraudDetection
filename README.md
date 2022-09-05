# FraudDetection
Fraud Detection System which basically helps to avert the frauds happening in educational examinations along with the attendance management portal with the faces detected.

## Scope:

• This project provides fraud detection management system. The main benefit of this
application is that cause of this application time will saved and also reduces complexity. <br/>
• In this project each and every student will be under surveillance and system itself will
take attendance of students. <br/>

### Features provided by this project are:
• Detection <br/>
• Alignment <br/>
• Measurement <br/>
• Representation <br/>
• Matching <br/>
• Verification or Identification <br/>

### Aim and Objective of the project:
The purpose behind this is to build a standalone system
which will recognize whether person appearing for exam is actual student or dummy writer.

The following are the objectives which we desire to fulfil with the completion of this project: <br/>
• Given a video footage computer should be able to identify the face of each and
every student passing through the system. <br/>
• Given a video footage computer should be able to match the pattern of
recognized image with the actual image of database. <br/>

### Problem Specifications:
Every face has numerous, distinguishable landmarks, the different peaks and valleys
that make up facial features. FaceIt defines these landmarks as nodal points. Each human face
has approximately 80 nodal points. Some of these measured by the software are:

• Distance between the eyes <br/>
• Width of the nose <br/>
• Depth of the eye sockets <br/>
• The shape of the cheekbones <br/>
• The length of the jaw line <br/>

### System Description:

As mentioned before, our project aims to detect frauds happening in the educational examinations
by image processing using Dlib's face recognition tool. This tool maps an image of a human face
to a 128 dimensional vector space where images of the same person are near to each other and
images from different people are
far apart. Therefore, you can perform face recognition by mapping faces to the 128D space and
then checking if their Euclidean distance is small enough.

When using a distance threshold of 0.6, the Dlib model obtains an accuracy of 99.38% on the
standard LFW face recognition benchmark, which is comparable to other state-of-the-art methods
for face recognition as of February 2017. This accuracy means that, when presented with a pair of
face images, the tool will correctly identify if the pair belongs to the same person or is from
different people 99.38% of the time. <br/> <br/>

This method starts by using: <br/>
1. A training set of labeled facial landmarks on an image. These images are manually labeled,
specifying specific (x, y)-coordinates of regions surrounding each facial structure. <br/>
2. Priors, of more specifically, the probability on distance between pairs of input pixels.
Given this training data, an ensemble of regression trees are trained to estimate the facial
landmark positions directly from the pixel intensities themselves (i.e., no “feature extraction” is
taking place). <br/>

The end result is a facial landmark detector that can be used to detect facial landmarks in real-
time with high quality predictions.

The pre-trained facial landmark detector inside the dlib library is used to estimate the location
of 68 (x, y)-coordinates that map to facial structures on the face.

The indexes of the 68 coordinates can be visualized on the image below:

<img width="508" alt="image" src="https://user-images.githubusercontent.com/99310137/188344181-db044b4d-0323-4c56-9a78-82bf82e830ef.png">

### Structure Diagram:
The process of face detection starts by opening the camera for
individual class . The camera will get the encodings of the detected faces and
compare them with the actual encodings. <br/>

<img width="257" alt="image" src="https://user-images.githubusercontent.com/99310137/188344314-0e178630-c7f0-4df5-8a73-64619c0b86b6.png">

### User Interface and Implementation:

<img width="480" alt="image" src="https://user-images.githubusercontent.com/99310137/188345214-51ef6c88-894e-438c-af75-36f22660a5ac.png">

<img width="482" alt="image" src="https://user-images.githubusercontent.com/99310137/188345231-060c441a-15da-4ec0-93d7-a5276f1786b7.png">

<img width="496" alt="image" src="https://user-images.githubusercontent.com/99310137/188345248-46a8ae65-c142-4dc0-afac-f73335f629fc.png">

<img width="488" alt="image" src="https://user-images.githubusercontent.com/99310137/188345267-06da19cb-fcea-45dc-8f2b-630d8f2953a2.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/99310137/188345290-b9d0448c-ec52-49ce-9967-d60542c7385b.png">

<img width="491" alt="image" src="https://user-images.githubusercontent.com/99310137/188345309-0d9c6596-31d5-435a-9bd2-e75c4783cc9d.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/99310137/188345327-341272e3-782d-424b-918a-2ecd9ade0a05.png">

<img width="495" alt="image" src="https://user-images.githubusercontent.com/99310137/188345343-e6c2ba8d-c59e-4eb2-b03a-9f1e13ed246a.png">

### Unique Features:

• People face should be visible in front of the camera. The people who are walking towards
camera are recognized. <br/> 
• Upon Face recognition it is alarmed whether it is accepted or rejected. <br/>
• The recognized person details are displayed in real time. <br/>
• The environment is indoor. <br/>
• The detection accuracy is greater than 80%. <br/>
• The camera is able to track the detected face when it is moving and should not generate
multiple alarms. <br/>
• The detection time is 5-10 sec. <br/>
• The face registered per person is 1-10. <br/>
• The face detection should allow ±20 degree tilt in both x and y direction. <br/>
• The face recognition should work at various resolutions above 640x480 and frame rate above
10 fps. <br/>
• Works simultaneously with video analytics for other cameras. <br/>

### Summary:

In general, in one aspect, the invention is a recognition system for identifying members of an
audience. The invention includes an imaging system which generates an image of the
audience; a selector module for selecting a portion of the generated image; a detection means
which analyzes the selected image portion to determine whether an image of a person is
present; and a recognition module for determining whether a detected image of a person
resembles one of a reference set of images of individuals. Preferred embodiments include the
following features. The recognition module also determines which one, if any, of the
individuals in the reference set the detected image resembles. The selection means includes
a motion detector for identifying the selected portion of the image by detecting motion and it
includes a locator module for locating the portion of the image corresponding to the face of
the person detected. In the recognition system, the detection means and the recognition
module employ a first and second pattern recognition techniques, respectively, to determine
whether an image of a person is present in the selected portion of the image and both pattern
recognition techniques employ a set of eigenvectors in a multi-dimensional image space to
characterize the reference set. In addition, the second pattern recognition technique also
represents each member of the reference set as a point in a subspace defined by the set of
eigenvectors. Also, the image of a person is an image of a person's face and the reference set
includes images of faces of the individuals.

