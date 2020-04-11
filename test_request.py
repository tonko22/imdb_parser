import requests
import json

def run_test_request(url: str):
    resp = requests.get(url)
    return resp


if __name__ == "__main__":
    host = "http://127.0.0.1"
    port = ":8009"
    postfix = "/series/tt0096697/episodes?season=16"
    url = host+port+postfix
    print("Requesting {}".format(url))
    response = run_test_request(url)
    print("{}\n".format(response.json()))