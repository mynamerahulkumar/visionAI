import cv2
import os 

def extract_frames(video_path,output_dir,interval_seconds):

    os.makedirs(output_dir,exist_ok=True)


    cap=cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error:Cannot open video{video_path}")
        return
    # get the video per second
    fps=cap.get(cv2.CAP_PROP_FPS)

    frame_interval=int(fps*interval_seconds)

    frame_count=0
    save_count=0


    while True:
        ret,frame=cap.read()
        if not ret:
            break

        if frame_count%frame_interval==0:
            output_fil=os.path.join(output_dir,f"frame_{save_count}.jpg")
            cv2.imwrite(output_fil,frame)
            save_count+=1
            print(f"Saved frame{save_count}")
        frame_count+=1
    cap.release()

    print(f"Extraction complete: {save_count} frames saved and image saved in {output_dir}")


interval_seconds=2
for i in range(5,6):
    video_path=f"/Users/rahulkumar/Documents/GitHub/visionAI/data/input_data/traffic{i}.mp4"
    output_dir=f"/Users/rahulkumar/Documents/GitHub/visionAI/data/output_data{i}"
    extract_frames(video_path,output_dir,interval_seconds)


