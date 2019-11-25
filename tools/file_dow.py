import os

IMAGE_TYPE = ["jpg", "png", "bmp", "tif", "gif"]


# 文件图片下载
def file_upload(upload_file):
    image_data = [upload_file.file, upload_file.name, upload_file.content_type,
                  upload_file.size, upload_file.charset, upload_file.content_type_extra]
    print(image_data)
    image_type = str(upload_file.name).split(".")[-1].lower()
    if image_type in IMAGE_TYPE:
        UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
        dest_path = os.path.join(UPLOAD_DIR, "statics/head", upload_file.name)  # 拼接上传文件的最终路径
        with open(dest_path, 'wb') as f:
            for chunk in upload_file.chunks():  # 将文件对象分块循环写入目标文件
                f.write(chunk)
        head_path = "http://47.92.132.161:8000/image/" + upload_file.name
        return head_path
    else:
        return None
