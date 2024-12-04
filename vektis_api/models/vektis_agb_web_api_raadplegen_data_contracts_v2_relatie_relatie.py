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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_relatie_rol import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_relatie_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgaanbod import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgaanbod
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgpartij_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType
from typing import Optional, Set
from typing_extensions import Self

class VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie(BaseModel):
    """
    
    """ # noqa: E501
    aanvang: datetime = Field(description="DATUMAANVANG, dateTime, Datum vanaf wanneer een relatie geldig is", alias="Aanvang")
    einde: Optional[datetime] = Field(default=None, description="DATUMEINDE, dateTime, Datum vanaf wanneer een relatie geldig is", alias="Einde")
    agb_code: Annotated[str, Field(min_length=8, strict=True, max_length=8)] = Field(description="CODE, length = 8 numeriek in een string, AGBCode", alias="AGBCode")
    naam: Annotated[str, Field(min_length=1, strict=True, max_length=60)] = Field(description="RELATIENAAM, maxLength = 60, Naam die een relatie kan hebben", alias="Naam")
    rol: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol = Field(alias="Rol")
    type: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType = Field(alias="Type")
    zorgaanbod: Optional[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgaanbod] = Field(default=None, alias="Zorgaanbod")
    zorgpartij_type: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType = Field(alias="ZorgpartijType")
    __properties: ClassVar[List[str]] = ["Aanvang", "Einde", "AGBCode", "Naam", "Rol", "Type", "Zorgaanbod", "ZorgpartijType"]

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
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rol
        if self.rol:
            _dict['Rol'] = self.rol.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['Type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of zorgaanbod
        if self.zorgaanbod:
            _dict['Zorgaanbod'] = self.zorgaanbod.to_dict()
        # override the default output from pydantic by calling `to_dict()` of zorgpartij_type
        if self.zorgpartij_type:
            _dict['ZorgpartijType'] = self.zorgpartij_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Aanvang": obj.get("Aanvang"),
            "Einde": obj.get("Einde"),
            "AGBCode": obj.get("AGBCode"),
            "Naam": obj.get("Naam"),
            "Rol": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol.from_dict(obj["Rol"]) if obj.get("Rol") is not None else None,
            "Type": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType.from_dict(obj["Type"]) if obj.get("Type") is not None else None,
            "Zorgaanbod": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgaanbod.from_dict(obj["Zorgaanbod"]) if obj.get("Zorgaanbod") is not None else None,
            "ZorgpartijType": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.from_dict(obj["ZorgpartijType"]) if obj.get("ZorgpartijType") is not None else None
        })
        return _obj

