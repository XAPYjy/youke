import os


# 文件下载
def file_upload(upload_file):
    UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 返回到上级目录
    dest_path = os.path.join(UPLOAD_DIR, 'statics/head', upload_file)  # 拼接上传文件的最终路径
    print(dest_path,"================")
    with open(dest_path, 'wb') as f:
        for chunk in upload_file.chunks():  # 将文件对象分块循环写入目标文件
            f.write(chunk)
    head_path = "/s/head/"+upload_file.name
    return head_path