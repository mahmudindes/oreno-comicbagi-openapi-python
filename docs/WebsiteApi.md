# comicbagi_openapi.WebsiteApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_website**](WebsiteApi.md#add_website) | **POST** /rest/websites | Add website.
[**add_website_item_language**](WebsiteApi.md#add_website_item_language) | **POST** /rest/websites/{websiteHost}/item-languages | Add website item language.
[**delete_website**](WebsiteApi.md#delete_website) | **DELETE** /rest/websites/{host} | Delete website.
[**delete_website_item_language**](WebsiteApi.md#delete_website_item_language) | **DELETE** /rest/websites/{websiteHost}/item-languages/{lang} | Delete website item language.
[**get_website**](WebsiteApi.md#get_website) | **GET** /rest/websites/{host} | Get website.
[**get_website_item_language**](WebsiteApi.md#get_website_item_language) | **GET** /rest/websites/{websiteHost}/item-languages/{lang} | Get website item language.
[**list_website**](WebsiteApi.md#list_website) | **GET** /rest/websites | List website.
[**list_website_item_language**](WebsiteApi.md#list_website_item_language) | **GET** /rest/websites/{websiteHost}/item-languages | List website item language.
[**update_website**](WebsiteApi.md#update_website) | **PATCH** /rest/websites/{host} | Update website.
[**update_website_item_language**](WebsiteApi.md#update_website_item_language) | **PATCH** /rest/websites/{websiteHost}/item-languages/{lang} | Update website item language.


# **add_website**
> Website add_website(new_website)

Add website.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.new_website import NewWebsite
from comicbagi_openapi.models.website import Website
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicbagi_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    new_website = comicbagi_openapi.NewWebsite() # NewWebsite | 

    try:
        # Add website.
        api_response = api_instance.add_website(new_website)
        print("The response of WebsiteApi->add_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->add_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_website** | [**NewWebsite**](NewWebsite.md)|  | 

### Return type

[**Website**](Website.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Website added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_website_item_language**
> WebsiteItemLanguage add_website_item_language(website_host, new_website_item_language)

Add website item language.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.new_website_item_language import NewWebsiteItemLanguage
from comicbagi_openapi.models.website_item_language import WebsiteItemLanguage
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicbagi_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    website_host = 'website_host_example' # str | 
    new_website_item_language = comicbagi_openapi.NewWebsiteItemLanguage() # NewWebsiteItemLanguage | 

    try:
        # Add website item language.
        api_response = api_instance.add_website_item_language(website_host, new_website_item_language)
        print("The response of WebsiteApi->add_website_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->add_website_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_host** | **str**|  | 
 **new_website_item_language** | [**NewWebsiteItemLanguage**](NewWebsiteItemLanguage.md)|  | 

### Return type

[**WebsiteItemLanguage**](WebsiteItemLanguage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Website item language added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website**
> delete_website(host)

Delete website.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicbagi_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    host = 'host_example' # str | 

    try:
        # Delete website.
        api_instance.delete_website(host)
    except Exception as e:
        print("Exception when calling WebsiteApi->delete_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Website deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website_item_language**
> delete_website_item_language(website_host, lang)

Delete website item language.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicbagi_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    website_host = 'website_host_example' # str | 
    lang = 'lang_example' # str | 

    try:
        # Delete website item language.
        api_instance.delete_website_item_language(website_host, lang)
    except Exception as e:
        print("Exception when calling WebsiteApi->delete_website_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_host** | **str**|  | 
 **lang** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Website item language deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website**
> Website get_website(host)

Get website.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.website import Website
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    host = 'host_example' # str | 

    try:
        # Get website.
        api_response = api_instance.get_website(host)
        print("The response of WebsiteApi->get_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->get_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 

### Return type

[**Website**](Website.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_item_language**
> WebsiteItemLanguage get_website_item_language(website_host, lang)

Get website item language.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.website_item_language import WebsiteItemLanguage
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    website_host = 'website_host_example' # str | 
    lang = 'lang_example' # str | 

    try:
        # Get website item language.
        api_response = api_instance.get_website_item_language(website_host, lang)
        print("The response of WebsiteApi->get_website_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->get_website_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_host** | **str**|  | 
 **lang** | **str**|  | 

### Return type

[**WebsiteItemLanguage**](WebsiteItemLanguage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website item language gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_website**
> List[Website] list_website(page=page, limit=limit, order=order, order_by=order_by)

List website.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.website import Website
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List website.
        api_response = api_instance.list_website(page=page, limit=limit, order=order, order_by=order_by)
        print("The response of WebsiteApi->list_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->list_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Website]**](Website.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_website_item_language**
> List[WebsiteItemLanguage] list_website_item_language(website_host, page=page, limit=limit, order=order, order_by=order_by)

List website item language.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.website_item_language import WebsiteItemLanguage
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    website_host = 'website_host_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List website item language.
        api_response = api_instance.list_website_item_language(website_host, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of WebsiteApi->list_website_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->list_website_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_host** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[WebsiteItemLanguage]**](WebsiteItemLanguage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website item language list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website**
> Website update_website(host, set_website)

Update website.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.set_website import SetWebsite
from comicbagi_openapi.models.website import Website
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicbagi_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    host = 'host_example' # str | 
    set_website = comicbagi_openapi.SetWebsite() # SetWebsite | 

    try:
        # Update website.
        api_response = api_instance.update_website(host, set_website)
        print("The response of WebsiteApi->update_website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->update_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 
 **set_website** | [**SetWebsite**](SetWebsite.md)|  | 

### Return type

[**Website**](Website.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website updated. |  * Location -  <br>  |
**204** | Website unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_item_language**
> WebsiteItemLanguage update_website_item_language(website_host, lang, set_website_item_language)

Update website item language.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.set_website_item_language import SetWebsiteItemLanguage
from comicbagi_openapi.models.website_item_language import WebsiteItemLanguage
from comicbagi_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicbagi_openapi.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = comicbagi_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with comicbagi_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicbagi_openapi.WebsiteApi(api_client)
    website_host = 'website_host_example' # str | 
    lang = 'lang_example' # str | 
    set_website_item_language = comicbagi_openapi.SetWebsiteItemLanguage() # SetWebsiteItemLanguage | 

    try:
        # Update website item language.
        api_response = api_instance.update_website_item_language(website_host, lang, set_website_item_language)
        print("The response of WebsiteApi->update_website_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->update_website_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_host** | **str**|  | 
 **lang** | **str**|  | 
 **set_website_item_language** | [**SetWebsiteItemLanguage**](SetWebsiteItemLanguage.md)|  | 

### Return type

[**WebsiteItemLanguage**](WebsiteItemLanguage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website item language updated. |  * Location -  <br>  |
**204** | Website item language unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

