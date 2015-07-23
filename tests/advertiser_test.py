import unittest
import json

from tubemogulclient.models.advertiser import Advertiser
from tests.base import Base


class AdvertiserTest(Base):

    def testGet(self):
        loader = Advertiser(AdvertiserTest.conn)
        advs = loader.find()

        for adv in advs:
            print adv
            
        print "DONE"
