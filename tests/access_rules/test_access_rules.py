import unittest

from mindsight_full_api import AccessRules
from mindsight_full_api.settings import API_ENDPOINT_ACCESS_RULES
from mindsight_full_api.utils.aux_functions import generate_url

new_access_rule_id = None


class TestMindAccessRules(unittest.TestCase):
    def test_a_post_create_access_rule(self):
        global new_access_rule_id
        data = {
            "type": "individual",
            "owner": "13556",  # joao.paulo user id
            "access_rule_users": ["13556"],  # joao.paulo user id
            "access_rule_target": 58401,  # pedro.zinner user id
        }
        new_access_rule_response = AccessRules().post_create_access_rules(**data)
        new_access_rule_data = new_access_rule_response.json()
        new_access_rule_id = int(
            new_access_rule_data.get("api_url")
            .replace(generate_url(API_ENDPOINT_ACCESS_RULES, ""), "")
            .replace("/", "")
        )
        print(new_access_rule_id)
        self.assertEqual(new_access_rule_response.status_code, 201)

    def test_b_get_list_access_rules(self):
        global new_access_rule_id
        get_list_response = (
            AccessRules().get_list_access_rules(type="individual").get_all().results
        )
        self.assertTrue(get_list_response)  # Implicit booleanness
        self.assertTrue(
            any(rule["id"] == new_access_rule_id for rule in get_list_response)
        )

    def test_c_delete_access_rule(self):
        global new_access_rule_id
        delete_response = AccessRules().delete_access_rule(str(new_access_rule_id))
        self.assertEqual(delete_response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
