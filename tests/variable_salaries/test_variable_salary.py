from mindsight_full_api import VaraibleSalary
from datetime import datetime
import unittest
from mindsight_full_api.settings import API_ENDPOINT_VARIABLE_SALARIES
from mindsight_full_api.utils.aux_functions import generate_url

new_variable_salary_id = None
class TestMindFullVariableSalaryRequests(unittest.TestCase):
    data = {
        "person_id":130333,
        "date": datetime.strptime("2023-03-01", "%Y-%m-%d").date(),
        "variable_salary": 2000,
        "variable_salary_currency": "BRL",
        "reference_value": 2000,
        "reference_value_currency": "BRL",
        "value_achievement": None,
        "raise_type_id": 1,
        "raise_type_old": "initial",
    }
    update_data = {
        "person_id":130333,
        "date": datetime.strptime("2023-04-01", "%Y-%m-%d").date(),
        "variable_salary": 2500,
        "variable_salary_currency": "BRL",
        "reference_value": 2000,
        "reference_value_currency": "BRL",
        "value_achievement": 300,
        "raise_type_id": 2,
        "raise_type_old": "raise",
    }
    
    def test_a_post_create_variable_salary(self):
        global new_variable_salary_id 
        new_variable_salary_response = VaraibleSalary().post_create_variable_salary(**self.data)
        new_variable_salary_data = new_variable_salary_response.json()
        new_variable_salary_id = int(new_variable_salary_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_VARIABLE_SALARIES, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert new_variable_salary_response.status_code==201

    def test_b_get_retrieve_variable_salary(self):
        global new_variable_salary_id 
        get_variable_salary_response = VaraibleSalary().get_variable_salary(new_variable_salary_id)
        get_variable_salary_data = get_variable_salary_response.json()
        get_data_id = int(get_variable_salary_data["api_url"]\
                                .replace(
                                    generate_url(API_ENDPOINT_VARIABLE_SALARIES, ""), 
                                    ""
                                )\
                                .replace("/", ""))
        print(get_data_id)
        assert get_variable_salary_response.status_code==200

    def test_c_patch_update_variable_salary(self):
        global new_variable_salary_id 
        self.update_data["_id"] = new_variable_salary_id
        patch_variable_salary_response = VaraibleSalary().patch_edit_variable_salary(**self.update_data)
        patch_variable_salary_data = patch_variable_salary_response.json()
        new_variable_salary_id = int(patch_variable_salary_data["api_url"]\
                        .replace(
                            generate_url(API_ENDPOINT_VARIABLE_SALARIES, ""), 
                            ""
                        )\
                        .replace("/", ""))
        assert patch_variable_salary_response.status_code==200

    #TODO
    #Open ticket this method is returning 500
    # def test_d_put_edit_variable_salary(self):
    #     global new_variable_salary_id 
    #     self.update_data["_id"] = new_variable_salary_id
    #     self.update_data["variable_salary"] = 3000.50
    #     put_variable_salary_response = VaraibleSalary().put_edit_variable_salary(**self.update_data)
    #     put_variable_salary_data = put_variable_salary_response.json()
    #     new_variable_salary_id = int(put_variable_salary_data["api_url"]\
    #                     .replace(
    #                         'https://full.mindsight.com.br/stone/api/v1/variable_salaries/', 
    #                         ""
    #                     )\
    #                     .replace("/", ""))
    #     assert put_variable_salary_response.status_code==200

    def test_e_delete_variable_salary(self):
        global new_variable_salary_id 
        deleted_bonus = VaraibleSalary().delete_variable_salary(new_variable_salary_id)
        assert deleted_bonus.status_code==204
