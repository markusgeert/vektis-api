# VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang_agb_code** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer een AGBCode geldig is | 
**einde_agb_code** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer de AGBCode geldig is | [optional] 
**aanvang_relatie** | **datetime** | DATUMAANVANG, dateTime, Datum tot en met wanneer een relatie geldig is | 
**einde_relatie** | **datetime** | DATUMEINDE, dateTime, Datum vanaf wanneer een relatie geldig is | [optional] 
**agb_code** | **str** | CODE, length &#x3D; 8 numeriek in een string, AGBCode | 
**bezoek_adres** | [**VektisAGBWebAPIRaadplegenDataContractsV2OndernemingAdres**](VektisAGBWebAPIRaadplegenDataContractsV2OndernemingAdres.md) |  | 
**naam** | **str** | HANDELSNAAM1, maxLength &#x3D; 150, Eerste handelsnaam waaronder de vestiging bekend is bij het handelsregister | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_vestiging_organisatie import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_vestiging_organisatie_instance = VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_vestiging_organisatie_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_vestiging_organisatie_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_vestiging_organisatie_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2OndernemingVestigingOrganisatie.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_vestiging_organisatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


