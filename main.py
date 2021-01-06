import requests
import json
import sys

from PostcodeData import PostcodeData


def main():
    postcode = sys.argv[1]
    postcode_is_valid = validate_postcode(postcode)
    if not postcode_is_valid:
        print("Error: Invalid Postcode")
        exit(1)

    print(f"Input postcode")
    print(str(get_postcode_info(postcode)))
    print(f"\nNearest Postcodes")
    for data in get_nearest_postcodes(postcode):
        print(str(data))


def validate_postcode(postcode):
    info = requests.get(f'http://api.postcodes.io/postcodes/{postcode}/validate')
    result = json.loads(info.text)
    if result['result']:
        return True
    else:
        return False


def get_postcode_info(postcode):
    info = requests.get(f'http://api.postcodes.io/postcodes/{postcode}')
    response = json.loads(info.text)
    postcode_data = PostcodeData(response['result']['postcode'], response['result']['region'],
                                 response['result']['country'])
    return postcode_data


def get_nearest_postcodes(postcode):
    info = requests.get(f'http://api.postcodes.io/postcodes/{postcode}/nearest')
    response = json.loads(info.text)
    postcode_data = [PostcodeData(item['postcode'],
                                  item['region'],
                                  item['country'])
                     for item in response['result'] if not postcode == item['postcode']]

    return postcode_data


if __name__ == "__main__":
    main()
