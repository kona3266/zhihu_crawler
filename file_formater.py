import json
import os
def format_result():
    with open('result.txt', 'r+') as f:
        data = f.readlines()
    data = [eval(i.strip()) for i in data]
    format_data = json.dumps(data, indent=4, separators=(',',": "),ensure_ascii=False)
    with open('format_result.json', 'w+', encoding='utf-8') as f:
        f.write(format_data)
        f.close()
    os.remove('result.txt')
