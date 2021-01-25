import json
import requests


def reportError(id):
    data = {"id": id}
    result = json.loads(requests.post("http://api.ttshitu.com/reporterror.json", json=data).text)
    if result['success']:
        return "报错成功"
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    result = reportError(id='成功返回的id')
    print(result)
