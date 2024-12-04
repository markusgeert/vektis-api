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
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_academische_titel import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_geslacht import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgsoort import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie
from typing import Optional, Set
from typing_extensions import Self

class VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener(BaseModel):
    """
    
    """ # noqa: E501
    agb_code: Annotated[str, Field(min_length=8, strict=True, max_length=8)] = Field(description="CODE, length = 8 numeriek in een string, AGBCode", alias="AGBCode")
    aanvang: datetime = Field(description="DATUMAANVANG, dateTime, Datum vanaf wanneer een AGBCode geldig is", alias="Aanvang")
    einde: Optional[datetime] = Field(default=None, description="DATUMEINDE, dateTime, Datum tot en met wanneer de AGBCode geldig is", alias="Einde")
    voorletters: Annotated[str, Field(min_length=1, strict=True, max_length=6)] = Field(description="VOORLETTERS, maxLength = 6, Initialen van de zorgverlener", alias="Voorletters")
    tussenvoegsel: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=12)]] = Field(default=None, description="TUSSENVOEGSEL, maxLength = 12, Tussenvoegsel waaronder de zorgverlener bekend is, waarde komt voor in codelijst NAM040 of referentiegegevens 'Tussenvoegsels'", alias="Tussenvoegsel")
    achternaam: Annotated[str, Field(min_length=1, strict=True, max_length=60)] = Field(description="Achternaam, maxLength = 60, Achternaam waaronder de zorgverlener bekend is", alias="Achternaam")
    geboortenaam_tussenvoegsel: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=12)]] = Field(default=None, description="GEBOORTENAAMTUSSENVOEGSEL, maxLength = 12, Tussenvoegsel die zorgverlener van oorsprong, vanaf de geboorte, heeft, waarde komt voor in codelijst NAM040 of referentiegegevens 'tussenvoegsels'\")]", alias="GeboortenaamTussenvoegsel")
    geboortenaam: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="GEBOORTENAAM, maxLength = 60, Achternaam die zorgverlener van oorsprong, vanaf de geboorte, heeft", alias="Geboortenaam")
    academische_titel: Optional[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel] = Field(default=None, alias="AcademischeTitel")
    geslacht: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht = Field(alias="Geslacht")
    geboorte_datum: datetime = Field(description="DATUMGEBOORTE, dateTime, Geboortedatum van de zorgverlener", alias="GeboorteDatum")
    kwalificaties: Optional[List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie]] = Field(default=None, description="Lijst van actieve kwalificatiegegevens op peildatum", alias="Kwalificaties")
    erkenningen: Optional[List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning]] = Field(default=None, description="Lijst van actieve erkenningen op peildatum", alias="Erkenningen")
    zorgsoort: VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort = Field(alias="Zorgsoort")
    __properties: ClassVar[List[str]] = ["AGBCode", "Aanvang", "Einde", "Voorletters", "Tussenvoegsel", "Achternaam", "GeboortenaamTussenvoegsel", "Geboortenaam", "AcademischeTitel", "Geslacht", "GeboorteDatum", "Kwalificaties", "Erkenningen", "Zorgsoort"]

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
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of academische_titel
        if self.academische_titel:
            _dict['AcademischeTitel'] = self.academische_titel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geslacht
        if self.geslacht:
            _dict['Geslacht'] = self.geslacht.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in kwalificaties (list)
        _items = []
        if self.kwalificaties:
            for _item_kwalificaties in self.kwalificaties:
                if _item_kwalificaties:
                    _items.append(_item_kwalificaties.to_dict())
            _dict['Kwalificaties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in erkenningen (list)
        _items = []
        if self.erkenningen:
            for _item_erkenningen in self.erkenningen:
                if _item_erkenningen:
                    _items.append(_item_erkenningen.to_dict())
            _dict['Erkenningen'] = _items
        # override the default output from pydantic by calling `to_dict()` of zorgsoort
        if self.zorgsoort:
            _dict['Zorgsoort'] = self.zorgsoort.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AGBCode": obj.get("AGBCode"),
            "Aanvang": obj.get("Aanvang"),
            "Einde": obj.get("Einde"),
            "Voorletters": obj.get("Voorletters"),
            "Tussenvoegsel": obj.get("Tussenvoegsel"),
            "Achternaam": obj.get("Achternaam"),
            "GeboortenaamTussenvoegsel": obj.get("GeboortenaamTussenvoegsel"),
            "Geboortenaam": obj.get("Geboortenaam"),
            "AcademischeTitel": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel.from_dict(obj["AcademischeTitel"]) if obj.get("AcademischeTitel") is not None else None,
            "Geslacht": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht.from_dict(obj["Geslacht"]) if obj.get("Geslacht") is not None else None,
            "GeboorteDatum": obj.get("GeboorteDatum"),
            "Kwalificaties": [VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie.from_dict(_item) for _item in obj["Kwalificaties"]] if obj.get("Kwalificaties") is not None else None,
            "Erkenningen": [VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning.from_dict(_item) for _item in obj["Erkenningen"]] if obj.get("Erkenningen") is not None else None,
            "Zorgsoort": VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.from_dict(obj["Zorgsoort"]) if obj.get("Zorgsoort") is not None else None
        })
        return _obj

