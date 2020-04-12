import requests
import json

def run_test_request(url: str):
    resp = requests.get(url)
    return resp


if __name__ == "__main__":
    host = "http://127.0.0.1"
    port = ":8009"
    
    # episodes_id endpoint
    postfix = "/series/tt0096697/episodes?season_num=4"
    url = host+port+postfix
    print("Requesting {}".format(url))
    response = run_test_request(url)
    print("{}\n".format(response.json()))
    
    # top 250 series endpoint
    postfix = "/top_250"
    url = host+port+postfix
    print("Requesting {}".format(url))
    response = run_test_request(url)
    print("{}\n".format(response.json()))
    
    # top rated series endpoint
    postfix = "/series/most_popular/12"
    url = host+port+postfix
    print("Requesting {}".format(url))
    response = run_test_request(url)
    print("{}\n".format(response.json()))
    
    # newest series endpoint
    postfix = "/series/newest/12"
    url = host+port+postfix
    print("Requesting {}".format(url))
    response = run_test_request(url)
    print("{}\n".format(response.json()))