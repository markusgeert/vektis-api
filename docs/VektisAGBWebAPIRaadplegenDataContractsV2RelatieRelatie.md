# VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer een relatie geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum vanaf wanneer een relatie geldig is | [optional] 
**agb_code** | **str** | CODE, length &#x3D; 8 numeriek in een string, AGBCode | 
**naam** | **str** | RELATIENAAM, maxLength &#x3D; 60, Naam die een relatie kan hebben | 
**rol** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol.md) |  | 
**type** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType.md) |  | 
**zorgaanbod** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgaanbod**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgaanbod.md) |  | [optional] 
**zorgpartij_type** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.md) |  | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_relatie import VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_relatie_instance = VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_relatie_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_relatie_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_relatie_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_relatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


