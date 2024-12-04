# vektis_api.OndernemingApi

All URIs are relative to *https://test-agb-api.vektis.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**onderneming_basisinformatie**](OndernemingApi.md#onderneming_basisinformatie) | **GET** /v2/ondernemingen/{agbcode} | Raadplegen van basisinformatie van een onderneming
[**onderneming_basisinformatie_0**](OndernemingApi.md#onderneming_basisinformatie_0) | **GET** /v2/ondernemingen/{agbcode}/{peildatum} | Raadplegen van basisinformatie van een onderneming op peildatum
[**onderneming_onderneming_organisatie_v2**](OndernemingApi.md#onderneming_onderneming_organisatie_v2) | **GET** /v2/ondernemingen/{agbcode}/relaties/organisatie | Raadplegen vestigingen bij een onderneming
[**onderneming_onderneming_organisatie_v2_0**](OndernemingApi.md#onderneming_onderneming_organisatie_v2_0) | **GET** /v2/ondernemingen/{agbcode}/relaties/organisatie/{peildatum} | Raadplegen vestigingen bij een onderneming op peildatum
[**onderneming_onderneming_relaties_totaal_v2**](OndernemingApi.md#onderneming_onderneming_relaties_totaal_v2) | **GET** /v2/ondernemingen/{agbcode}/relaties/totaal | Raadplegen van alle relaties van een onderneming
[**onderneming_onderneming_relaties_v2**](OndernemingApi.md#onderneming_onderneming_relaties_v2) | **GET** /v2/ondernemingen/{agbcode}/relaties | Raadplegen van huidige actieve relaties van een onderneming
[**onderneming_onderneming_relaties_v2_0**](OndernemingApi.md#onderneming_onderneming_relaties_v2_0) | **GET** /v2/ondernemingen/{agbcode}/relaties/{peildatum} | Raadplegen van actieve relaties van een onderneming op peildatum
[**onderneming_zorgpartij_mutaties**](OndernemingApi.md#onderneming_zorgpartij_mutaties) | **GET** /v2/ondernemingen/mutaties/{vanaf} | Raadplegen van ondernemingen met mutaties
[**onderneming_zorgpartij_mutaties_0**](OndernemingApi.md#onderneming_zorgpartij_mutaties_0) | **GET** /v2/ondernemingen/mutaties/{zorgsoort}/{vanaf} | Raadplegen van ondernemingen met mutaties binnen het opgegeven zorgsoort.


# **onderneming_basisinformatie**
> VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming onderneming_basisinformatie(agbcode, authorization)

Raadplegen van basisinformatie van een onderneming

Op basis van een gegeven AGB-code wordt de basisinformatie van de betreffende onderneming opgehaald en teruggegeven. <br />  Deze basisinformatie vertelt wie de onderneming is, waarvoor deze gekwalificeerd is, waar deze gevestigd is en hoe deze bereikbaar is. <br />  Het betreft adressen, communicatiegegevens, erkenningen en kwalificaties die op dit moment actief zijn. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming
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
    api_instance = vektis_api.OndernemingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van basisinformatie van een onderneming
        api_response = api_instance.onderneming_basisinformatie(agbcode, authorization)
        print("The response of OndernemingApi->onderneming_basisinformatie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_basisinformatie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming**](VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onderneming |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_basisinformatie_0**
> VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming onderneming_basisinformatie_0(agbcode, peildatum, authorization)

Raadplegen van basisinformatie van een onderneming op peildatum

Op basis van een gegeven AGB-code en peildatum wordt de basisinformatie van de betreffende onderneming opgehaald en teruggegeven. <br />  Deze basisinformatie vertelt wie de onderneming is, waarvoor deze gekwalificeerd is, waar deze gevestigd is en hoe deze bereikbaar is. <br />  Het betreft adressen, communicatiegegevens, erkenningen en kwalificaties waarvan de peildatum binnen de geldigheidsperiode valt. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming
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
    api_instance = vektis_api.OndernemingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    peildatum = 'peildatum_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van basisinformatie van een onderneming op peildatum
        api_response = api_instance.onderneming_basisinformatie_0(agbcode, peildatum, authorization)
        print("The response of OndernemingApi->onderneming_basisinformatie_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_basisinformatie_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **peildatum** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming**](VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOnderneming.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onderneming |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_onderneming_organisatie_v2**
> VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie onderneming_onderneming_organisatie_v2(agbcode, authorization)

Raadplegen vestigingen bij een onderneming

Op basis van een gegeven AGB-code van een onderneming of een vestiging en peildatum worden de onderneming gegevens opgehaald en teruggegeven.  <br />  Daarnaast worden ook de vestigingen van de onderneming teruggegeven. <br />  Het betreft vestigingen die op dit moment actief zijn.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie
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
    api_instance = vektis_api.OndernemingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen vestigingen bij een onderneming
        api_response = api_instance.onderneming_onderneming_organisatie_v2(agbcode, authorization)
        print("The response of OndernemingApi->onderneming_onderneming_organisatie_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_onderneming_organisatie_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie**](VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onderneming |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden, Onderneming niet actief, Onderneming bevat geen actieve vestigingen |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_onderneming_organisatie_v2_0**
> VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie onderneming_onderneming_organisatie_v2_0(agbcode, peildatum, authorization)

Raadplegen vestigingen bij een onderneming op peildatum

Op basis van een gegeven AGB-code van een onderneming of een vestiging en peildatum worden de onderneming gegevens opgehaald en teruggegeven.  <br />  Daarnaast worden ook de vestigingen van de onderneming teruggegeven. <br />  Het betreft vestigingen waarvan de peildatum binnen de geldigheidsperiode valt.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_onderneming_onderneming_organisatie import VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie
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
    api_instance = vektis_api.OndernemingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    peildatum = 'peildatum_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen vestigingen bij een onderneming op peildatum
        api_response = api_instance.onderneming_onderneming_organisatie_v2_0(agbcode, peildatum, authorization)
        print("The response of OndernemingApi->onderneming_onderneming_organisatie_v2_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_onderneming_organisatie_v2_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **peildatum** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie**](VektisAGBWebAPIRaadplegenDataContractsV2OndernemingOndernemingOrganisatie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onderneming |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden, Onderneming niet actief, Onderneming bevat geen actieve vestigingen |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_onderneming_relaties_totaal_v2**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties onderneming_onderneming_relaties_totaal_v2(agbcode, authorization)

Raadplegen van alle relaties van een onderneming

Op basis van een gegeven AGB-code worden de relaties van de betreffende onderneming opgehaald en teruggegeven. <br />  De relaties met andere ondernemingen, vestigingen en zorgverleners die direct aan de onderneming gekoppeld zijn worden getoond. <br />  Het betreft alle relaties, dus actieve, reeds beëindigde en eventueel toekomstige relaties.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties import VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties
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
    api_instance = vektis_api.OndernemingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van alle relaties van een onderneming
        api_response = api_instance.onderneming_onderneming_relaties_totaal_v2(agbcode, authorization)
        print("The response of OndernemingApi->onderneming_onderneming_relaties_totaal_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_onderneming_relaties_totaal_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties**](VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relaties |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**404** | AGB-code niet gevonden, Zorgpartij niet actief, Geen relaties gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_onderneming_relaties_v2**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties onderneming_onderneming_relaties_v2(agbcode, authorization)

Raadplegen van huidige actieve relaties van een onderneming

Op basis van een gegeven AGB-code worden de relaties van de betreffende onderneming opgehaald en teruggegeven. <br />  De relaties met andere ondernemingen, vestigingen en zorgverleners die direct aan de onderneming gekoppeld zijn worden getoond. <br />  Het betreft relaties die op dit moment actief zijn.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties import VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties
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
    api_instance = vektis_api.OndernemingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van huidige actieve relaties van een onderneming
        api_response = api_instance.onderneming_onderneming_relaties_v2(agbcode, authorization)
        print("The response of OndernemingApi->onderneming_onderneming_relaties_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_onderneming_relaties_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties**](VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relaties |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**404** | AGB-code niet gevonden, Zorgpartij niet actief, Geen relaties gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_onderneming_relaties_v2_0**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties onderneming_onderneming_relaties_v2_0(agbcode, peildatum, authorization)

Raadplegen van actieve relaties van een onderneming op peildatum

Op basis van een gegeven AGB-code en peildatum worden de relaties van de betreffende onderneming opgehaald en teruggegeven. <br />  De relaties met andere ondernemingen, vestigingen en zorgverleners die direct aan de onderneming gekoppeld zijn worden getoond. <br />  Het betreft relaties waarvan de peildatum binnen de geldigheidsperiode valt.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties import VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties
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
    api_instance = vektis_api.OndernemingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    peildatum = 'peildatum_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van actieve relaties van een onderneming op peildatum
        api_response = api_instance.onderneming_onderneming_relaties_v2_0(agbcode, peildatum, authorization)
        print("The response of OndernemingApi->onderneming_onderneming_relaties_v2_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_onderneming_relaties_v2_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **peildatum** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties**](VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relaties |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**404** | AGB-code niet gevonden, Zorgpartij niet actief, Geen relaties gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_zorgpartij_mutaties**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties onderneming_zorgpartij_mutaties(vanaf, authorization)

Raadplegen van ondernemingen met mutaties

Op basis van een gegeven peildatum worden de ondernemingen die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v1_zorgpartij_zorgpartij_mutaties import VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties
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
    api_instance = vektis_api.OndernemingApi(api_client)
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van ondernemingen met mutaties
        api_response = api_instance.onderneming_zorgpartij_mutaties(vanaf, authorization)
        print("The response of OndernemingApi->onderneming_zorgpartij_mutaties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_zorgpartij_mutaties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vanaf** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties**](VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mutaties |  -  |
**400** | Ongeldige peildatum |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onderneming_zorgpartij_mutaties_0**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties onderneming_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)

Raadplegen van ondernemingen met mutaties binnen het opgegeven zorgsoort.

Op basis van een gegeven peildatum en zorgsoort worden de ondernemingen die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br />  Alleen de ondernemingen met de betreffende zorgsoort worden teruggegeven.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v1_zorgpartij_zorgpartij_mutaties import VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties
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
    api_instance = vektis_api.OndernemingApi(api_client)
    zorgsoort = 'zorgsoort_example' # str | 
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van ondernemingen met mutaties binnen het opgegeven zorgsoort.
        api_response = api_instance.onderneming_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)
        print("The response of OndernemingApi->onderneming_zorgpartij_mutaties_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OndernemingApi->onderneming_zorgpartij_mutaties_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zorgsoort** | **str**|  | 
 **vanaf** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties**](VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mutaties |  -  |
**400** | Ongeldige peildatum of zorgsoort |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

