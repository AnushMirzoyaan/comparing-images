import cv2
import face_recognition


def find_face_encodings(image_path):
    # reading image
    image = cv2.imread(image_path)

    # get face encodings from the image
    face_enc = face_recognition.face_encodings(image)

    # return face encodings
    return face_enc[0]


image_1 = find_face_encodings("/home/solicy/Desktop/comparing-images/images/image1.jpg")
image_2 = find_face_encodings("/home/solicy/Desktop/comparing-images/images/image4.jpg")

# checking both images are same
is_same = face_recognition.compare_faces([image_1], image_2)[0]

print(f"Is Same : {is_same}")

if is_same:
    # find the distance level between images
    distance = face_recognition.face_distance([image_1], image_2)
    distance = round(distance[0]*100)

    # calculating accurancy level between images
    accurancy = 100 - round(distance)

    print("the images are same")
    print(f"accurancy level is : {accurancy}%")
else:
    print ("the images are not same")
