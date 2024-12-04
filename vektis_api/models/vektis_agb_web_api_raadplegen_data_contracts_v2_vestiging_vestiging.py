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
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_beheerder import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgpartij_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgsoort import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_communicatiegegeven import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_adres import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie
from typing import Optional, Set
from typing_extensions import Self

class VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging(BaseModel):
    """
    
    """ # noqa: E501
    aanvang: datetime = Field(description="DATUMAANVANG, dateTime, Datum vanaf wanneer een AGBCode geldig is", alias="Aanvang")
    einde: Optional[datetime] = Field(default=None, description="DATUMEINDE, dateTime, Datum tot en met wanneer de AGBCode geldig is", alias="Einde")
    adressen: Optional[List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres]] = Field(default=None, description="Lijst van actieve adressen op peildatum", alias="Adressen")
    agb_code: Annotated[str, Field(min_length=8, strict=True, max_length=8)] = Field(description="CODE, length = 8 numeriek in een string, AGBCode", alias="AGBCode")
    communicatiegegevens: Optional[List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven]] = Field(default=None, description="Lijst van actieve communicatiegegevens op peildatum", alias="Communicatiegegevens")
    erkenningen: Optional[List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning]] = Field(default=None, description="Lijst van actieve erkenningen op peildatum", alias="Erkenningen")
    handelsnaam: Annotated[str, Field(min_length=1, strict=True, max_length=150)] = Field(description="HANDELSNAAM1, maxLength = 150, Eerste handelsnaam waaronder de vestiging bekend is bij het handelsregister", alias="Handelsnaam")
    kwalificaties: Optional[List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie]] = Field(default=None, description="Lijst van actieve kwalificatiegegevens op peildatum", alias="Kwalificaties")
    naam: Annotated[str, Field(min_length=1, strict=True, max_length=60)] = Field(description="ROEPNAAM, maxLength = 60, Naam waaronder de vestiging bekend is of vermeld wil staan", alias="Naam")
    statutaire_naam: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=150)]] = Field(default=None, description="Statutaire naam vestiging is niet gevuld", alias="StatutaireNaam")
    zorgpartij_type: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType = Field(alias="ZorgpartijType")
    beheerder_verlener_agb_code: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder = Field(alias="BeheerderVerlenerAGBCode")
    zorgsoort: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort = Field(alias="Zorgsoort")
    __properties: ClassVar[List[str]] = ["Aanvang", "Einde", "Adressen", "AGBCode", "Communicatiegegevens", "Erkenningen", "Handelsnaam", "Kwalificaties", "Naam", "StatutaireNaam", "ZorgpartijType", "BeheerderVerlenerAGBCode", "Zorgsoort"]

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
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in adressen (list)
        _items = []
        if self.adressen:
            for _item_adressen in self.adressen:
                if _item_adressen:
                    _items.append(_item_adressen.to_dict())
            _dict['Adressen'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in communicatiegegevens (list)
        _items = []
        if self.communicatiegegevens:
            for _item_communicatiegegevens in self.communicatiegegevens:
                if _item_communicatiegegevens:
                    _items.append(_item_communicatiegegevens.to_dict())
            _dict['Communicatiegegevens'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in erkenningen (list)
        _items = []
        if self.erkenningen:
            for _item_erkenningen in self.erkenningen:
                if _item_erkenningen:
                    _items.append(_item_erkenningen.to_dict())
            _dict['Erkenningen'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in kwalificaties (list)
        _items = []
        if self.kwalificaties:
            for _item_kwalificaties in self.kwalificaties:
                if _item_kwalificaties:
                    _items.append(_item_kwalificaties.to_dict())
            _dict['Kwalificaties'] = _items
        # override the default output from pydantic by calling `to_dict()` of zorgpartij_type
        if self.zorgpartij_type:
            _dict['ZorgpartijType'] = self.zorgpartij_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of beheerder_verlener_agb_code
        if self.beheerder_verlener_agb_code:
            _dict['BeheerderVerlenerAGBCode'] = self.beheerder_verlener_agb_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of zorgsoort
        if self.zorgsoort:
            _dict['Zorgsoort'] = self.zorgsoort.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Aanvang": obj.get("Aanvang"),
            "Einde": obj.get("Einde"),
            "Adressen": [VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres.from_dict(_item) for _item in obj["Adressen"]] if obj.get("Adressen") is not None else None,
            "AGBCode": obj.get("AGBCode"),
            "Communicatiegegevens": [VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven.from_dict(_item) for _item in obj["Communicatiegegevens"]] if obj.get("Communicatiegegevens") is not None else None,
            "Erkenningen": [VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning.from_dict(_item) for _item in obj["Erkenningen"]] if obj.get("Erkenningen") is not None else None,
            "Handelsnaam": obj.get("Handelsnaam"),
            "Kwalificaties": [VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie.from_dict(_item) for _item in obj["Kwalificaties"]] if obj.get("Kwalificaties") is not None else None,
            "Naam": obj.get("Naam"),
            "StatutaireNaam": obj.get("StatutaireNaam"),
            "ZorgpartijType": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.from_dict(obj["ZorgpartijType"]) if obj.get("ZorgpartijType") is not None else None,
            "BeheerderVerlenerAGBCode": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder.from_dict(obj["BeheerderVerlenerAGBCode"]) if obj.get("BeheerderVerlenerAGBCode") is not None else None,
            "Zorgsoort": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.from_dict(obj["Zorgsoort"]) if obj.get("Zorgsoort") is not None else None
        })
        return _obj


