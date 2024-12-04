# VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agb_code** | **str** | De uitgegeven AGBCode, 8 cijfers inclusief de voorloopnul | 
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer het communicatiegegeven geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer het communicatiegegeven geldig is | [optional] 
**zorgsoort** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.md) |  | 
**type** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.md) |  | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartij import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartij_instance = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartij_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartij_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartij_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartij_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


