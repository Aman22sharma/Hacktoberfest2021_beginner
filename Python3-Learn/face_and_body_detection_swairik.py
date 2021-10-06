import mediapipe as mp
import cv2
import sys

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cascPath = sys.argv[1] if len(sys.argv) > 1 else '.'

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()
#         frame = cv2.flip(frame, 1)  # flip at the end for showing
        
        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Make Detections
        results = holistic.process(image)
#         print(results.face_landmarks)
        
        # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
        
        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Draw face landmarks using mp_holistic.FACE_CONNECTIONS
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color = (0,0,0), thickness = 1, circle_radius = 1),
                                  mp_drawing.DrawingSpec(color = (80,256,121), thickness = 1, circle_radius = 1)
                                 )
        
        # Draw right hand
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color = (80,22,10), thickness = 2, circle_radius = 4),
                                  mp_drawing.DrawingSpec(color = (80,44,121), thickness = 2, circle_radius = 2)
                                 )

        # Draw left hand
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color = (121,22,76), thickness = 2, circle_radius = 4),
                                  mp_drawing.DrawingSpec(color = (121,44,250), thickness = 2, circle_radius = 2)
                                 )
        
        # Draw Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color = (245,117,66), thickness = 2, circle_radius = 4),
                                  mp_drawing.DrawingSpec(color = (245,66,230), thickness = 2, circle_radius = 2)
                                 )
        
        
        
        image = cv2.flip(image, 1)
        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xff == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()