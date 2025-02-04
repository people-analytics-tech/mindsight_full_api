"""This module provide methods to work with areas entity"""

from datetime import date, datetime
from mindsight_full_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_full_api.settings import (
    API_ENDPOINT_COMPANIES,
    API_ENDPOINT_PEOPLE,
    DATE_FORMAT,
    DATETIME_FORMAT,
)
from mindsight_full_api.utils.aux_functions import generate_url


class Companies(ApiEndpoint):
    """This class abstract the absence endpoint methods
    Reference: https://full.mindsight.com.br/stone/api/v1/docs/#tag/Vinculo-com-empresa
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_COMPANIES)

    def get_list_companies(
        self,
        person__gender: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        person__age_category: str = None,
        person__company_time_category: str = None,
        person__spam_control_category: str = None,
        person__seniority: str = None,
        person__education_degree_category: str = None,
    ) -> ApiPaginationResponse:
        """Get companies data
        https://full.mindsight.com.br/stone/api/v1/docs/#tag/Vinculo-com-empresa/operation/listCompanys

        Args:
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            }
        """

        path = ""
        parameters = {
            "person__gender": person__gender,
            "created__gt": created__gt.strftime(DATETIME_FORMAT)
            if created__gt
            else None,
            "created__lt": created__lt.strftime(DATETIME_FORMAT)
            if created__lt
            else None,
            "modified__gt": modified__gt.strftime(DATETIME_FORMAT)
            if modified__gt
            else None,
            "modified__lt": modified__lt.strftime(DATETIME_FORMAT)
            if modified__lt
            else None,
            "person__age_category": person__age_category,
            "person__company_time_category": person__company_time_category,
            "person__spam_control_category": person__spam_control_category,
            "person__seniority": person__seniority,
            "person__education_degree_category": person__education_degree_category,
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def post_create_bonus(
        self,
        name: str,
        start_date: date,
        person_id: int,
        registration_code: str = None,
        end_date: date = None,
        entrance_type: str = None,
        termination_type: str = None,
        unit_name: str = None,
    ):
        """Create new bonus
        Reference:
            https://full.mindsight.com.br/stone/api/v1/docs/#tag/Bonus/operation/createBonus

        Args:
            start_date (date, Mandatory): Area start date
            end_date (date, Optional): Parent area id
            is_approved (bool, Mandatory): Code of area
            type (str, Mandatory): Name of area
            observations (str, Mandatory): Name of area
            number_of_days (int, Mandatory): Name of area
            person (int, Mandatory): Name of area
        """
        path = ""
        data = {
            "name": name,
            "registration_code": registration_code,
            "start_date": start_date.strftime(DATE_FORMAT),
            "end_date": end_date.strftime(DATE_FORMAT) if end_date else end_date,
            "entrance_type": entrance_type,
            "termination_type": termination_type,
            "unit_name": unit_name,
            "person": generate_url(base_path=API_ENDPOINT_PEOPLE, path=f"/{person_id}"),
        }

        return self._base_requests.post(path=path, data=data)

    def get_bonus(
        self,
        _id: int,
        person__gender: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        person__age_category: str = None,
        person__company_time_category: str = None,
        person__spam_control_category: str = None,
        person__seniority: str = None,
        person__education_degree_category: str = None,
    ) -> dict:
        """Get retrieve bonus
        Reference:
            https://full.mindsight.com.br/stone/api/v1/docs/#tag/Bonus/operation/retrieveBonus

        Args:
            _id (int, Mandatory): Id of area to retrieve
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
        """
        path = f"/{_id}"
        parameters = {
            "person__gender": person__gender,
            "created__gt": created__gt.strftime(DATETIME_FORMAT)
            if created__gt
            else None,
            "created__lt": created__lt.strftime(DATETIME_FORMAT)
            if created__lt
            else None,
            "modified__gt": modified__gt.strftime(DATETIME_FORMAT)
            if modified__gt
            else None,
            "modified__lt": modified__lt.strftime(DATETIME_FORMAT)
            if modified__lt
            else None,
            "person__age_category": person__age_category,
            "person__company_time_category": person__company_time_category,
            "person__spam_control_category": person__spam_control_category,
            "person__seniority": person__seniority,
            "person__education_degree_category": person__education_degree_category,
        }
        return self._base_requests.get(
            path=path,
            parameters=parameters,
        )

    def patch_edit_bonus(
        self,
        _id: int,
        name: str,
        start_date: date,
        person_id: int,
        person__gender: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        person__age_category: str = None,
        person__company_time_category: str = None,
        person__spam_control_category: str = None,
        person__seniority: str = None,
        person__education_degree_category: str = None,
        registration_code: str = None,
        end_date: date = None,
        entrance_type: str = None,
        termination_type: str = None,
        unit_name: str = None,
    ) -> dict:
        """Edit area and last area record
        Reference:
            https://full.mindsight.com.br/stone/api/v1/docs/#tag/Afastamentos/operation/partialUpdateAbsence

        Args:
            _id (int, Mandatory): Area id
            start_date (date, Mandatory): Area start date
            end_date (date, Optional): Parent area id
            is_approved (bool, Mandatory): Code of area
            type (str, Mandatory): Name of area
            observations (str, Mandatory): Name of area
            number_of_days (int, Mandatory): Name of area
            person (int, Mandatory): Name of area
        """
        path = f"/{_id}/"
        data = {
            "name": name,
            "registration_code": registration_code,
            "start_date": start_date.strftime(DATE_FORMAT),
            "end_date": end_date.strftime(DATE_FORMAT) if end_date else end_date,
            "entrance_type": entrance_type,
            "termination_type": termination_type,
            "unit_name": unit_name,
            "person": generate_url(base_path=API_ENDPOINT_PEOPLE, path=f"/{person_id}"),
        }
        parameters = {
            "person__gender": person__gender,
            "created__gt": created__gt.strftime(DATETIME_FORMAT)
            if created__gt
            else None,
            "created__lt": created__lt.strftime(DATETIME_FORMAT)
            if created__lt
            else None,
            "modified__gt": modified__gt.strftime(DATETIME_FORMAT)
            if modified__gt
            else None,
            "modified__lt": modified__lt.strftime(DATETIME_FORMAT)
            if modified__lt
            else None,
            "person__age_category": person__age_category,
            "person__company_time_category": person__company_time_category,
            "person__spam_control_category": person__spam_control_category,
            "person__seniority": person__seniority,
            "person__education_degree_category": person__education_degree_category,
        }
        return self._base_requests.patch(path=path, data=data, parameters=parameters)

    def put_edit_bonus(
        self,
        _id: int,
        name: str,
        start_date: date,
        person_id: int,
        person__gender: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        person__age_category: str = None,
        person__company_time_category: str = None,
        person__spam_control_category: str = None,
        person__seniority: str = None,
        person__education_degree_category: str = None,
        registration_code: str = None,
        end_date: date = None,
        entrance_type: str = None,
        termination_type: str = None,
        unit_name: str = None,
    ) -> dict:
        """Edit absence
        Reference:
            https://full.mindsight.com.br/stone/api/v1/docs/#tag/Afastamentos/operation/updatebonus

        Args:
            _id (int, Mandatory): Area id
            start_date (date, Mandatory): Area start date
            end_date (date, Optional): Parent area id
            is_approved (bool, Mandatory): Code of area
            type (str, Mandatory): Name of area
            observations (str, Mandatory): Name of area
            number_of_days (int, Mandatory): Name of area
            person (int, Mandatory): Name of area
        """
        path = f"/{_id}/"
        data = {
            "name": name,
            "registration_code": registration_code,
            "start_date": start_date.strftime(DATE_FORMAT),
            "end_date": end_date.strftime(DATE_FORMAT) if end_date else end_date,
            "entrance_type": entrance_type,
            "termination_type": termination_type,
            "unit_name": unit_name,
            "person": generate_url(base_path=API_ENDPOINT_PEOPLE, path=f"/{person_id}"),
        }
        parameters = {
            "person__gender": person__gender,
            "created__gt": created__gt.strftime(DATETIME_FORMAT)
            if created__gt
            else None,
            "created__lt": created__lt.strftime(DATETIME_FORMAT)
            if created__lt
            else None,
            "modified__gt": modified__gt.strftime(DATETIME_FORMAT)
            if modified__gt
            else None,
            "modified__lt": modified__lt.strftime(DATETIME_FORMAT)
            if modified__lt
            else None,
            "person__age_category": person__age_category,
            "person__company_time_category": person__company_time_category,
            "person__spam_control_category": person__spam_control_category,
            "person__seniority": person__seniority,
            "person__education_degree_category": person__education_degree_category,
        }
        return self._base_requests.put(path=path, data=data, parameters=parameters)

    def delete_bonus(
        self,
        _id: int,
        person__gender: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        person__age_category: str = None,
        person__company_time_category: str = None,
        person__spam_control_category: str = None,
        person__seniority: str = None,
        person__education_degree_category: str = None,
    ) -> dict:
        """Delete bonus
        Reference:
            https://full.mindsight.com.br/stone/api/v1/docs/#tag/Bonus/operation/destroyBonus

        Args:
            _id (int, Mandatory): Id of area to retrieve
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
        """
        path = f"/{_id}"

        parameters = {
            "person__gender": person__gender,
            "created__gt": created__gt.strftime(DATETIME_FORMAT)
            if created__gt
            else None,
            "created__lt": created__lt.strftime(DATETIME_FORMAT)
            if created__lt
            else None,
            "modified__gt": modified__gt.strftime(DATETIME_FORMAT)
            if modified__gt
            else None,
            "modified__lt": modified__lt.strftime(DATETIME_FORMAT)
            if modified__lt
            else None,
            "person__age_category": person__age_category,
            "person__company_time_category": person__company_time_category,
            "person__spam_control_category": person__spam_control_category,
            "person__seniority": person__seniority,
            "person__education_degree_category": person__education_degree_category,
        }
        return self._base_requests.delete(
            path=path,
            parameters=parameters,
        )
