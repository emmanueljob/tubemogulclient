from tubemogulclient.models.trafficking_base import TraffickingBase


class Campaign(TraffickingBase):

    obj_name = "campaigns"

    def find_by_advertiser(self, advertiser_id, limit=50, offset=0):
        url = "{0}?advertiser_id={1}&limit={2}&offet={3}".format(self.get_url(), advertiser_id, limit, offset)
        return self.find_many_by_url(url)
