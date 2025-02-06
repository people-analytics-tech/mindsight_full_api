from mindsight_full_api import User
from datetime import datetime
import unittest
from mindsight_full_api.settings import API_ENDPOINT_USERS, API_ENDPOINT_GROUPS, API_ENDPOINT_PERMISSIONS, API_ENDPOINT_USER_CONFIG_NOTIFICATIONS
from mindsight_full_api.utils.aux_functions import generate_url



new_user_id = None
class TestMindFullUsersRequests(unittest.TestCase):
    data = {
        "username": "teste@stonedex.com.br",
        "password": "teste123",
        "email": "teste@stonedex.com.br",
        "first_name": "Teste",
        "last_name": "Stonedex",
        "groups": [generate_url(API_ENDPOINT_GROUPS, "/1")],
        "user_permissions": [generate_url(API_ENDPOINT_PERMISSIONS, "/1")],
        "is_superuser": True,
        "is_active": True,
    }
    update_data = {
        "username": "teste@stonedex.com.br",
        "email": "teste@stonedex.com.br",
        "first_name": "Teste",
        "last_name": "Stonedex",
        "groups": [generate_url(API_ENDPOINT_GROUPS, "/2")],
        "user_permissions": [generate_url(API_ENDPOINT_PERMISSIONS, "/2")],
        "notifications_config": generate_url(API_ENDPOINT_USER_CONFIG_NOTIFICATIONS, "/46"),
        "is_superuser": True,
        "is_active": False,
    }
    
    def test_a_post_create_user(self):
        global new_user_id 
        new_user_response = User().post_create_user(**self.data)
        new_user_data = new_user_response.json()
        new_user_id = new_user_data["id"]
        assert new_user_response.status_code==201


    def test_b_get_retrieve_user(self):
        global new_user_id 
        get_user_response = User().get_user(new_user_id)
        get_user_data = get_user_response.json()
        get_data_id = int(get_user_data["api_url"]\
                                .replace(
                                    generate_url(API_ENDPOINT_USERS, ""), 
                                    ""
                                )\
                                .replace("/", ""))
        assert get_user_response.status_code==200

    def test_c_patch_update_user(self):
        global new_user_id 
        self.update_data["_id"] = new_user_id
        self.update_data["date_joined"] = datetime.now()
        patch_user_response = User().patch_edit_user(**self.update_data)
        patch_user_data = patch_user_response.json()
        new_user_id = int(patch_user_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_USERS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_user_response.status_code==200

    def test_d_put_edit_user(self):
        global new_user_id 
        self.update_data["_id"] = new_user_id
        self.update_data["is_active"] = True
        self.update_data["date_joined"] = datetime.now()
        put_user_response = User().put_edit_user(**self.update_data)
        put_user_data = put_user_response.json()
        new_user_id = put_user_data["id"]
        assert put_user_response.status_code==200

    def test_e_delete_user(self):
        global new_user_id 
        deleted_bonus = User().delete_user(new_user_id)
        assert deleted_bonus.status_code==204

    def test_b_get_list_user(self):
        global new_user_id 
        get_user_response = User().get_list_users().get_all().results
        assert get_user_response != []

