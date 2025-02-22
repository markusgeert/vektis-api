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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgpartij_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgsoort import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort
from typing import Optional, Set
from typing_extensions import Self

class VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij(BaseModel):
    """
    VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij
    """ # noqa: E501
    agb_code: StrictStr = Field(description="De uitgegeven AGBCode, 8 cijfers inclusief de voorloopnul", alias="AGBCode")
    aanvang: datetime = Field(description="DATUMAANVANG, dateTime, Datum vanaf wanneer het communicatiegegeven geldig is", alias="Aanvang")
    einde: Optional[datetime] = Field(default=None, description="DATUMEINDE, dateTime, Datum tot en met wanneer het communicatiegegeven geldig is", alias="Einde")
    zorgsoort: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort = Field(alias="Zorgsoort")
    type: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType = Field(alias="Type")
    __properties: ClassVar[List[str]] = ["AGBCode", "Aanvang", "Einde", "Zorgsoort", "Type"]

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
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of zorgsoort
        if self.zorgsoort:
            _dict['Zorgsoort'] = self.zorgsoort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['Type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AGBCode": obj.get("AGBCode"),
            "Aanvang": obj.get("Aanvang"),
            "Einde": obj.get("Einde"),
            "Zorgsoort": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.from_dict(obj["Zorgsoort"]) if obj.get("Zorgsoort") is not None else None,
            "Type": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.from_dict(obj["Type"]) if obj.get("Type") is not None else None
        })
        return _obj


