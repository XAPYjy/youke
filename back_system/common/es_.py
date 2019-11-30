import requests

HOST = '47.92.132.161'
PORT = 9200  # 默认9200
INDEX = 'youke'


def create_index(index_name='youke'):
    global INDEX
    INDEX = index_name
    url = f'http://{HOST}:{PORT}/{index_name}'
    json = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    # 调用增加索引的接口
    resp = requests.put(url, json=json)
    print(resp.json())


def remove_index(index_name):
    url = f'http://{HOST}:{PORT}/{INDEX if index_name is None else index_name}'
    resp = requests.delete(url)
    ret = resp.json()
    print(ret)


def add_doc(doc: dict, doc_type: str):
    # dict 对象中不存在id的key时会抛出异常吗？ 会
    doc_id = doc.pop('id') if 'id' in doc.keys() else None

    url = f'http://{HOST}:{PORT}/{INDEX}/{doc_type}' \
          + ('/' + str(doc_id) if doc_id else '')

    resp = requests.post(url, json=doc)
    ret = resp.json()
    if ret.get('result') == 'created':
        print('添加datas成功')
        return True

    print(ret)
    print('添加datas失败。。。')
    return False


def remove_doc(doc_type, doc_id):
    url = f'http://{HOST}:{PORT}/{INDEX}/{doc_type}/{doc_id}'
    resp = requests.delete(url)
    ret = resp.json()
    if ret.get('result') == 'deleted':
        print('删除成功')
        return True

    print('删除失败')
    return False


def search(keyword):
    url = f'http://{HOST}:{PORT}/_all/_search?q={keyword}'
    resp = requests.get(url)
    ret = resp.json()
    hits = ret.get('hits').get('hits')
    if hits:
        datas = []
        for source in hits:
            source_ = source.get('_source')
            source_['id'] = source.get('_id')

            datas.append(source_)

        return datas  # 返回搜索后的数据


if __name__ == '__main__':
    create_index()
    # remove_doc('person1', 'w5_3lW4BMRCZTBbTXLkQ')
    # remove_index()

    # search('图片')
