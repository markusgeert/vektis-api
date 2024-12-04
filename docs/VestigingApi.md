# vektis_api.VestigingApi

All URIs are relative to *https://test-agb-api.vektis.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vestiging_basisinformatie**](VestigingApi.md#vestiging_basisinformatie) | **GET** /v2/vestigingen/{agbcode} | Raadplegen van basisinformatie van een vestiging
[**vestiging_basisinformatie_0**](VestigingApi.md#vestiging_basisinformatie_0) | **GET** /v2/vestigingen/{agbcode}/{peildatum} | Raadplegen van basisinformatie van een vestiging op peildatum
[**vestiging_vestiging_relaties_totaal_v2**](VestigingApi.md#vestiging_vestiging_relaties_totaal_v2) | **GET** /v2/vestigingen/{agbcode}/relaties/totaal | Raadplegen van alle relaties van een vestiging
[**vestiging_vestiging_relaties_v2**](VestigingApi.md#vestiging_vestiging_relaties_v2) | **GET** /v2/vestigingen/{agbcode}/relaties | Raadplegen van huidige actieve relaties van een vestiging
[**vestiging_vestiging_relaties_v2_0**](VestigingApi.md#vestiging_vestiging_relaties_v2_0) | **GET** /v2/vestigingen/{agbcode}/relaties/{peildatum} | Raadplegen van actieve relaties van een vestiging op peildatum
[**vestiging_zorgpartij_mutaties**](VestigingApi.md#vestiging_zorgpartij_mutaties) | **GET** /v2/vestigingen/mutaties/{vanaf} | Raadplegen van vestigingen met mutaties
[**vestiging_zorgpartij_mutaties_0**](VestigingApi.md#vestiging_zorgpartij_mutaties_0) | **GET** /v2/vestigingen/mutaties/{zorgsoort}/{vanaf} | Raadplegen van vestigingen met mutaties binnen het opgegeven zorgsoort.


# **vestiging_basisinformatie**
> VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging vestiging_basisinformatie(agbcode, authorization)

Raadplegen van basisinformatie van een vestiging

Op basis van een gegeven AGB-code wordt de basisinformatie van de betreffende vestiging opgehaald en teruggegeven. <br />  Deze basisinformatie vertelt wie de vestiging is, waarvoor deze gekwalificeerd is, waar deze gevestigd is en hoe deze bereikbaar is. <br />  Het betreft adressen, communicatiegegevens, erkenningen en kwalificaties die op dit moment actief zijn. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging import VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging
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
    api_instance = vektis_api.VestigingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van basisinformatie van een vestiging
        api_response = api_instance.vestiging_basisinformatie(agbcode, authorization)
        print("The response of VestigingApi->vestiging_basisinformatie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VestigingApi->vestiging_basisinformatie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging**](VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vestiging |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vestiging_basisinformatie_0**
> VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging vestiging_basisinformatie_0(agbcode, peildatum, authorization)

Raadplegen van basisinformatie van een vestiging op peildatum

Op basis van een gegeven AGB-code en peildatum wordt de basisinformatie van de betreffende vestiging opgehaald en teruggegeven. <br />  Deze basisinformatie vertelt wie de vestiging is, waarvoor deze gekwalificeerd is, waar deze gevestigd is en hoe deze bereikbaar is. <br />  Het betreft adressen, communicatiegegevens, erkenningen en kwalificaties waarvan de peildatum binnen de geldigheidsperiode valt. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_vestiging_vestiging import VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging
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
    api_instance = vektis_api.VestigingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    peildatum = 'peildatum_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van basisinformatie van een vestiging op peildatum
        api_response = api_instance.vestiging_basisinformatie_0(agbcode, peildatum, authorization)
        print("The response of VestigingApi->vestiging_basisinformatie_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VestigingApi->vestiging_basisinformatie_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agbcode** | **str**|  | 
 **peildatum** | **str**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging**](VektisAGBWebAPIRaadplegenDataContractsV2VestigingVestiging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vestiging |  -  |
**400** | Ongeldige invoer AGB-code |  -  |
**404** | AGB-code niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vestiging_vestiging_relaties_totaal_v2**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties vestiging_vestiging_relaties_totaal_v2(agbcode, authorization)

Raadplegen van alle relaties van een vestiging

Op basis van een gegeven AGB-code worden de relaties van de betreffende vestiging opgehaald en teruggegeven. <br />  De relaties met de onderneming en zorgverleners die direct aan de vestiging gekoppeld zijn worden getoond. <br />  Het betreft alle relaties, dus actieve, reeds beëindigde en eventueel toekomstige relaties.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.VestigingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van alle relaties van een vestiging
        api_response = api_instance.vestiging_vestiging_relaties_totaal_v2(agbcode, authorization)
        print("The response of VestigingApi->vestiging_vestiging_relaties_totaal_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VestigingApi->vestiging_vestiging_relaties_totaal_v2: %s\n" % e)
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

# **vestiging_vestiging_relaties_v2**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties vestiging_vestiging_relaties_v2(agbcode, authorization)

Raadplegen van huidige actieve relaties van een vestiging

Op basis van een gegeven AGB-code worden de relaties van de betreffende vestiging opgehaald en teruggegeven. <br />  De relaties met de onderneming en zorgverleners die direct aan de vestiging gekoppeld zijn worden getoond. <br />  Het betreft relaties die op dit moment actief zijn.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.VestigingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van huidige actieve relaties van een vestiging
        api_response = api_instance.vestiging_vestiging_relaties_v2(agbcode, authorization)
        print("The response of VestigingApi->vestiging_vestiging_relaties_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VestigingApi->vestiging_vestiging_relaties_v2: %s\n" % e)
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
**404** | AGB-code niet gevonden, Vestiging niet actief, Relaties niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vestiging_vestiging_relaties_v2_0**
> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties vestiging_vestiging_relaties_v2_0(agbcode, peildatum, authorization)

Raadplegen van actieve relaties van een vestiging op peildatum

Op basis van een gegeven AGB-code en peildatum worden de relaties van de betreffende vestiging opgehaald en teruggegeven. <br />  De relaties met de onderneming en zorgverleners die direct aan de vestiging gekoppeld zijn worden getoond. <br />  Het betreft relaties waarvan de peildatum binnen de geldigheidsperiode valt.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.VestigingApi(api_client)
    agbcode = 'agbcode_example' # str | 
    peildatum = 'peildatum_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van actieve relaties van een vestiging op peildatum
        api_response = api_instance.vestiging_vestiging_relaties_v2_0(agbcode, peildatum, authorization)
        print("The response of VestigingApi->vestiging_vestiging_relaties_v2_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VestigingApi->vestiging_vestiging_relaties_v2_0: %s\n" % e)
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
**404** | AGB-code niet gevonden, Vestiging niet actief, Relaties niet gevonden |  -  |
**500** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vestiging_zorgpartij_mutaties**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties vestiging_zorgpartij_mutaties(vanaf, authorization)

Raadplegen van vestigingen met mutaties

Op basis van een gegeven peildatum worden de vestigingen die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.VestigingApi(api_client)
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van vestigingen met mutaties
        api_response = api_instance.vestiging_zorgpartij_mutaties(vanaf, authorization)
        print("The response of VestigingApi->vestiging_zorgpartij_mutaties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VestigingApi->vestiging_zorgpartij_mutaties: %s\n" % e)
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

# **vestiging_zorgpartij_mutaties_0**
> VektisAGBWebAPIRaadplegenDataContractsV1ZorgpartijZorgpartijMutaties vestiging_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)

Raadplegen van vestigingen met mutaties binnen het opgegeven zorgsoort.

Op basis van een gegeven peildatum en zorgsoort worden de vestigingen die zijn aangepast sinds de peildatum opgehaald en teruggegeven. <br />  Deze gegevens zijn bedoeld om de gegevens bij de klant te synchroniseren met de gegevens in het AGB-register. <br />  Alleen de vestigingen met de betreffende zorgsoort worden teruggegeven.<br /><br /><h4>Available for Roles</h4>RaadplegenZorgpartij

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
    api_instance = vektis_api.VestigingApi(api_client)
    zorgsoort = 'zorgsoort_example' # str | 
    vanaf = 'vanaf_example' # str | 
    authorization = 'authorization_example' # str | access token

    try:
        # Raadplegen van vestigingen met mutaties binnen het opgegeven zorgsoort.
        api_response = api_instance.vestiging_zorgpartij_mutaties_0(zorgsoort, vanaf, authorization)
        print("The response of VestigingApi->vestiging_zorgpartij_mutaties_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VestigingApi->vestiging_zorgpartij_mutaties_0: %s\n" % e)
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

