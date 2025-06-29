import os
import shutil
import random

# ==============================
# CẤU HÌNH THƯ MỤC NGUỒN
image_folder = "D:\downloads\project-2\images"      # Thư mục ảnh gốc (frame_XXXX.jpg)
label_folder = "D:\downloads\project-2\labels"       # Thư mục nhãn gốc (xxx-frame_XXXX.txt)

# THƯ MỤC ĐÍCH
output_dir = "dataset"
images_output = os.path.join(output_dir, "images")
labels_output = os.path.join(output_dir, "labels")

# TỶ LỆ TRAIN / VAL
train_ratio = 0.8
# ==============================

# Tạo thư mục
for split in ["train", "val"]:
    os.makedirs(os.path.join(images_output, split), exist_ok=True)
    os.makedirs(os.path.join(labels_output, split), exist_ok=True)

# Lấy danh sách ảnh
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".jpg")])
random.shuffle(image_files)

# Tách train / val
train_count = int(len(image_files) * train_ratio)
train_files = image_files[:train_count]
val_files = image_files[train_count:]

# Hàm xử lý từng ảnh
def process_split(split_files, split_name):
    for img_file in split_files:
        base_name = os.path.splitext(img_file)[0]  # frame_XXXX
        label_file = None

        # Tìm file label gốc theo tên
        for f in os.listdir(label_folder):
            if f.endswith(".txt") and base_name in f:
                label_file = f
                break

        if label_file is None:
            print(f"⚠️ Không tìm thấy nhãn cho {img_file}, bỏ qua")
            continue

        # Đổi tên label về đúng dạng: frame_XXXX.txt
        new_label_name = base_name + ".txt"

        # Copy ảnh
        shutil.copyfile(
            os.path.join(image_folder, img_file),
            os.path.join(images_output, split_name, img_file)
        )

        # Copy nhãn
        shutil.copyfile(
            os.path.join(label_folder, label_file),
            os.path.join(labels_output, split_name, new_label_name)
        )

        print(f"✅ {split_name}: {img_file} + {label_file} → OK")

# Chạy chia
process_split(train_files, "train")
process_split(val_files, "val")

print("\n🎉 Hoàn tất! Dataset đã chia tại thư mục 'dataset/'")
