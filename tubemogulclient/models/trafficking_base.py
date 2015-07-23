from tubemogulclient.models.base import Base


class TraffickingBase(Base):

    obj_name = "advertisers"

    def get_url(self):
        return "{0}/v1/trafficking/{1}".format(Base.connection.url, self.obj_name)
