from mindsight_full_api import Trainings
from datetime import datetime
import unittest

new_training_id = None
class TestMindFullTrainingRequests(unittest.TestCase):
    data = {
        "person_id":130333,
        "date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "course": "CURSO TESTE",
        "course_pt_br": "CURSO TESTE EM PT-BR",
        "course_en": "CURSO TESTE EM EN-US",
        "course_es": "CURSO TESTE EM ES-ES",
        "course_id": "1194163",
        "performance": "",
        "performance_pt_br": "",
        "performance_en": "",
        "performance_es": "",
        "old_status": "pending",
        "status": "pending",
        "mandatory": True,
    }
    update_data = {
        "person_id":130333,
        "date": datetime.strptime("2023-03-10", "%Y-%m-%d").date(),
        "course": "CURSO TESTE",
        "course_pt_br": "CURSO TESTE EM PT-BR",
        "course_en": "CURSO TESTE EM EN-US",
        "course_es": "CURSO TESTE EM ES-ES",
        "course_id": "1194163",
        "performance": "",
        "performance_pt_br": "",
        "performance_en": "",
        "performance_es": "",
        "old_status": "in_progress",
        "status": "in_progress",
        "mandatory": True,
    }
    
    def test_a_post_create_training(self):
        global new_training_id 
        new_training_response = Trainings().post_create_training(**self.data)
        new_training_data = new_training_response.json()
        new_training_id = int(new_training_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/trainings/', 
                            ""
                        )\
                        .replace("/", ""))
        assert new_training_response.status_code==201

    def test_b_get_retrieve_training(self):
        global new_training_id 
        get_training_response = Trainings().get_training(new_training_id)
        get_training_data = get_training_response.json()
        get_data_id = int(get_training_data["api_url"]\
                                .replace(
                                    'https://full.mindsight.com.br/stone/api/v1/trainings/', 
                                    ""
                                )\
                                .replace("/", ""))
        assert get_training_response.status_code==200

    def test_c_patch_update_training(self):
        global new_training_id 
        self.update_data["_id"] = new_training_id
        patch_training_response = Trainings().patch_edit_training(**self.update_data)
        patch_training_data = patch_training_response.json()
        new_training_id = int(patch_training_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/trainings/', 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_training_response.status_code==200

    def test_d_put_edit_training(self):
        global new_training_id 
        self.update_data["_id"] = new_training_id
        self.update_data["old_status"] = "concluded"
        self.update_data["status"] = "concluded"
        put_training_response = Trainings().put_edit_training(**self.update_data)
        put_training_data = put_training_response.json()
        new_training_id = int(put_training_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/trainings/', 
                            ""
                        )\
                        .replace("/", ""))
        assert put_training_response.status_code==200

    def test_e_delete_training(self):
        global new_training_id 
        deleted_bonus = Trainings().delete_training(new_training_id)
        assert deleted_bonus.status_code==204
