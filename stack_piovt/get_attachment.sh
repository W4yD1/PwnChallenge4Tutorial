#!/bin/bash

# 检查是否提供了镜像名称参数
if [ -z "$1" ]; then
  echo "Usage: $0 <image_name>"
  exit 1
fi

IMAGE_NAME=$1
CONTAINER_NAME="temp_container"
FILES_TO_COPY=("/home/ctf/dictionary" "/home/ctf/lib/x86_64-linux-gnu/libc.so.6" "/home/ctf/lib64/ld-linux-x86-64.so.2") # 替换为容器中的文件路径
DEST_DIR="./attchments" # 本地目标目录
ZIP_FILE="attchments.zip"

# 检查镜像是否存在
if ! docker image inspect "$IMAGE_NAME" > /dev/null 2>&1; then
  echo "Error: Image '$IMAGE_NAME' does not exist."
  exit 1
fi

# 创建本地目标目录
mkdir -p "$DEST_DIR"

# 运行容器
echo "Running container from image '$IMAGE_NAME'..."
docker run --name "$CONTAINER_NAME" -d "$IMAGE_NAME"

# 等待容器启动（可根据需要调整等待时间）
sleep 5

# 从容器中复制文件
echo "Copying files from container..."
for file in "${FILES_TO_COPY[@]}"; do
  docker cp "$CONTAINER_NAME":"$file" "$DEST_DIR"
done

# 检查文件是否成功复制
if [ ! -f "$DEST_DIR/${FILES_TO_COPY[0]##*/}" ] || [ ! -f "$DEST_DIR/${FILES_TO_COPY[1]##*/}" ] || [ ! -f "$DEST_DIR/${FILES_TO_COPY[2]##*/}" ]; then
  echo "Error: Failed to copy files from container."
  docker rm -f "$CONTAINER_NAME"
  exit 1
fi

# 打包文件为 ZIP
echo "Creating ZIP archive..."
zip -j "$ZIP_FILE" "$DEST_DIR"/*

# 删除容器
echo "Removing container..."
docker rm -f "$CONTAINER_NAME"



echo "Process completed. ZIP file created: $ZIP_FILE"q
