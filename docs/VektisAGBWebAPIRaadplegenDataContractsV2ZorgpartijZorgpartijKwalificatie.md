# VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer de kwalificatie geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer de kwalificatie geldig is | [optional] 
**code** | **str** | KWALIFICATIETYPE, length &#x3D; 4 numeriek in een string, Code kwalificatie, waarde komt voor in codelijst AGB018 of in referentiegegevens &#39;kwalificaties&#39; | 
**omschrijving** | **str** | BETEKENIS, maxLength &#x3D; 255, Omschrijving van het kwalificatietype | 
**nictiz_code** | **str** | NICTIZ_ID, maxLength &#x3D; 6, Nictiz code die zorgaanbieders gebruiken voor deze kwalificatie | [optional] 
**patiententerm** | **str** | BETEKENIS, maxLength &#x3D; 255, Patiententerm horend bij de Nictiz code | [optional] 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie_instance = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_kwalificatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


