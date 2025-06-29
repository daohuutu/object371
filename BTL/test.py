import cv2
from ultralytics import YOLO

# Load mô hình đã huấn luyện (đường dẫn đến model của bạn)
model = YOLO("runs/detect/train6/weights/best.pt")  # hoặc yolov8n.pt nếu dùng model mặc định

# Mở video
video_path = "C:\\Users\\Admin\\Videos\\Captures\\War Thunder - Lái thử 2025-06-28 16-45-37.mp4"
cap = cv2.VideoCapture(video_path)

# Ghi video đầu ra (tùy chọn)
out = cv2.VideoWriter("C:\\Users\\Admin\\Videos\\Captures\\tets1920.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 
                      int(cap.get(cv2.CAP_PROP_FPS)),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Dự đoán với YOLO
    results = model.predict(frame, conf=0.4, iou=0.5)  # confidence có thể điều chỉnh

    # Vẽ kết quả lên khung hình
    annotated_frame = results[0].plot()

    # Hiển thị
    cv2.imshow("Tank Detection", annotated_frame)
    out.write(annotated_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
