# VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aanvang** | **datetime** | DATUMAANVANG, dateTime, Datum vanaf wanneer het adres geldig is | 
**einde** | **datetime** | DATUMEINDE, dateTime, Datum tot en met wanneer het adres geldig is | [optional] 
**huisnummer** | **int** | HUISNUMMER, Huisnummer van het adres | 
**huisnummer_toevoeging** | **str** | HUISNUMMERTOEVOEGING, maxLength &#x3D; 8, Huisnummertoevoeging van het adres | [optional] 
**land** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensLand**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensLand.md) |  | 
**plaats** | **str** | PLAATS, maxLength &#x3D; 60, Plaatsnaam van het adres | 
**postcode** | **str** | POSTCODE, maxLength &#x3D; 8, Postcode van het adres voor zowel binnenlandse als buitenlandse adressen | 
**provincie** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensProvincie**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensProvincie.md) |  | [optional] 
**straat** | **str** | STRAATNAAM, maxLength &#x3D; 60, Straatnaam van het adres | 
**type** | [**VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAdresType**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAdresType.md) |  | 

## Example

```python
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_adres import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres

# TODO update the JSON string below
json = "{}"
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres from a JSON string
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_adres_instance = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres.from_json(json)
# print the JSON string representation of the object
print(VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres.to_json())

# convert the object into a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_adres_dict = vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_adres_instance.to_dict()
# create an instance of VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres from a dict
vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_adres_from_dict = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijAdres.from_dict(vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_adres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


