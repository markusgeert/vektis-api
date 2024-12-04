# VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agb_code** | **str** | CODE, length &#x3D; 8 numeriek in een string, AGBCode | 
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer een AGBCode geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer de AGBCode geldig is | [optional] 
**voorletters** | **str** | VOORLETTERS, maxLength &#x3D; 6, Initialen van de zorgverlener | 
**tussenvoegsel** | **str** | TUSSENVOEGSEL, maxLength &#x3D; 12, Tussenvoegsel waaronder de zorgverlener bekend is, waarde komt voor in codelijst NAM040 of referentiegegevens &#39;Tussenvoegsels&#39; | [optional] 
**achternaam** | **str** | Achternaam, maxLength &#x3D; 60, Achternaam waaronder de zorgverlener bekend is | 
**geboortenaam_tussenvoegsel** | **str** | GEBOORTENAAMTUSSENVOEGSEL, maxLength &#x3D; 12, Tussenvoegsel die zorgverlener van oorsprong, vanaf de geboorte, heeft, waarde komt voor in codelijst NAM040 of referentiegegevens &#39;tussenvoegsels&#39;\&quot;)] | [optional] 
**geboortenaam** | **str** | GEBOORTENAAM, maxLength &#x3D; 60, Achternaam die zorgverlener van oorsprong, vanaf de geboorte, heeft | [optional] 
**academische_titel** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel.md) |  | [optional] 
**geslacht** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht.md) |  | 
**geboorte_datum** | **datetime** | DATUMGEBOORTE, dateTime, Geboortedatum van de zorgverlener | 
**kwalificaties** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie]**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijKwalificatie.md) | Lijst van actieve kwalificatiegegevens op peildatum | [optional] 
**erkenningen** | [**List[VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning]**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning.md) | Lijst van actieve erkenningen op peildatum | [optional] 
**zorgsoort** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.md) |  | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener import VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener_instance = VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


