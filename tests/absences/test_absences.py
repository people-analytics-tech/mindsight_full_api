from mindsight_full_api import Absence
from datetime import datetime
import unittest
from mindsight_full_api.utils.aux_functions import generate_url
from mindsight_full_api.settings import API_ENDPOINT_ABSENCES

new_absence_id = None
class TestMindFullAbsenceRequests(unittest.TestCase):
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
    
    def test_a_post_create_absence(self):
        global new_absence_id 
        new_absence_response = Absence().post_create_absence(**self.data)
        new_absence_data = new_absence_response.json()
        new_absence_id = new_absence_data["id"]
        assert new_absence_response.status_code==201

    def test_b_get_retrieve_absence(self):
        global new_absence_id 
        get_absence_response = Absence().get_absence(new_absence_id)
        get_absence_data = get_absence_response.json()
        get_data_id = int(get_absence_data["api_url"]\
                                .replace(
                                    generate_url(API_ENDPOINT_ABSENCES, ""), 
                                    ""
                                )\
                                .replace("/", ""))
        assert get_absence_response.status_code==200

    def test_c_patch_update_absence(self):
        global new_absence_id 
        self.update_data["_id"] = new_absence_id
        patch_absence_response = Absence().patch_edit_absence(**self.update_data)
        patch_absence_data = patch_absence_response.json()
        new_absence_id = int(patch_absence_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_ABSENCES, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_absence_response.status_code==200

    def test_d_put_edit_absence(self):
        global new_absence_id 
        self.update_data["_id"] = new_absence_id
        self.update_data["observations"] = "Retroative vacation"
        put_absence_response = Absence().put_edit_absence(**self.update_data)
        put_absence_data = put_absence_response.json()
        new_absence_id = put_absence_data["id"]
        assert put_absence_response.status_code==200

    def test_e_delete_absence(self):
        global new_absence_id 
        deleted_bonus = Absence().delete_absence(new_absence_id)
        assert deleted_bonus.status_code==204


cli = TestMindFullAbsenceRequests()
cli.test_a_post_create_absence()
cli.test_d_put_edit_absence()
cli.test_e_delete_absence()