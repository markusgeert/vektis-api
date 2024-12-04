# VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer het communicatiegegeven geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer het communicatiegegeven geldig is | [optional] 
**doel** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensDoel**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensDoel.md) |  | 
**gegeven** | **str** | NUMMER_URL, maxLength &#x3D; 128, Waarde communicatiegegeven, t.w. een telefoonnummer of een URL | 
**type** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensCommunicatiegegevenType**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensCommunicatiegegevenType.md) |  | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_communicatiegegeven import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_communicatiegegeven_instance = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_communicatiegegeven_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_communicatiegegeven_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_communicatiegegeven_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_communicatiegegeven_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


