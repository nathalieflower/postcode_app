class PostcodeData:
    def __init__(self, postcode, region, country):
        self.postcode = postcode
        self.region = region
        self.country = country


    def __str__(self):
        return f"\n\tPostcode:{self.postcode} \n\tRegion:{self.region} \n\tCountry:{self.country}"
