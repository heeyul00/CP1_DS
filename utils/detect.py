import torch
import cv2
from pathlib import Path
import torch
import numpy as np
import time
import os


def load_model(model_path):
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, device='cpu')
    return model



def prepare_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) # 원본 영상의 프레임 속도 가져오기

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height)) # 프레임 속도 설정

    return cap, out



def detect_and_save(model, cap, out):
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # BGR 이미지를 RGB 이미지로 변환
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 이미지에 바운딩 박스 그리기
        start_time = time.time()
        results = model(frame_rgb)
        print(f"Frame {frame_count}: Detection took {time.time() - start_time:.2f} seconds")
        img = results.render()[0]

        # YOLOv5에서 반환된 이미지를 OpenCV 형식으로 변환
        img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        out.write(img_bgr)  # 결과를 저장

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()


def main():
    # 현재 작업 디렉토리 가져오기
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    # 상위 디렉토리로 이동
    parent_dir = os.path.dirname(current_dir)

    # 절대 경로로 파일 경로 지정
    model_path = os.path.join(parent_dir, 'weights', 'best.pt')
    video_path = os.path.join(parent_dir, 'data', 'sample.mp4')
    output_path = os.path.join(parent_dir, 'result', 'output_sample.mp4')

    model = load_model(model_path)
    cap, out = prepare_video(video_path, output_path)
    detect_and_save(model, cap, out)
    print('탐지가 완료되었습니다')


if __name__ == '__main__':
    main()
