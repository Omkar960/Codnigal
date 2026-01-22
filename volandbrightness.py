import cv2
import mediapipe as mp
import numpy as np
import subprocess
from math import hypot
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
mp_draw = mp.solutions.drawing_utils

def set_mac_volume(volume_percent):
    volume_percent = int(np.clip(volume_percent,0,100))
    subprocess.run(
        ["osascript", "-e",f"set volume output volume {volume_percent}"],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL
    )

def set_mac_brightness(brightness_percent):
    brightness_percent = int(np.clip(brightness_percent,0,100))
    
    try:
        
        subprocess.run(
            ["osascript", "-e",f"tell application \"System Events\" to key code 113"],
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL,
            timeout=1
        )
    except:
        pass

def set_hand_difference_control(hand_difference):
    
    hand_difference = int(np.clip(hand_difference, 0, 100))
    
    if hand_difference > 50:
        print(f"Hand difference: YES ({hand_difference}%)")
        return "YES"
    else:
        print(f"Hand difference: NO ({hand_difference}%)")
        return "NO"


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera 0 failed, trying alternative indices...")
    for i in range(1, 5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Successfully opened camera {i}")
            break
    else:
        print("Error: couldn't access any webcam")
        exit()


cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cap.set(cv2.CAP_PROP_FPS, 30)
    
while True:
    success, img = cap.read()
    if not success:
        print('Failed to read frame, attempting to reconnect...')
        cap.release()
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print('Could not reconnect to camera')
            break
        continue
    img = cv2.flip(img,1)
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        
        if len(results.multi_hand_landmarks) >= 2:
            
            hand1_landmarks = results.multi_hand_landmarks[0]
            hand1_label = results.multi_handedness[0].classification[0].label
            hand2_landmarks = results.multi_hand_landmarks[1]
            hand2_label = results.multi_handedness[1].classification[0].label
            
            
            hand1_palm = hand1_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
            hand2_palm = hand2_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
            
            h, w, _ = img.shape
            hand1_pos = (int(hand1_palm.x*w), int(hand1_palm.y*h))
            hand2_pos = (int(hand2_palm.x*w), int(hand2_palm.y*h))
            
          
            hand_distance = hypot(
                hand2_pos[0] - hand1_pos[0],
                hand2_pos[1] - hand1_pos[1]
            )
            
            
            hand_diff_percent = np.interp(hand_distance, [50, 400], [0, 100])
            result = set_hand_difference_control(hand_diff_percent)
            
            
            cv2.line(img, hand1_pos, hand2_pos, (255, 0, 255), 3)
            cv2.circle(img, hand1_pos, 12, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, hand2_pos, 12, (255, 0, 255), cv2.FILLED)
            
            
            handdif_bar = np.interp(hand_distance, [50, 400], [400, 150])
            cv2.rectangle(img, (200, 150), (235, 400), (255, 0, 255), 2)
            cv2.rectangle(img, (200, int(handdif_bar)), (235, 400), (255, 0, 255), cv2.FILLED)
            
            display_text = "YES" if hand_diff_percent > 50 else "NO"
            color = (0, 255, 0) if hand_diff_percent > 50 else (0, 0, 255)
            
            cv2.putText(
                img,
                f"Hand Distance: {int(hand_distance)}px - {display_text}",
                (150, 450),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                3
            )
        
        
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[i].classification[0].label

            mp_draw.draw_landmarks(
                    img,hand_landmarks,mp_hands.HAND_CONNECTIONS
                )
            thumb_tip = hand_landmarks.landmark[
                mp_hands.HandLandmark.THUMB_TIP
                ]
            index_tip = hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP
                ]
            h,w,_ = img.shape
            thumb_pos = (int(thumb_tip.x*w),int(thumb_tip.y*h))
            index_pos = (int(index_tip.x*w),int(index_tip.y*h))

            cv2.circle(img,thumb_pos,10,(255,0,0),cv2.FILLED)
            cv2.circle(img, index_pos,10,(255,0,0),cv2.FILLED)
            cv2.line(img,thumb_pos,index_pos,(0,255,0),3)
            distance = hypot(
                index_pos[0]-thumb_pos[0],
                index_pos[1] - thumb_pos[1]
                )
            if hand_label == "Right":
                volume_percent = np.interp(distance,[30,300],[0,100])
                set_mac_volume(volume_percent)
                vol_bar = np.interp(distance,[30,300],[400,150])
                cv2.rectangle(img,(50,150),(85,400),(255,0,0),2)
                cv2.rectangle(img,(50,int(vol_bar)),(85,400),(255,0,0),cv2.FILLED)
                cv2.putText(
                    img,f"Volume {int(volume_percent)}%",
                    (40,450),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,0,0),
                    3
                    )
            elif hand_label =="Left":
                brightness = np.interp(distance, [30,300],[0,100])
                try:
                    set_mac_brightness(brightness)
                except Exception as e:
                    print("Brightness error",e)
                bright_bar = np.interp(distance,[30,300],[400,150])
                cv2.rectangle(img,(100,150),(135,400),(0,255,0),2)
                cv2.rectangle(img,(100,int(bright_bar)),(135,400),(0,255,0),cv2.FILLED)
                cv2.putText(
                    img,
                    f"Brightness: {int(brightness)}%",
                    (90,450),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    3 
                )



    cv2.imshow("Mac Gesture volume & Brightness Controller",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

                



