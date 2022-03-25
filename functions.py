import json


def find_post(word_request=''):
    with open('posts.json', encoding='windows-1251') as f:
        file = json.load(f)
        posts_list = list()
        for item in file:
            if word_request in item['content']:
                posts_list.append(item)
        return posts_list


def add_post(filename, text):
    with open('posts.json', encoding='windows-1251') as f:
        file = json.load(f)
    json_item = {"pic": f'static/uploads/images/{filename}', "content": text}
    file.append(json_item)

    with open('posts.json', 'w') as f:
        json.dump(file, f, indent=2, ensure_ascii=False)
