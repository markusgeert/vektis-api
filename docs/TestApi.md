# vektis_api.TestApi

All URIs are relative to *https://test-agb-api.vektis.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_get**](TestApi.md#test_get) | **GET** /v2/test/{number} | Test aanroep


# **test_get**
> VektisAGBWebAPIRaadplegenDataContractsTestModel test_get(number, authorization)

Test aanroep

Aanroep bedoeld voor connectiviteitstest. Kan gebruikt worden om te pollen of de service beschikbaar is.

### Example


```python
import vektis_api
from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_test_model import VektisAGBWebAPIRaadplegenDataContractsTestModel
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
    api_instance = vektis_api.TestApi(api_client)
    number = 56 # int | 
    authorization = 'authorization_example' # str | access token

    try:
        # Test aanroep
        api_response = api_instance.test_get(number, authorization)
        print("The response of TestApi->test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->test_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int**|  | 
 **authorization** | **str**| access token | 

### Return type

[**VektisAGBWebAPIRaadplegenDataContractsTestModel**](VektisAGBWebAPIRaadplegenDataContractsTestModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/problem+json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Testmodel |  -  |
**500** | Technische fout |  -  |
**503** | Technische fout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

