# VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer een AGBCode geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer de AGBCode geldig is | [optional] 
**adressen** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres]**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres.md) | Lijst van actieve adressen op peildatum | [optional] 
**agb_code** | **str** | CODE, length &#x3D; 8 numeriek in een string, AGBCode | 
**communicatiegegevens** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven]**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijCommunicatiegegeven.md) | Lijst van actieve communicatiegegevens op peildatum | [optional] 
**erkenningen** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning]**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning.md) | Lijst van actieve erkenningen op peildatum | [optional] 
**handelsnaam** | **str** | HANDELSNAAM1, maxLength &#x3D; 150, Eerste handelsnaam waaronder de vestiging bekend is bij het handelsregister | 
**kwalificaties** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie]**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie.md) | Lijst van actieve kwalificatiegegevens op peildatum | [optional] 
**naam** | **str** | ROEPNAAM, maxLength &#x3D; 60, Naam waaronder de vestiging bekend is of vermeld wil staan | 
**statutaire_naam** | **str** | Statutaire naam vestiging is niet gevuld | [optional] 
**zorgpartij_type** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.md) |  | 
**beheerder_verlener_agb_code** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder.md) |  | 
**zorgsoort** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.md) |  | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging import VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging_instance = VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


