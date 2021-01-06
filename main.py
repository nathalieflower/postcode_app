import requests
import json


def main():
    print("Please input postcode:")

    postcode = 'PE28 3JT'
    r = requests.get(f'http://api.postcodes.io/postcodes/{postcode}/validate')
    result = json.loads(r.text)
    if result['result']:
        print(postcode_info(postcode))
        print(nearest_postcodes(postcode))
    else:
        print("Error: Invalid postcode")


def postcode_info(postcode):
    info = requests.get(f'http://api.postcodes.io/postcodes/{postcode}')
    response = json.loads(info.text)
    country = response['result']['country']
    region = response['result']['region']
    result = f"Region: {region} \nCountry: {country}"
    return result

def nearest_postcodes(postcode):
    info = requests.get(f'http://api.postcodes.io/postcodes/{postcode}/nearest')
    response = json.loads(info.text)
    postcodes = {item['postcode'] for item in response['result']}

    return postcodes


if __name__ == "__main__":
    main()
