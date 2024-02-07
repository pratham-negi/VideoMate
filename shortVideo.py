import cv2 
import numpy as np 


   
    


def shortVideoFun(input , val = 40):
    temp_file_to_save = 'temp_file_1.mp4'
    with open(temp_file_to_save, "wb") as outfile:
        outfile.write(input.getbuffer())
    video = cv2.VideoCapture(temp_file_to_save)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    threshold = val

    writer = cv2.VideoWriter('final.mp4', cv2.VideoWriter_fourcc(*'h264'), 25, (width, height))
    ret, frame1 = video.read()
    prev_frame = frame1



    while True:
        ret, frame = video.read()
        if ret is True:
            if (((np.sum(np.absolute(frame-prev_frame))/np.size(frame)) > threshold)):
                writer.write(frame)
                prev_frame = frame
            
            else:
                prev_frame = frame
            

        
    
        else:
            break


    video.release()
    writer.release()
    cv2.destroyAllWindows()
    return writer