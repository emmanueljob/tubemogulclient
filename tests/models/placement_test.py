import unittest
import json

from tubemogulclient.models.placement import Placement
from tests.base import Base


class PlacementTest(Base):

    def testGet(self):
        loader = Placement(PlacementTest.conn)
        placements = loader.find()

        for placement in placements:
            assert placement['placement_id'] > 0

    def testGetByCampaign(self):
        loader = Placement(PlacementTest.conn)
        placements = loader.find_by_campaign(522549)

        for placement in placements:
            print placement
            assert placement['placement_id'] > 0
        
