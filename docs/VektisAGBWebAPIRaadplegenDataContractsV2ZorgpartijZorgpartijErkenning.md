# VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer de erkenning geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer de erkenning geldig is | [optional] 
**code** | **str** | ERKENNINGTYPE, length &#x3D; 6 numeriek in een string, Code erkenning, waarde komt voor in codelijst AGB029 of in referentiegegevens &#39;erkenningen&#39; | 
**omschrijving** | **str** | BETEKENIS, maxLength &#x3D; 255, Omschrijving van het erkenningtype | 
**registratie_nummer** | **str** | REFERENTIE, maxLength &#x3D; 32, Nummer, code of lidmaatschapsnummer van de erkenning zoals dat bij de erkenner bekend is | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning_instance = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


