# vektis_api.ZorgpartijApi

All URIs are relative to *https://test-agb-api.vektis.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zorgpartij_zorgpartij_mutaties**](ZorgpartijApi.md#zorgpartij_zorgpartij_mutaties) | **GET** /v2/zorgpartijen/mutaties/{vanaf} | Raadplegen van zorgpartijen met mutaties
[**zorgpartij_zorgpartij_mutaties_0**](ZorgpartijApi.md#zorgpartij_zorgpartij_mutaties_0) | **GET** /v2/zorgpartijen/mutaties/{zorgsoort}/{vanaf} | Raadplegen van zorgpartijen met mutaties binnen het opgegeven zorgsoort.
[**zorgpartij_zorgpartijen**](ZorgpartijApi.md#zorgpartij_zorgpartijen) | **GET** /v2/zorgpartijen | Raadplegen van actieve zorgpartijen.
[**zorgpartij_zorgpartijen_0**](ZorgpartijApi.md#zorgpartij_zorgpartijen_0) | **GET** /v2/zorgpartijen/{zorgsoort} | Raadplegen van actieve zorgpartijen binnen het opgegeven zorgsoort.


# **zorgpartij_zorgpartij_mutaties**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties zorgpartij_zorgpartij_mutaties(vanaf, authorization)

Raadplegen van zorgpartijen met mutaties

Op basis van een gegeven peildatum worden de zorgpartijen die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.ZorgpartijApi(api_client)
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van zorgpartijen met mutaties
        api_response = api_instance.zorgpartij_zorgpartij_mutaties(vanaf, authorization)
        print("The response of ZorgpartijApi->zorgpartij_zorgpartij_mutaties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgpartijApi->zorgpartij_zorgpartij_mutaties: %s\n" % e)
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

# **zorgpartij_zorgpartij_mutaties_0**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties zorgpartij_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)

Raadplegen van zorgpartijen met mutaties binnen het opgegeven zorgsoort.

Op basis van een gegeven peildatum en zorgsoort worden de zorgpartijen die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br />  Alleen de zorgpartijen met de betreffende zorgsoort worden teruggegeven.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.ZorgpartijApi(api_client)
    zorgsoort = 'zorgsoort_example' # str | 
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van zorgpartijen met mutaties binnen het opgegeven zorgsoort.
        api_response = api_instance.zorgpartij_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)
        print("The response of ZorgpartijApi->zorgpartij_zorgpartij_mutaties_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgpartijApi->zorgpartij_zorgpartij_mutaties_0: %s\n" % e)
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

# **zorgpartij_zorgpartijen**
> VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen zorgpartij_zorgpartijen(paginanummer, aantal, authorization)

Raadplegen van actieve zorgpartijen.

De actieve zorgpartijen worden opgehaald en teruggegeven. <br />  Een zorgpartij is actief wanner er geen einddatum is geregistreerd, of de einddatum in de toekomst ligt.<br />  Deze gegevens zijn bedoeld om een initiele vulling met de gegevens vanuit het AGB-register mogelijk te maken. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen
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
    api_instance = vektis_api.ZorgpartijApi(api_client)
    paginanummer = 56 # int | 
    aantal = 56 # int | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van actieve zorgpartijen.
        api_response = api_instance.zorgpartij_zorgpartijen(paginanummer, aantal, authorization)
        print("The response of ZorgpartijApi->zorgpartij_zorgpartijen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgpartijApi->zorgpartij_zorgpartijen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginanummer** | **int**|  | 
 **aantal** | **int**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zorgpartijen |  -  |
**400** | Ongeldige peildatum of zorgsoort |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zorgpartij_zorgpartijen_0**
> VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen zorgpartij_zorgpartijen_0(zorgsoort, paginanummer, aantal, authorization)

Raadplegen van actieve zorgpartijen binnen het opgegeven zorgsoort.

Op basis van een gegeven zorgsoort worden de actieve zorgpartijen binnen de geselecteerde zorgsoort opgehaald en teruggegeven. <br />  Een zorgpartij is actief wanner er geen einddatum is geregistreerd, of de einddatum in de toekomst ligt.<br />  Deze gegevens zijn bedoeld om een initiele vulling met de gegevens vanuit het AGB-register mogelijk te maken.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_actieve_zorgpartijen import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen
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
    api_instance = vektis_api.ZorgpartijApi(api_client)
    zorgsoort = 'zorgsoort_example' # str | 
    paginanummer = 56 # int | 
    aantal = 56 # int | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van actieve zorgpartijen binnen het opgegeven zorgsoort.
        api_response = api_instance.zorgpartij_zorgpartijen_0(zorgsoort, paginanummer, aantal, authorization)
        print("The response of ZorgpartijApi->zorgpartij_zorgpartijen_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZorgpartijApi->zorgpartij_zorgpartijen_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zorgsoort** | **str**|  | 
 **paginanummer** | **int**|  | 
 **aantal** | **int**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen**](VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijActieveZorgpartijen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zorgpartijen |  -  |
**400** | Ongeldige peildatum of zorgsoort |  -  |
**401** | U bent niet gemachtigd voor deze methode |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

