import cv2

cap = cv2.VideoCapture(0) #filename can be an argument. 0 or -1 for camera
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480)) #Used to save the file

while(cap.isOpened()):
	ret,frame = cap.read()
	if ret == True:
		#out.write(frame)
		cv2.imshow('capture',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
#out.release()
cv2.destroyAllWindows()

