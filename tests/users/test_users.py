from mindsight_full_api import User
from datetime import datetime
import unittest

new_user_id = None
class TestMindFullUsersRequests(unittest.TestCase):
    data = {
        "person_id":130333,
        "start_date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "end_date": None,
        "is_approved": True,
        "type": "vacation",
        "observations": None,
        "number_of_days": 10,
    }
    update_data = {
        "person_id":130333,
        "start_date": datetime.strptime("2023-03-02", "%Y-%m-%d").date(),
        "end_date": datetime.strptime("2023-03-12", "%Y-%m-%d").date(),
        "is_approved": True,
        "type": "vacation",
        "observations": None,
        "number_of_days": 11,
    }
    def test_b_get_retrieve_user(self):
        global new_user_id 
        return User().get_list_users().get_all().results
        get_user_data = get_user_response.json()
        get_data_id = int(get_user_data["api_url"]\
                                .replace(
                                    'https://full.mindsight.com.br/stone/api/v1/users/', 
                                    ""
                                )\
                                .replace("/", ""))
        assert get_user_response.status_code==200
    # def test_a_post_create_user(self):
    #     global new_user_id 
    #     new_user_response = User().post_create_user(**self.data)
    #     new_user_data = new_user_response.json()
    #     new_user_id = new_user_data["id"]
    #     assert new_user_response.status_code==201

    # def test_b_get_retrieve_user(self):
    #     global new_user_id 
    #     get_user_response = User().get_user(new_user_id)
    #     get_user_data = get_user_response.json()
    #     get_data_id = int(get_user_data["api_url"]\
    #                             .replace(
    #                                 'https://full.mindsight.com.br/stone/api/v1/users/', 
    #                                 ""
    #                             )\
    #                             .replace("/", ""))
    #     assert get_user_response.status_code==200

    # def test_c_patch_update_user(self):
    #     global new_user_id 
    #     self.update_data["_id"] = new_user_id
    #     patch_user_response = User().patch_edit_user(**self.update_data)
    #     patch_user_data = patch_user_response.json()
    #     new_user_id = int(patch_user_data["api_url"]\
    #                     .replace(
    #                         'https://full.mindsight.com.br/stone/api/v1/users/', 
    #                         ""
    #                     )\
    #                     .replace("/", ""))
    #     assert patch_user_response.status_code==200

    # def test_d_put_edit_user(self):
    #     global new_user_id 
    #     self.update_data["_id"] = new_user_id
    #     self.update_data["observations"] = "Retroative vacation"
    #     put_user_response = User().put_edit_user(**self.update_data)
    #     put_user_data = put_user_response.json()
    #     new_user_id = put_user_data["id"]
    #     assert put_user_response.status_code==200

    # def test_e_delete_user(self):
    #     global new_user_id 
    #     deleted_bonus = User().delete_user(new_user_id)
    #     assert deleted_bonus.status_code==204


cli = TestMindFullUsersRequests()
data = cli.test_b_get_retrieve_user()
print()
# cli.test_a_post_create_User()
# cli.test_d_put_edit_User()
# cli.test_e_delete_User()