class PostcodeData:
    def __init__(self, postcode, country, region):
        self.postcode = postcode
        self.country = country
        self.region = region

    def __str__(self):
        return f"\n\tPostcode:{self.postcode} \n\tRegion:{self.region} \n\tCountry:{self.country}"
