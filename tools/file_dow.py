import base64
import json
import os
import uuid

IMAGE_TYPE = ["jpg", "png", "bmp", "tif", "gif"]
VIDEO_TYPE = ["mp4"]

uid = uuid.uuid4().hex


# 头像图片下载
def file_upload(upload_file):
    image_data = [upload_file.file, upload_file.name, upload_file.content_type,
                  upload_file.size]
    print(image_data)
    # UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
    # dest_path = os.path.join(UPLOAD_DIR, "statics/head", uid + upload_file.name)  # 拼接上传文件的最终路径
    # dest_path = os.path.join(r'/var/flvs', uid + upload_file.name)
    with open(dest_path, 'ab') as f:
        for chunk in upload_file.chunks():  # 将文件对象分块循环写入目标文件
            f.write(chunk)
    head_path = "http://47.92.132.161:8000/image/" + uid + upload_file.name + "/"
    return head_path


# 下载上传的视频和图片
def video_upload(upload_file):
    # 返回类型
    image_data = [upload_file.file, upload_file.name, upload_file.content_type,
                  upload_file.size, upload_file.charset, upload_file.content_type_extra]
    print(image_data)
    # 判断文件类型
    src_type = str(upload_file.name).split(".")[-1].lower()
    if src_type in IMAGE_TYPE:
        UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
        dest_path = os.path.join(UPLOAD_DIR, "statics/video_img", uid + upload_file.name)  # 拼接上传文件的最终路径
        with open(dest_path, 'wb') as f:
            for chunk in upload_file.chunks():  # 将文件对象分块循环写入目标文件
                f.write(chunk)
        head_path = "http://47.92.132.161:8000/video_img/" + uid + upload_file.name + "/"  # 拼接图片路径返回
        class_size = round((upload_file.size / 1024) / 1024, 2)
        video_dict = {
            "video_path": head_path,
            "class_size": class_size,
        }
        return video_dict
    elif src_type in VIDEO_TYPE:
        # UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
        # dest_path = os.path.join(UPLOAD_DIR, "statics/video_img", uid+upload_file.name)  # 拼接上传文件的最终路径
        dest_path = os.path.join(r'/var/flvs', uid + upload_file.name)  # 拼接上传文件的最终路径
        with open(dest_path, 'ab') as f:
            for chunk in upload_file.chunks():  # 将文件对象分块循环写入目标文件
                f.write(chunk)
        video_path = "http://47.92.132.161:8000/video/youke/" + uid + upload_file.name + "/"
        # 计算视频大小
        class_size = round((upload_file.size / 1024) / 1024, 2)
        video_dict = {
            "video_path": video_path,
            "class_size": class_size,
        }
        return video_dict
    else:
        return None


if __name__ == '__main__':
    UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
    dest_path = os.path.join(UPLOAD_DIR, "statics/head/img.txt")
    dest_path_img = os.path.join(UPLOAD_DIR, "statics/head/img.jpg")
    print(dest_path)
    f = open(dest_path, "rb" )
    # print(json_data)
    with open(dest_path_img, "wb") as f2:
        img = f.read()
        # temp = base64.b64decode(img)
        f2.write(img)
