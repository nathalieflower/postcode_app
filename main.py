import requests
import json
import sys

from PostcodeData import PostcodeData


def main():
    postcode = sys.argv[1]
    r = requests.get(f'http://api.postcodes.io/postcodes/{postcode}/validate')
    result = json.loads(r.text)
    if result['result']:
        print(f"Input postcode")
        postcode_info(postcode)
        print(f"\nNearest Postcodes")
        nearest_postcodes(postcode)
    else:
        print("Error: Invalid postcode")


def postcode_info(postcode):
    info = requests.get(f'http://api.postcodes.io/postcodes/{postcode}')
    response = json.loads(info.text)
    postcode_data = PostcodeData(response['result']['postcode'], response['result']['region'],
                                 response['result']['country'])
    print(str(postcode_data))


def nearest_postcodes(postcode):
    info = requests.get(f'http://api.postcodes.io/postcodes/{postcode}/nearest')
    response = json.loads(info.text)
    postcode_data = {PostcodeData(item['postcode'],
                                  item['country'],
                                  item['region'])
                     for item in response['result'] if not postcode == item['postcode']}

    for data in postcode_data:
        print(str(data))


if __name__ == "__main__":
    main()
