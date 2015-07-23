from tubemogulclient.models.trafficking_base import TraffickingBase


class Placement(TraffickingBase):

    obj_name = "placements"

    def find_by_campaign(self, campaign_id):
        url = "{0}/v1/trafficking/campaigns/{1}/placements".format(Placement.connection.url, campaign_id)
        return self.find_many_by_url(url)
