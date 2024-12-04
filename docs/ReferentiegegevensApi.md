# vektis_api.ReferentiegegevensApi

All URIs are relative to *https://test-agb-api.vektis.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**referentiegegevens_academische_titels**](ReferentiegegevensApi.md#referentiegegevens_academische_titels) | **GET** /v2/academischetitels | AGB010: Raadplegen van alle geldige academische titels
[**referentiegegevens_adres_types**](ReferentiegegevensApi.md#referentiegegevens_adres_types) | **GET** /v2/adrestypes | AGB022: Raadplegen van alle adrestypes
[**referentiegegevens_arbeids_relatie_rollen**](ReferentiegegevensApi.md#referentiegegevens_arbeids_relatie_rollen) | **GET** /v2/relaties/arbeidsrelatie/zorgverlener/rollen | AGB012: Raadplegen van arbeidsrelatierollen voor een zorgverlener
[**referentiegegevens_beheerders**](ReferentiegegevensApi.md#referentiegegevens_beheerders) | **GET** /v2/beheerders | AGB011: Raadplegen van alle Beheerders/verleners agbcode
[**referentiegegevens_bekend**](ReferentiegegevensApi.md#referentiegegevens_bekend) | **GET** /v2/adres/correspondentie/{postcode}/{huisnummer} | Verifieren van een adres tegen AGB
[**referentiegegevens_communicatie_gegeven_types**](ReferentiegegevensApi.md#referentiegegevens_communicatie_gegeven_types) | **GET** /v2/communicatiegegeventypes | AGB021: Raadplegen van alle communicatiegegeventypes
[**referentiegegevens_doelen**](ReferentiegegevensApi.md#referentiegegevens_doelen) | **GET** /v2/doelen | AGB028: Raadplegen van alle doelen
[**referentiegegevens_erkenningen**](ReferentiegegevensApi.md#referentiegegevens_erkenningen) | **GET** /v2/erkenningen | AGB029: Raadplegen van alle geldige erkenningen
[**referentiegegevens_geslachten**](ReferentiegegevensApi.md#referentiegegevens_geslachten) | **GET** /v2/geslachten | COD046: Raadplegen van alle geldige geslachten
[**referentiegegevens_kwalificaties**](ReferentiegegevensApi.md#referentiegegevens_kwalificaties) | **GET** /v2/kwalificaties | AGB018: Raadplegen van alle geldige kwalificaties
[**referentiegegevens_kwalificaties_onderneming_vestiging**](ReferentiegegevensApi.md#referentiegegevens_kwalificaties_onderneming_vestiging) | **GET** /v2/kwalificaties/ondernemingvestiging | AGB018: Raadplegen van alle geldige kwalificaties voor ondernemingen en vestigingen
[**referentiegegevens_kwalificaties_zorgverlener**](ReferentiegegevensApi.md#referentiegegevens_kwalificaties_zorgverlener) | **GET** /v2/kwalificaties/zorgverlener | AGB018: Raadplegen van alle geldige kwalificaties voor zorgverleners
[**referentiegegevens_landen**](ReferentiegegevensApi.md#referentiegegevens_landen) | **GET** /v2/landen | COD032-NEN: Raadplegen van alle landen
[**referentiegegevens_provincies**](ReferentiegegevensApi.md#referentiegegevens_provincies) | **GET** /v2/provincies | AGB014: Raadplegen van alle provincies
[**referentiegegevens_redenen_einde**](ReferentiegegevensApi.md#referentiegegevens_redenen_einde) | **GET** /v2/redeneneinde | AGB009: Raadplegen van geldige redenen voor beeindigen lidmaatschap(erkenning)
[**referentiegegevens_relatie_rollen**](ReferentiegegevensApi.md#referentiegegevens_relatie_rollen) | **GET** /v2/relatierollen | AGB012: Raadplegen van alle relatierollen
[**referentiegegevens_relatie_types**](ReferentiegegevensApi.md#referentiegegevens_relatie_types) | **GET** /v2/relatietypes | AGB020: Raadplegen van alle relatietypes
[**referentiegegevens_voorvoegsels**](ReferentiegegevensApi.md#referentiegegevens_voorvoegsels) | **GET** /v2/voorvoegsels | NAM040: Raadplegen van alle geldige voorvoegsels
[**referentiegegevens_werkzaam_bij_rollen**](ReferentiegegevensApi.md#referentiegegevens_werkzaam_bij_rollen) | **GET** /v2/relaties/werkzaambij/zorgverlener/rollen | AGB012: Raadplegen van geldige werkzaambijrollen voor een zorgverlener
[**referentiegegevens_zorgpartij_types**](ReferentiegegevensApi.md#referentiegegevens_zorgpartij_types) | **GET** /v2/zorgpartijtypes | AGB001: Raadplegen van alle zorgpartijtypes
[**referentiegegevens_zorgsoorten_onderneming_vestiging**](ReferentiegegevensApi.md#referentiegegevens_zorgsoorten_onderneming_vestiging) | **GET** /v2/zorgsoorten/ondernemingvestiging | AGB016: Raadplegen van alle geldige zorgsoorten voor een onderneming en vestiging
[**referentiegegevens_zorgsoorten_zorgverlener**](ReferentiegegevensApi.md#referentiegegevens_zorgsoorten_zorgverlener) | **GET** /v2/zorgsoorten/zorgverlener | AGB015: Raadplegen van alle geldige zorgsoorten voor een zorgverlener


# **referentiegegevens_academische_titels**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel] referentiegegevens_academische_titels(authorization)

AGB010: Raadplegen van alle geldige academische titels

Geeft een lijst van geldige academische titels terug.<br />  Code ELEMENT maxLength = 12 alfanumeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_academische_titel import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB010: Raadplegen van alle geldige academische titels
        api_response = api_instance.referentiegegevens_academische_titels(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_academische_titels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_academische_titels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAcademischeTitel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Academische titels |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_adres_types**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAdresType] referentiegegevens_adres_types(authorization)

AGB022: Raadplegen van alle adrestypes

Geeft een lijst van geldige adrestypes terug.<br />  Code ELEMENT maxLength = 2 numeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_adres_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAdresType
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB022: Raadplegen van alle adrestypes
        api_response = api_instance.referentiegegevens_adres_types(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_adres_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_adres_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAdresType]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensAdresType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adrestypes |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_arbeids_relatie_rollen**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol] referentiegegevens_arbeids_relatie_rollen(authorization)

AGB012: Raadplegen van arbeidsrelatierollen voor een zorgverlener

Geeft een lijst van geldige arbeidsrelatie rollen terug. Dit is een subset van AGB012.<br />             Code ELEMENT maxLength = 2 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_rol import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB012: Raadplegen van arbeidsrelatierollen voor een zorgverlener
        api_response = api_instance.referentiegegevens_arbeids_relatie_rollen(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_arbeids_relatie_rollen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_arbeids_relatie_rollen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rollen |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_beheerders**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder] referentiegegevens_beheerders(authorization)

AGB011: Raadplegen van alle Beheerders/verleners agbcode

Geeft een lijst van geldige beheerders/verleners agbcode terug.<br />  Code ELEMENT maxLength = 4 numeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_beheerder import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB011: Raadplegen van alle Beheerders/verleners agbcode
        api_response = api_instance.referentiegegevens_beheerders(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_beheerders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_beheerders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensBeheerder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Beheerders |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_bekend**
> str referentiegegevens_bekend(postcode, huisnummer, authorization)

Verifieren van een adres tegen AGB

DEPRECATED : Methode komt in komende Cloud-Release te vervallen, en zal niet worden vervangen.<br />  Op basis van een gegeven postcode/huisnummer combinatie koppelt deze service terug of de gegeven postcode/huisnummer combinatie bekend is bij AGB.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    postcode = 'postcode_example' # str | 
    huisnummer = 'huisnummer_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Verifieren van een adres tegen AGB
        api_response = api_instance.referentiegegevens_bekend(postcode, huisnummer, authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_bekend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_bekend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postcode** | **str**|  | 
 **huisnummer** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Ongeldige invoer postcode, Ongeldige invoer huisnummer |  -  |
**404** | Adres niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_communicatie_gegeven_types**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensCommunicatiegegevenType] referentiegegevens_communicatie_gegeven_types(authorization)

AGB021: Raadplegen van alle communicatiegegeventypes

Geeft een lijst van geldige communicatiegegeventypes terug.<br />  Code ELEMENT maxLength = 2 numeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_communicatiegegeven_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensCommunicatiegegevenType
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB021: Raadplegen van alle communicatiegegeventypes
        api_response = api_instance.referentiegegevens_communicatie_gegeven_types(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_communicatie_gegeven_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_communicatie_gegeven_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensCommunicatiegegevenType]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensCommunicatiegegevenType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Communicatiegegeventypes |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_doelen**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensDoel] referentiegegevens_doelen(authorization)

AGB028: Raadplegen van alle doelen

Geeft een lijst van geldige doelen terug.<br />  Code ELEMENT maxLength = 2 numeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_doel import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensDoel
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB028: Raadplegen van alle doelen
        api_response = api_instance.referentiegegevens_doelen(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_doelen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_doelen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensDoel]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensDoel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Doelen |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_erkenningen**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensErkenning] referentiegegevens_erkenningen(authorization)

AGB029: Raadplegen van alle geldige erkenningen

Geeft een lijst van geldige erkenningen terug.<br />  Code ELEMENT length = 6 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_erkenning import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensErkenning
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB029: Raadplegen van alle geldige erkenningen
        api_response = api_instance.referentiegegevens_erkenningen(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_erkenningen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_erkenningen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensErkenning]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensErkenning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erkenningen |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_geslachten**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht] referentiegegevens_geslachten(authorization)

COD046: Raadplegen van alle geldige geslachten

Geeft een lijst van geldige geslachten terug.<br />  Code ELEMENT maxLength = 1 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_geslacht import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # COD046: Raadplegen van alle geldige geslachten
        api_response = api_instance.referentiegegevens_geslachten(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_geslachten:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_geslachten: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensGeslacht.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Geslachten |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_kwalificaties**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie] referentiegegevens_kwalificaties(authorization)

AGB018: Raadplegen van alle geldige kwalificaties

Geeft een lijst van valide kwalificaties terug.<br />  Code ELEMENT length = 4 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_kwalificatie import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB018: Raadplegen van alle geldige kwalificaties
        api_response = api_instance.referentiegegevens_kwalificaties(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_kwalificaties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_kwalificaties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kwalificaties |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_kwalificaties_onderneming_vestiging**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie] referentiegegevens_kwalificaties_onderneming_vestiging(authorization)

AGB018: Raadplegen van alle geldige kwalificaties voor ondernemingen en vestigingen

Geeft een lijst van geldige kwalificaties voor ondernemingen en vestigingen terug.<br />  Code ELEMENT length = 4 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_kwalificatie import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB018: Raadplegen van alle geldige kwalificaties voor ondernemingen en vestigingen
        api_response = api_instance.referentiegegevens_kwalificaties_onderneming_vestiging(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_kwalificaties_onderneming_vestiging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_kwalificaties_onderneming_vestiging: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kwalificaties |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_kwalificaties_zorgverlener**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie] referentiegegevens_kwalificaties_zorgverlener(authorization)

AGB018: Raadplegen van alle geldige kwalificaties voor zorgverleners

Geeft een lijst van geldige kwalificaties voor zorgverleners terug.<br />  Code ELEMENT length = 4 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_kwalificatie import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB018: Raadplegen van alle geldige kwalificaties voor zorgverleners
        api_response = api_instance.referentiegegevens_kwalificaties_zorgverlener(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_kwalificaties_zorgverlener:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_kwalificaties_zorgverlener: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensKwalificatie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kwalificaties |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_landen**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensLand] referentiegegevens_landen(authorization)

COD032-NEN: Raadplegen van alle landen

Geeft een lijst van geldige landen terug. Zie ook https://www.vektis.nl/standaardisatie/codelijsten/COD032-NEN. <br />  Code ELEMENT length = 2 alfanumeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_land import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensLand
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # COD032-NEN: Raadplegen van alle landen
        api_response = api_instance.referentiegegevens_landen(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_landen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_landen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensLand]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensLand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Landen |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_provincies**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensProvincie] referentiegegevens_provincies(authorization)

AGB014: Raadplegen van alle provincies

Geeft een lijst van geldige provincies terug.<br />  Code ELEMENT length = 1 alfanumeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_provincie import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensProvincie
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB014: Raadplegen van alle provincies
        api_response = api_instance.referentiegegevens_provincies(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_provincies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_provincies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensProvincie]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensProvincie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provincies |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_redenen_einde**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRedenenEinde] referentiegegevens_redenen_einde(authorization)

AGB009: Raadplegen van geldige redenen voor beeindigen lidmaatschap(erkenning)

Geeft een lijst van geldige \"redenen einde\" terug voor het beeindigen van erkenningen.<br />  Code ELEMENT maxLength = 2 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_redenen_einde import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRedenenEinde
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB009: Raadplegen van geldige redenen voor beeindigen lidmaatschap(erkenning)
        api_response = api_instance.referentiegegevens_redenen_einde(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_redenen_einde:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_redenen_einde: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRedenenEinde]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRedenenEinde.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Redenen voor beeindigen erkenningen |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_relatie_rollen**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol] referentiegegevens_relatie_rollen(authorization)

AGB012: Raadplegen van alle relatierollen

Geeft een lijst van geldige relatierollen terug.<br />  Code ELEMENT maxLength = 2 numeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_relatie_rol import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB012: Raadplegen van alle relatierollen
        api_response = api_instance.referentiegegevens_relatie_rollen(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_relatie_rollen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_relatie_rollen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieRol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relatierollen |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_relatie_types**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType] referentiegegevens_relatie_types(authorization)

AGB020: Raadplegen van alle relatietypes

Geeft een lijst van geldige relatietypes terug.<br />  Code ELEMENT maxLength = 2 numeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_relatie_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB020: Raadplegen van alle relatietypes
        api_response = api_instance.referentiegegevens_relatie_types(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_relatie_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_relatie_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relatietypes |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_voorvoegsels**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensVoorvoegsel] referentiegegevens_voorvoegsels(authorization)

NAM040: Raadplegen van alle geldige voorvoegsels

Geeft een lijst van geldige voorvoegsels terug..<br />  Code ELEMENT maxLength = 12 alfanumeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_voorvoegsel import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensVoorvoegsel
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # NAM040: Raadplegen van alle geldige voorvoegsels
        api_response = api_instance.referentiegegevens_voorvoegsels(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_voorvoegsels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_voorvoegsels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensVoorvoegsel]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensVoorvoegsel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Voorvoegsels |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_werkzaam_bij_rollen**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol] referentiegegevens_werkzaam_bij_rollen(authorization)

AGB012: Raadplegen van geldige werkzaambijrollen voor een zorgverlener

Geeft een lijst van geldige werkzaam bij rollen terug. Dit is een subset van AGB012.<br />  Code ELEMENT maxLength = 2 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_rol import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB012: Raadplegen van geldige werkzaambijrollen voor een zorgverlener
        api_response = api_instance.referentiegegevens_werkzaam_bij_rollen(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_werkzaam_bij_rollen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_werkzaam_bij_rollen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rollen |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_zorgpartij_types**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType] referentiegegevens_zorgpartij_types(authorization)

AGB001: Raadplegen van alle zorgpartijtypes

Geeft een lijst van geldige zorgpartijtypes terug.<br />  Code ELEMENT maxLength = 1 numeriek.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgpartij_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB001: Raadplegen van alle zorgpartijtypes
        api_response = api_instance.referentiegegevens_zorgpartij_types(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_zorgpartij_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_zorgpartij_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgpartijType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zorgpartijtypes |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_zorgsoorten_onderneming_vestiging**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort] referentiegegevens_zorgsoorten_onderneming_vestiging(authorization)

AGB016: Raadplegen van alle geldige zorgsoorten voor een onderneming en vestiging

Geeft een lijst van valide zorgsoorten voor een onderneming en vestiging terug.<br />  Code ELEMENT length = 2 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgsoort import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB016: Raadplegen van alle geldige zorgsoorten voor een onderneming en vestiging
        api_response = api_instance.referentiegegevens_zorgsoorten_onderneming_vestiging(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_zorgsoorten_onderneming_vestiging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_zorgsoorten_onderneming_vestiging: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zorgsoorten |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **referentiegegevens_zorgsoorten_zorgverlener**
> List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort] referentiegegevens_zorgsoorten_zorgverlener(authorization)

AGB015: Raadplegen van alle geldige zorgsoorten voor een zorgverlener

Geeft een lijst van geldige zorgsoorten voor een zorgverlener terug.<br />  Code ELEMENT length = 2 numeriek in een string.<br /><br /><h4>Available for Roles</h4>Referentiegegevens

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_zorgsoort import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort
from vektis_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://test-agb-api.vektis.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = vektis_api.Configuration(
    host = "https://test-agb-api.vektis.nl"
)


# Enter a context with an instance of the API client
with vektis_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vektis_api.ReferentiegegevensApi(api_client)
    authorization = 'authorization_example' # str | access token

    try:
        # AGB015: Raadplegen van alle geldige zorgsoorten voor een zorgverlener
        api_response = api_instance.referentiegegevens_zorgsoorten_zorgverlener(authorization)
        print("The response of ReferentiegegevensApi->referentiegegevens_zorgsoorten_zorgverlener:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferentiegegevensApi->referentiegegevens_zorgsoorten_zorgverlener: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| access token | 

### Return type

[**List[VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort]**](VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensZorgsoort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zorgsoorten |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

