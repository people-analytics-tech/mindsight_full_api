from mindsight_full_api import PerformanceLabels
from datetime import datetime
import unittest
from mindsight_full_api.settings import API_ENDPOINT_PERFORMANCE_LABELS
from mindsight_full_api.utils.aux_functions import generate_url

new_performance_labels_id = None

class TestMindFullPerformanceLabels(unittest.TestCase):
    data = {
        "key": 13,
        "score_description": "6",
        "color": "#FFFFFF",
        "color_comparative": "#000000",
        "scores": None,
    }
    update_data = {
        "key": 13,
        "score_description": "7",
        "color": "#FFFFFF",
        "color_comparative": "#000000",
        "scores": None,
    }
    
    def test_a_post_create_performance_labels(self):
        global new_performance_labels_id 
        new_performance_labels_response = PerformanceLabels().post_create_performance_labels(**self.data)
        new_performance_labels_data = new_performance_labels_response.json()
        new_performance_labels_id = int(new_performance_labels_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_PERFORMANCE_LABELS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert new_performance_labels_response.status_code==201

    def test_b_get_retrieve_performance_labels(self):
        global new_performance_labels_id 
        get_performance_labels_response = PerformanceLabels().get_performance_labels(new_performance_labels_id)
        get_performance_labels_data = get_performance_labels_response.json()
        assert get_performance_labels_response.status_code==200

    def test_c_patch_update_performance_labels(self):
        global new_performance_labels_id 
        self.update_data["_id"] = new_performance_labels_id
        patch_performance_labels_response = PerformanceLabels().patch_edit_performance_labels(**self.update_data)
        patch_performance_labels_data = patch_performance_labels_response.json()
        new_performance_labels_id = int(patch_performance_labels_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_PERFORMANCE_LABELS, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_performance_labels_response.status_code==200

    #TODO
    #Open ticket this method is returning 500
    # def test_put_edit_performance_labels(self):
    #     global new_performance_labels_id 
    #     self.update_data["_id"] = new_performance_labels_id
    #     self.update_data["performance_labels"] = 3000.50
    #     put_performance_labels_response = PerformanceLabels().put_edit_performance_labels(**self.update_data)
    #     put_performance_labels_data = put_performance_labels_response.json()
    #     new_performance_labels_id = int(put_performance_labels_data["api_url"]\
    #                     .replace(
    #                         generate_url(API_ENDPOINT_SHARES, ""), 
    #                         ""
    #                     )\
    #                     .replace("/", ""))
    #     assert put_performance_labels_response.status_code==200

    def test_d_delete_performance_labels(self):
        global new_performance_labels_id 
        deleted_bonus = PerformanceLabels().delete_performance_labels(new_performance_labels_id)
        assert deleted_bonus.status_code==204


TestMindFullPerformanceLabels().test_a_post_create_performance_labels()
PerformanceLabels().get_list_performance_labels().get_all().results