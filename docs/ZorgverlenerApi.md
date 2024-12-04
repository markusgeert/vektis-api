# vektis_api.ZorgverlenerApi

All URIs are relative to *https://test-agb-api.vektis.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zorgverlener_basisinformatie**](ZorgverlenerApi.md#zorgverlener_basisinformatie) | **GET** /v2/zorgverleners/{agbcode} | Raadplegen van basisinformatie van een zorgverlener
[**zorgverlener_basisinformatie_0**](ZorgverlenerApi.md#zorgverlener_basisinformatie_0) | **GET** /v2/zorgverleners/{agbcode}/{peildatum} | Raadplegen van basisinformatie van een zorgverlener op peildatum
[**zorgverlener_zorgpartij_mutaties**](ZorgverlenerApi.md#zorgverlener_zorgpartij_mutaties) | **GET** /v2/zorgverleners/mutaties/{vanaf} | Raadplegen van zorgverleners met mutaties
[**zorgverlener_zorgpartij_mutaties_0**](ZorgverlenerApi.md#zorgverlener_zorgpartij_mutaties_0) | **GET** /v2/zorgverleners/mutaties/{zorgsoort}/{vanaf} | Raadplegen van zorgverleners met mutaties binnen het opgegeven zorgsoort.
[**zorgverlener_zorgverlener_relaties_totaal_v2**](ZorgverlenerApi.md#zorgverlener_zorgverlener_relaties_totaal_v2) | **GET** /v2/zorgverleners/{agbcode}/relaties/totaal | Raadplegen van alle relaties van een zorgverlener
[**zorgverlener_zorgverlener_relaties_v2**](ZorgverlenerApi.md#zorgverlener_zorgverlener_relaties_v2) | **GET** /v2/zorgverleners/{agbcode}/relaties | Raadplegen van de huidige actieve relaties van een zorgverlener
[**zorgverlener_zorgverlener_relaties_v2_0**](ZorgverlenerApi.md#zorgverlener_zorgverlener_relaties_v2_0) | **GET** /v2/zorgverleners/{agbcode}/relaties/{peildatum} | Raadplegen relaties van een zorgverlener op peildatum


# **zorgverlener_basisinformatie**
> VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener zorgverlener_basisinformatie(agbcode, authorization)

Raadplegen van basisinformatie van een zorgverlener

Op basis van een gegeven AGB-code wordt de basisinformatie van de betreffende zorgverlener opgehaald en teruggegeven. <br />  Deze basisinformatie vertelt wie de zorgverlener is en waarvoor deze gekwalificeerd is. <br />  Het betreft erkenningen en kwalificaties die op dit moment actief zijn. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener import VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener
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
    api_instance = vektis_api.ZorgverlenerApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van basisinformatie van een zorgverlener
        api_response = api_instance.zorgverlener_basisinformatie(agbcode, authorization)
        print("The response of ZorgverlenerApi->zorgverlener_basisinformatie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgverlenerApi->zorgverlener_basisinformatie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zorgverlener |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zorgverlener_basisinformatie_0**
> VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener zorgverlener_basisinformatie_0(agbcode, peildatum, authorization)

Raadplegen van basisinformatie van een zorgverlener op peildatum

Op basis van een gegeven AGB-code en peildatum wordt de basisinformatie van de betreffende zorgverlener opgehaald en teruggegeven. <br />  Deze basisinformatie vertelt wie de zorgverlener is en waarvoor deze gekwalificeerd is. <br />  Het betreft erkenningen en kwalificaties waarvan de peildatum binnen de geldigheidsperiode valt. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgverlener_zorgverlener import VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener
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
    api_instance = vektis_api.ZorgverlenerApi(api_client)
    agbcode = 'agbcode_example' # str | 
    peildatum = 'peildatum_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van basisinformatie van een zorgverlener op peildatum
        api_response = api_instance.zorgverlener_basisinformatie_0(agbcode, peildatum, authorization)
        print("The response of ZorgverlenerApi->zorgverlener_basisinformatie_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgverlenerApi->zorgverlener_basisinformatie_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **peildatum** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgverlenerZorgverlener.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zorgverlener |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zorgverlener_zorgpartij_mutaties**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties zorgverlener_zorgpartij_mutaties(vanaf, authorization)

Raadplegen van zorgverleners met mutaties

Op basis van een gegeven peildatum worden de zorgverleners die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.ZorgverlenerApi(api_client)
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van zorgverleners met mutaties
        api_response = api_instance.zorgverlener_zorgpartij_mutaties(vanaf, authorization)
        print("The response of ZorgverlenerApi->zorgverlener_zorgpartij_mutaties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgverlenerApi->zorgverlener_zorgpartij_mutaties: %s\n" % e)
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

# **zorgverlener_zorgpartij_mutaties_0**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties zorgverlener_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)

Raadplegen van zorgverleners met mutaties binnen het opgegeven zorgsoort.

Op basis van een gegeven peildatum en zorgsoort worden de zorgverleners die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br />  Alleen de zorgverleners met de betreffende zorgsoort worden teruggegeven.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.ZorgverlenerApi(api_client)
    zorgsoort = 'zorgsoort_example' # str | 
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van zorgverleners met mutaties binnen het opgegeven zorgsoort.
        api_response = api_instance.zorgverlener_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)
        print("The response of ZorgverlenerApi->zorgverlener_zorgpartij_mutaties_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgverlenerApi->zorgverlener_zorgpartij_mutaties_0: %s\n" % e)
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

# **zorgverlener_zorgverlener_relaties_totaal_v2**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties zorgverlener_zorgverlener_relaties_totaal_v2(agbcode, authorization)

Raadplegen van alle relaties van een zorgverlener

Op basis van een gegeven AGB-code worden de relaties van de betreffende zorgverlener opgehaald en teruggegeven. <br />  De actieve relaties met de vestiging(en) en onderneming die direct aan de zorgverlener gekoppeld zijn worden getoond.  <br />  Het betreft alle relaties, dus actieve, reeds beëindigde en eventueel toekomstige relaties.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.ZorgverlenerApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van alle relaties van een zorgverlener
        api_response = api_instance.zorgverlener_zorgverlener_relaties_totaal_v2(agbcode, authorization)
        print("The response of ZorgverlenerApi->zorgverlener_zorgverlener_relaties_totaal_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgverlenerApi->zorgverlener_zorgverlener_relaties_totaal_v2: %s\n" % e)
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
**404** | AGB-code niet gevonden, Zorgverlener niet actief, Geen relaties gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zorgverlener_zorgverlener_relaties_v2**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties zorgverlener_zorgverlener_relaties_v2(agbcode, authorization)

Raadplegen van de huidige actieve relaties van een zorgverlener

Op basis van een gegeven AGB-code worden de relaties van de betreffende zorgverlener opgehaald en teruggegeven. <br />  De actieve relaties met de vestiging(en) en onderneming die direct aan de zorgverlener gekoppeld zijn worden getoond.  <br />  Het betreft relaties die op dit moment actief zijn.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.ZorgverlenerApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van de huidige actieve relaties van een zorgverlener
        api_response = api_instance.zorgverlener_zorgverlener_relaties_v2(agbcode, authorization)
        print("The response of ZorgverlenerApi->zorgverlener_zorgverlener_relaties_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgverlenerApi->zorgverlener_zorgverlener_relaties_v2: %s\n" % e)
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
**404** | AGB-code niet gevonden, Zorgverlener niet actief, Geen relaties gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zorgverlener_zorgverlener_relaties_v2_0**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties zorgverlener_zorgverlener_relaties_v2_0(agbcode, peildatum, authorization)

Raadplegen relaties van een zorgverlener op peildatum

Op basis van een gegeven AGB-code en peildatum worden de relaties van de betreffende zorgverlener opgehaald en teruggegeven. <br />  De actieve relaties met de vestiging(en) en onderneming die direct aan de zorgverlener gekoppeld zijn worden getoond.  <br />  Het betreft relaties waarvan de peildatum binnen de geldigheidsperiode valt.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.ZorgverlenerApi(api_client)
    agbcode = 'agbcode_example' # str | 
    peildatum = 'peildatum_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen relaties van een zorgverlener op peildatum
        api_response = api_instance.zorgverlener_zorgverlener_relaties_v2_0(agbcode, peildatum, authorization)
        print("The response of ZorgverlenerApi->zorgverlener_zorgverlener_relaties_v2_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgverlenerApi->zorgverlener_zorgverlener_relaties_v2_0: %s\n" % e)
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
**404** | AGB-code niet gevonden, Zorgverlener niet actief, Geen relaties gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

