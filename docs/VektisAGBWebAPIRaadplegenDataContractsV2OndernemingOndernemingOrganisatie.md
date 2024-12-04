# VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang_agb_code** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer een AGBCode geldig is | 
**einde_agb_code** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer de AGBCode geldig is | [optional] 
**agb_code** | **str** | CODE, length &#x3D; 8 numeriek in een string, AGBCode | 
**correspondentie_adres** | [**VektisAGBWebAPIRaadplegenDataContractsV2OndernemingAdres**](VektisAGBWebAPIRaadplegenDataContractsV2OndernemingAdres.md) |  | [optional] 
**naam** | **str** | HANDELSNAAM1, maxLength &#x3D; 150, Eerste handelsnaam waaronder de onderneming bekend is bij het handelsregister | 
**vestigingen** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie]**](VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie.md) | Lijst van actieve vestigingen op peildatum | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie_instance = VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


