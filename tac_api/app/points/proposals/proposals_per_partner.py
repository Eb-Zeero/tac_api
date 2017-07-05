import pandas as pd
from tac_api.app.alchemy.config import db


def partner_proposal(partner):
    # proposals = pd.DataFrame()

    proposals = {"partner": partner, 'id': {'key1': [56, 34, 56, 56, 65, 65, 56]}}
    # proposals['partner'] = [partner, partner, partner, partner, partner, partner]
    # proposals['pi_id'] = [2, 3, 1, 5, 2, 5]
    # proposals['title'] = ['title1', 'title2', 'title3', 'title4', 'title5', 'title6']
    # proposals['description'] = ['description1', 'description2', 'description3', 'description4', 'description5',
    # 'description6']
    # proposals['semester'] = ['2017-1', '2017-1', '2017-1', '2017-2', '2017-2', '2017-1']
    # proposals['comment'] = ['comment1', 'comment2', 'comment3', 'comment4', 'comment5', 'comment6']
    # proposals['req_time'] = [10, 20, 30, 20, 30, 20]
    # proposals['p0'] = [10, 20, 0, 20, 30, 0]
    # proposals['p1'] = [0, 0, 0, 0, 30, 20]
    # proposals['p2'] = [0, 0, 0, 0, 30, 0]
    # proposals['p3'] = [0, 20, 30, 0, 0, 20]
    # proposals['P4'] = [10, 20, 30, 20, 0, 0]
    # proposals['total_req_time'] = [10, 20, 30, 20, 30, 20]
    # proposals['moon'] = [10, 20, 100, 70, 30, 60]
    # proposals['seeing'] = [1, 2, 3, 2, 3, 2]
    # proposals['transparency'] = [60, 20, 30, 10, 70, 20]
    # proposals['warnings'] = ['title1', None, None, 'title4', None, 'title6']
    # print(proposals.to_dict())
    return proposals


class proposal_per_partner(db.module):
    __tablename__ = "name"
