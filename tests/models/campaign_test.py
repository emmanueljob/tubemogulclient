import unittest
import json

from tubemogulclient.models.campaign import Campaign
from tests.base import Base


class CampaignTest(Base):

    def testGet(self):
        loader = Campaign(CampaignTest.conn)
        campaigns = loader.find()

        for campaign in campaigns:
            assert campaign['campaign_id'] > 0

    def testGetByAdvertiser(self):
        loader = Campaign(CampaignTest.conn)
        campaigns = loader.find_by_advertiser(83239, 1000)

        for campaign in campaigns:
            print campaign
            assert campaign['campaign_id'] > 0
        
