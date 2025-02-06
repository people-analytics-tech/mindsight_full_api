from mindsight_full_api import ExtraHours
from datetime import datetime
import unittest

from mindsight_full_api.utils.aux_functions import generate_url
from mindsight_full_api.settings import API_ENDPOINT_EXTRA_HOURS

new_extra_hours_id = None

class TestMindFullExtraHoursRequests(unittest.TestCase):
    data = {
        "date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "amount": 200.3,
        "hours": 2,
        "person_id": 130333,
        "type": "HORA EXTRA",
    }
    patch_data = {
        "date": datetime.strptime("2022-05-01", "%Y-%m-%d").date(),
        "amount": 250.6,
        "hours": 2.5,
        "person_id": 130333,
        "type": "HORA EXTRA",
    }
    wrong_data = {
        "date": datetime.strptime("2022-05-01", "%Y-%m-%d").date(),
        "amount": "",
        "hours": 2.5,
        "person_id": -1,
        "type": "HORA EXTRA",
    }

    
    def test_a_post_create_extra_hours_right_data(self):
        global new_extra_hours_id 
        new_extra_hours_response = ExtraHours().post_create_extra_hours(**self.data)
        new_extra_hours_data = new_extra_hours_response.json()
        new_extra_hours_id = int(new_extra_hours_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_EXTRA_HOURS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert new_extra_hours_response.status_code==201

    def test_b_get_retrieve_extra_hours_right_data(self):
        global new_extra_hours_id 
        get_extra_hours_response = ExtraHours().get_extra_hours(new_extra_hours_id)
        get_extra_hours_data = get_extra_hours_response.json()
        assert get_extra_hours_response.status_code==200

    def test_c_patch_update_extra_hours_right_data(self):
        global new_extra_hours_id 
        self.patch_data["_id"] = new_extra_hours_id
        patch_extra_hours_response = ExtraHours().patch_edit_extra_hours(**self.patch_data)
        patch_extra_hours_data = patch_extra_hours_response.json()
        new_extra_hours_id = int(patch_extra_hours_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_EXTRA_HOURS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_extra_hours_response.status_code==200

    def test_d_put_edit_extra_hours_right_data(self):
        global new_extra_hours_id 
        self.patch_data["_id"] = new_extra_hours_id
        self.patch_data["amount"] = 300.90
        put_extra_hours_response = ExtraHours().put_edit_extra_hours(**self.patch_data)
        put_extra_hours_data = put_extra_hours_response.json()
        new_extra_hours_id = int(put_extra_hours_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_EXTRA_HOURS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert put_extra_hours_response.status_code==200

    def test_e_delete_extra_hours_right_data(self):
        global new_extra_hours_id 
        deleted_extra_hours = ExtraHours().delete_extra_hours(new_extra_hours_id)
        assert deleted_extra_hours.status_code==204

