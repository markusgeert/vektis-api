# VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agb_code** | **str** | CODE, length &#x3D; 8 numeriek in een string, AGBCode | 
**naam** | **str** | ROEPNAAM, maxLength &#x3D; 60, Naam waaronder de zorgpartij bekend is of vermeld wil staan | 
**relaties** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie]**](VektisAGBWebAPIRaadplegenDataContractsV2RelatieRelatie.md) | Lijst van relaties (afhankelijk van parameter) | 
**zorgpartij_type** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.md) |  | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties import VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties_instance = VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


