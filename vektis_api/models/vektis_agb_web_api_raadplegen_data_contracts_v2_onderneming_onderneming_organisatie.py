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
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_adres import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingAdres
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_vestiging_organisatie import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie
from typing import Optional, Set
from typing_extensions import Self

class VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie(BaseModel):
    """
    
    """ # noqa: E501
    aanvang_agb_code: datetime = Field(description="DATUMAANVANG, dateTime, Datum vanaf wanneer een AGBCode geldig is", alias="AanvangAGBCode")
    einde_agb_code: Optional[datetime] = Field(default=None, description="DATUMEINDE, dateTime, Datum tot en met wanneer de AGBCode geldig is", alias="EindeAGBCode")
    agb_code: Annotated[str, Field(min_length=8, strict=True, max_length=8)] = Field(description="CODE, length = 8 numeriek in een string, AGBCode", alias="AGBCode")
    correspondentie_adres: Optional[VektisAGBWebAPIRaadplegenDataContractsV2OndernemingAdres] = Field(default=None, alias="CorrespondentieAdres")
    naam: Annotated[str, Field(min_length=1, strict=True, max_length=150)] = Field(description="HANDELSNAAM1, maxLength = 150, Eerste handelsnaam waaronder de onderneming bekend is bij het handelsregister", alias="Naam")
    vestigingen: List[VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie] = Field(description="Lijst van actieve vestigingen op peildatum", alias="Vestigingen")
    __properties: ClassVar[List[str]] = ["AanvangAGBCode", "EindeAGBCode", "AGBCode", "CorrespondentieAdres", "Naam", "Vestigingen"]

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
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of correspondentie_adres
        if self.correspondentie_adres:
            _dict['CorrespondentieAdres'] = self.correspondentie_adres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vestigingen (list)
        _items = []
        if self.vestigingen:
            for _item_vestigingen in self.vestigingen:
                if _item_vestigingen:
                    _items.append(_item_vestigingen.to_dict())
            _dict['Vestigingen'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AanvangAGBCode": obj.get("AanvangAGBCode"),
            "EindeAGBCode": obj.get("EindeAGBCode"),
            "AGBCode": obj.get("AGBCode"),
            "CorrespondentieAdres": VektisAGBWebAPIRaadplegenDataContractsV2OndernemingAdres.from_dict(obj["CorrespondentieAdres"]) if obj.get("CorrespondentieAdres") is not None else None,
            "Naam": obj.get("Naam"),
            "Vestigingen": [VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie.from_dict(_item) for _item in obj["Vestigingen"]] if obj.get("Vestigingen") is not None else None
        })
        return _obj

