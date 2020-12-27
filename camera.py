import cv2
import pyautogui
from speach import speak # for speaking use speak("enter text to speak")
def camera():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0
    speak = ("press space for cpturing image  &  Press esc to exit")

    pyautogui.alert("Press space for cpturing image  &  Press esc to exit")
    speak = ("press space for cpturing image  &  Press esc to exit")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()
    a=pyautogui.confirm('Enter option Gfg', buttons =['see_the_image', 'exit'])
    
    if a == 'see_the_image':
        print("img_name")
        c=cv2.imread(img_name)
        cv2.imshow("image",c)
        cv2.waitKey(0)
#camera()



