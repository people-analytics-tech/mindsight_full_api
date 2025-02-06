from mindsight_full_api import SharesValue
from datetime import datetime
import unittest

from mindsight_full_api.utils.aux_functions import generate_url
from mindsight_full_api.settings import API_ENDPOINT_SHARES_VALUE

new_shares_value_id = 2028

class TestMindFullSharesValue(unittest.TestCase):
    data = {
        "value": 86.9,
        "date": datetime.strptime("2025-05-02", "%Y-%m-%d").date(),
        "shares_type": "Bônus Equity"
    }
    update_data = {
        "value": 67.8,
        "date": datetime.strptime("2025-05-02", "%Y-%m-%d").date(),
        "shares_type": "Bônus Equity"
    }
    
    
    def test_a_post_create_shares_value(self):
        global new_shares_value_id 
        new_shares_value_response = SharesValue().post_create_shares_value(**self.data)
        new_shares_value_data = new_shares_value_response.json()
        new_shares_value_id = int(new_shares_value_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_SHARES_VALUE, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert new_shares_value_response.status_code==201

    def test_b_get_retrieve_shares_value(self):
        global new_shares_value_id 
        get_shares_value_response = SharesValue().get_shares_value(new_shares_value_id)
        get_shares_value_data = get_shares_value_response.json()
        assert get_shares_value_response.status_code==200

    def test_c_patch_update_shares_value(self):
        global new_shares_value_id 
        self.update_data["_id"] = new_shares_value_id
        patch_shares_value_response = SharesValue().patch_edit_shares_value(**self.update_data)
        patch_shares_value_data = patch_shares_value_response.json()
        new_shares_value_id = int(patch_shares_value_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_SHARES_VALUE, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_shares_value_response.status_code==200

    def test_put_edit_shares_value(self):
        global new_shares_value_id 
        self.update_data["_id"] = new_shares_value_id
        self.update_data["value"] = 65.8
        put_shares_value_response = SharesValue().put_edit_shares_value(**self.update_data)
        put_shares_value_data = put_shares_value_response.json()
        new_shares_value_id = int(put_shares_value_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_SHARES_VALUE, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert put_shares_value_response.status_code==200

    def test_d_delete_shares_value(self):
        global new_shares_value_id 
        deleted_shares_value = SharesValue().delete_shares_value(new_shares_value_id)
        assert deleted_shares_value.status_code==204

    def test_e_get_list_shares_value(self):
        list_shares_value = SharesValue().get_list_shares_value().get_all().results
        assert list_shares_value != []


TestMindFullSharesValue().test_put_edit_shares_value()