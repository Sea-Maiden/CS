import os
from pathlib import Path

# 设置目录路径
dataset_directory = Path('dataset')

# 遍历dataset目录下的所有子目录
for subdir in dataset_directory.iterdir():
    if subdir.is_dir():  # 确保是目录
        # 获取所有图片文件的路径列表
        images = list(subdir.glob('*'))
        # 只有当图片数量超过50时才进行处理
        if len(images) > 50:
            # 对文件列表按名称排序，然后去除前50个之后的所有文件
            images_to_remove = sorted(images)[50:]
            # 删除多余的文件
            for image in images_to_remove:
                try:
                    os.remove(image)
                    print(f'Removed: {image}')
                except OSError as e:
                    print(f"Error: {e.strerror} while removing {e.filename}")

print('Cleanup completed.')
