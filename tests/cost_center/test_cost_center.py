from mindsight_full_api import CostCenters
from datetime import datetime
import unittest
from mindsight_full_api.utils.aux_functions import generate_url
from mindsight_full_api.settings import API_ENDPOINT_COST_CENTERS

new_cost_center_id = None

class TestMindFullCostCenterRequests(unittest.TestCase):
    data = {
        "name": "Cost Center Test Post",
        "start_date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "person_id": 130333,
        "end_date": None,
        "code": 81231231,
    }
    patch_data = {
        "name": "Cost Center Test Patch",
        "start_date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "person_id": 130333,
        "end_date": datetime.strptime("2023-04-01", "%Y-%m-%d").date(),
        "code": 81231231,
    }
    wrong_data = {
        "date": datetime.strptime("2022-05-01", "%Y-%m-%d").date(),
        "amount": "",
        "hours": 2.5,
        "person_id": -1,
        "type": "HORA EXTRA",
    }

    
    def test_a_post_create_cost_center_right_data(self):
        global new_cost_center_id 
        new_cost_center_response = CostCenters().post_create_cost_center(**self.data)
        new_cost_center_data = new_cost_center_response.json()
        new_cost_center_id = int(new_cost_center_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_COST_CENTERS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert new_cost_center_response.status_code==201

    def test_b_get_retrieve_cost_center_right_data(self):
        global new_cost_center_id 
        get_cost_center_response = CostCenters().get_cost_center(new_cost_center_id)
        get_cost_center_data = get_cost_center_response.json()
        assert get_cost_center_response.status_code==200

    def test_c_patch_update_cost_center_right_data(self):
        global new_cost_center_id 
        self.patch_data["_id"] = new_cost_center_id
        patch_cost_center_response = CostCenters().patch_edit_cost_center(**self.patch_data)
        patch_cost_center_data = patch_cost_center_response.json()
        new_cost_center_id = int(patch_cost_center_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_COST_CENTERS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_cost_center_response.status_code==200

    def test_d_put_edit_cost_center_right_data(self):
        global new_cost_center_id 
        self.patch_data["_id"] = new_cost_center_id
        self.patch_data["name"] = "Cost Center Test Put"
        put_cost_center_response = CostCenters().put_edit_cost_center(**self.patch_data)
        put_cost_center_data = put_cost_center_response.json()
        new_cost_center_id = int(put_cost_center_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_COST_CENTERS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert put_cost_center_response.status_code==200

    def test_e_delete_cost_center_right_data(self):
        global new_cost_center_id 
        deleted_cost_center = CostCenters().delete_cost_center(new_cost_center_id)
        assert deleted_cost_center.status_code==204

cli = TestMindFullCostCenterRequests()

# cli.test_a_post_create_cost_center_right_data()
cli.test_b_get_retrieve_cost_center_right_data()
cli.test_c_patch_update_cost_center_right_data()
cli.test_b_get_retrieve_cost_center_right_data()
cli.test_d_put_edit_cost_center_right_data()
cli.test_b_get_retrieve_cost_center_right_data()
cli.test_e_delete_cost_center_right_data()