from mindsight_full_api import Bonus
from datetime import datetime
import unittest
import pytest

new_bonus_id = None

class TestMindFullBonusRequests(unittest.TestCase):
    data = {
        "date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "amount": 200.3,
        "person_id": 130333,
        "reference_date": datetime.strptime("2022-12-01", "%Y-%m-%d").date(),
        "reference_label": None,
        "type": "PLR",
    }
    update_data = {
        "date": datetime.strptime("2022-03-01", "%Y-%m-%d").date(),
        "amount": 250.50,
        "person_id": 130333,
        "reference_date": datetime.strptime("2021-12-01", "%Y-%m-%d").date(),
        "reference_label": None,
        "type": "Bônus",
    }
    
    def test_a_post_create_bonus(self):
        global new_bonus_id 
        new_bonus_response = Bonus().post_create_bonus(**self.data)
        new_bonus_data = new_bonus_response.json()
        new_bonus_id = int(new_bonus_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/bonuses/', 
                            ""
                        )\
                        .replace("/", ""))
        print(new_bonus_id)
        assert new_bonus_response.status_code==201

    def test_b_get_retrieve_bonus(self):
        global new_bonus_id 
        get_bonus_response = Bonus().get_bonus(new_bonus_id)
        get_bonus_data = get_bonus_response.json()
        assert get_bonus_response.status_code==200

    def test_c_patch_update_bonus(self):
        global new_bonus_id 
        self.update_data["_id"] = new_bonus_id
        patch_bonus_response = Bonus().patch_edit_bonus(**self.update_data)
        patch_bonus_data = patch_bonus_response.json()
        new_bonus_id = int(patch_bonus_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/bonuses/', 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_bonus_response.status_code==200

    def test_d_put_edit_bonus(self):
        global new_bonus_id 
        self.update_data["_id"] = new_bonus_id
        self.update_data["amount"] = 300.90
        put_bonus_response = Bonus().put_edit_bonus(**self.update_data)
        put_bonus_data = put_bonus_response.json()
        new_bonus_id = int(put_bonus_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/bonuses/', 
                            ""
                        )\
                        .replace("/", ""))
        assert put_bonus_response.status_code==200

    def test_e_delete_bonus(self):
        global new_bonus_id 
        deleted_bonus = Bonus().delete_bonus(new_bonus_id)
        assert deleted_bonus.status_code==204
