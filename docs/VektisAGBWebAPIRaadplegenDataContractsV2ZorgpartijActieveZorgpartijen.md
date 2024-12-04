# VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paginanummer** | **int** |  | [optional] 
**paginagrootte** | **int** |  | [optional] 
**totaalpaginas** | **int** |  | [optional] 
**totaalrecords** | **int** |  | [optional] 
**data** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij]**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartij.md) |  | [optional] 
**succeeded** | **bool** |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen_instance = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


