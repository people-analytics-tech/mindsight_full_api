from mindsight_full_api import Salary
from datetime import datetime
import unittest
import pytest

new_salary_id = None

class TestMindFullSalaryRequests(unittest.TestCase):
    data = {
        "date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "salary": 2000,
        "person_id":130333,
        "salary_currency": "BRL",
        "raise_type_old": "initial",
        "raise_type_id": 1,
    }
    update_data = {
        "date": datetime.strptime("2023-04-01", "%Y-%m-%d").date(),
        "salary": 2500,
        "person_id":130333,
        "raise_type_old": "raise",
        "salary_currency": "USD",
        "raise_type_id": 2,
    }
    
    def test_a_post_create_salary(self):
        global new_salary_id 
        new_salary_response = Salary().post_create_salary(**self.data)
        new_salary_data = new_salary_response.json()
        new_salary_id = int(new_salary_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/salaries/', 
                            ""
                        )\
                        .replace("/", ""))
        assert new_salary_response.status_code==201

    def test_b_get_retrieve_salary(self):
        global new_salary_id 
        get_salary_response = Salary().get_salary(new_salary_id)
        get_salary_data = get_salary_response.json()
        assert get_salary_response.status_code==200

    def test_c_patch_update_salary(self):
        global new_salary_id 
        self.update_data["_id"] = new_salary_id
        patch_salary_response = Salary().patch_edit_salary(**self.update_data)
        patch_salary_data = patch_salary_response.json()
        new_salary_id = int(patch_salary_data["api_url"]\
                        .replace(
                            'https://full.mindsight.com.br/stone/api/v1/salaries/', 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_salary_response.status_code==200

    #TODO
    #Open ticket this method is returning 500
    # def test_put_edit_salary(self):
    #     global new_salary_id 
    #     self.update_data["_id"] = new_salary_id
    #     self.update_data["salary"] = 3000.50
    #     put_salary_response = Salary().put_edit_salary(**self.update_data)
    #     put_salary_data = put_salary_response.json()
    #     new_salary_id = int(put_salary_data["api_url"]\
    #                     .replace(
    #                         'https://full.mindsight.com.br/stone/api/v1/salaries/', 
    #                         ""
    #                     )\
    #                     .replace("/", ""))
    #     assert put_salary_response.status_code==200

    def test_d_delete_salary(self):
        global new_salary_id 
        deleted_bonus = Salary().delete_salary(new_salary_id)
        assert deleted_bonus.status_code==204
