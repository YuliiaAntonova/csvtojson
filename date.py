import json
import pandas as pd
import requests
from io import StringIO
import sys


def get_file():
    url = 'https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view?usp=sharing'
    file_id = url.split('/')[-2]
    dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
    url2 = requests.get(dwn_url).text
    csv_raw = StringIO(url2)
    df = pd.read_csv(csv_raw)
    res = df[['date', 'spend']].to_dict('records')
    print(res)
    content = {'data': res}
    with open("fill.json", "w") as f:
        json.dump(content, f, indent=4)

    if len(sys.argv) > 1:
        select = sys.argv[1:]
    else:
        select = 'None'

    print(df[select])
    return content


if __name__ == '__main__':
    get_file()
