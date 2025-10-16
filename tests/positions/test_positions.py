from mindsight_full_api import Positions
from datetime import datetime
import unittest
from mindsight_full_api.settings import API_ENDPOINT_POSITIONS
from mindsight_full_api.utils.aux_functions import generate_url

new_positions_id = None
positions_client = Positions()

class TestMindFullPositions(unittest.TestCase):
    data = {
        "_id": 1642407,
        "start_date":  "2010-01-01",
        "person_id": 130333,
        "end_date":  "2023-10-25",
        "uuid":  "70ffedd3-306f-5216-a137-e21a9afc0c6c",
        "name": "LÍDER DE PROCESSOS FINANCEIROS",
        "name_pt_br": "LÍDER DE PROCESSOS FINANCEIROS",
    }
    update_data = {
        "_id": 1642407,
        "start_date":  "2009-01-01",
        "person_id": 130333,
        "end_date":  "2023-10-25",
        "uuid":  "70ffedd3-306f-5216-a137-e21a9afc0c6c",
        "name": "LÍDER DE PROCESSOS FINANCEIROS",
        "name_pt_br": "LÍDER DE PROCESSOS FINANCEIROS",
    }
    
    def test_a_post_create_position(self):
        pass

    def test_b_get_retrieve_position(self):
        global new_positions_id
        get_positions_response = positions_client.get_positions(new_positions_id)
        assert get_positions_response.status_code==200

    def test_c_patch_update_positions(self):
        pass

    #TODO
    def test_put_edit_position(self):
        pass
    
    def test_patch_edit_position(self):
        pass

    def test_d_delete_position(self):
        pass


