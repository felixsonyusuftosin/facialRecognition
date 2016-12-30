from django.db import models
from .models import *
import cv2,os
import numpy as np
from PIL import Image
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.createLBPHFaceRecognizer()

def preptraining(idh):
    try:
        faces = face.objects.get(id = idh)
        lisfaces = list(faces)
    except:
        return False

    if len (lisfaces) > 0:
        images = []    
        for i in faces:
            imges = i.pictures.all()
            nbr = str(i.account)
            for img in imges:
                image_pil = Image.open(i.Picture.url).convert('L')
                image = np.array(image_pil, 'uint8')
                faces = faceCascade.detectMultiScale(image)
                for (x,y,w,h) in faces:
                    images.append(image[y:y+ h, x:x +w])
                    labels.append(nbr)
                    cv2.imshow("Adding faces to training set ...", image[y:y + h, x:x + w])
                    cv2.waitKey(50)
        return images,labels
                
    else:
        return False
def train(idh):
    try:
        images, labels = preptraining(idh)
        if images and training:
            cv2.destroyAllWindows()
            recognizer.train(images, np.array(labels))
            return True
        else:
            return False
    except():
        return False
def detect(img, accountnumber):
    predict_image = img
    nbr = accountnumber
    faces = faceCascade.detectMultiScale(predict_image)
    for (x, y, w, h) in faces:
        nbr_predicted,conf = recognizer.predict(predict_image[y:y + h.x:x +w])
        if nbr_predicted == accountnumber:
            obj = {}
            obj['success'] = True
            obj['confidence'] = conf
        else:
            obj = {}
            obj['success'] = False
            obj['confidence'] = conf
    return obj
            
            
            

def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)
 
	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()
 
		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()
 
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image

