# coding: utf-8

"""
    Vektis.AGB.WebAPI.Raadplegen (test-agb-api.vektis.nl/) v2

    De raadpleegdienst biedt de mogelijkheid voor diverse bevragingen op AGB. De informatie die beschikbaar is, kan gebruikt worden voor het aanvragen van AGB-codes met de aanvraagdienst.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartij import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij
from typing import Optional, Set
from typing_extensions import Self

class VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen(BaseModel):
    """
    VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen
    """ # noqa: E501
    paginanummer: Optional[StrictInt] = Field(default=None, alias="Paginanummer")
    paginagrootte: Optional[StrictInt] = Field(default=None, alias="Paginagrootte")
    totaalpaginas: Optional[StrictInt] = Field(default=None, alias="Totaalpaginas")
    totaalrecords: Optional[StrictInt] = Field(default=None, alias="Totaalrecords")
    data: Optional[List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij]] = Field(default=None, alias="Data")
    succeeded: Optional[StrictBool] = Field(default=None, alias="Succeeded")
    errors: Optional[List[StrictStr]] = Field(default=None, alias="Errors")
    message: Optional[StrictStr] = Field(default=None, alias="Message")
    __properties: ClassVar[List[str]] = ["Paginanummer", "Paginagrootte", "Totaalpaginas", "Totaalrecords", "Data", "Succeeded", "Errors", "Message"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['Data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Paginanummer": obj.get("Paginanummer"),
            "Paginagrootte": obj.get("Paginagrootte"),
            "Totaalpaginas": obj.get("Totaalpaginas"),
            "Totaalrecords": obj.get("Totaalrecords"),
            "Data": [VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij.from_dict(_item) for _item in obj["Data"]] if obj.get("Data") is not None else None,
            "Succeeded": obj.get("Succeeded"),
            "Errors": obj.get("Errors"),
            "Message": obj.get("Message")
        })
        return _obj


