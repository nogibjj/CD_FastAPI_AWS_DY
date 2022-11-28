import requests

def get_topic(poem_topic = ''):
    if poem_topic == '':
        url = "https://v1.jinrishici.com/all"
    else:
        url = "https://v1.jinrishici.com/" + poem_topic
    Data = requests.get(url, timeout = 20)
    json_data = Data.json()
    print(json_data)
    return json_data

if __name__ == "__main__":
    get_topic("")