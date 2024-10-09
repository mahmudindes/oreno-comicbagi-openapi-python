# comicbagi_openapi.LinkApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_link**](LinkApi.md#add_link) | **POST** /rest/links | Add link.
[**add_link_item_language**](LinkApi.md#add_link_item_language) | **POST** /rest/links/{linkHref}/item-languages | Add link item language.
[**delete_link**](LinkApi.md#delete_link) | **DELETE** /rest/links/{href} | Delete link.
[**delete_link_item_language**](LinkApi.md#delete_link_item_language) | **DELETE** /rest/links/{linkHref}/item-languages/{lang} | Delete link item language.
[**get_link**](LinkApi.md#get_link) | **GET** /rest/links/{href} | Get link.
[**get_link_item_language**](LinkApi.md#get_link_item_language) | **GET** /rest/links/{linkHref}/item-languages/{lang} | Get link item language.
[**list_link**](LinkApi.md#list_link) | **GET** /rest/links | List link.
[**list_link_item_language**](LinkApi.md#list_link_item_language) | **GET** /rest/links/{linkHref}/item-languages | List link item language.
[**update_link**](LinkApi.md#update_link) | **PATCH** /rest/links/{href} | Update link.
[**update_link_item_language**](LinkApi.md#update_link_item_language) | **PATCH** /rest/links/{linkHref}/item-languages/{lang} | Update link item language.


# **add_link**
> Link add_link(new_link)

Add link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.link import Link
from comicbagi_openapi.models.new_link import NewLink
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    new_link = comicbagi_openapi.NewLink() # NewLink | 

    try:
        # Add link.
        api_response = api_instance.add_link(new_link)
        print("The response of LinkApi->add_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->add_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_link** | [**NewLink**](NewLink.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Link added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_link_item_language**
> LinkItemLanguage add_link_item_language(link_href, new_link_item_language)

Add link item language.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.link_item_language import LinkItemLanguage
from comicbagi_openapi.models.new_link_item_language import NewLinkItemLanguage
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    link_href = 'link_href_example' # str | 
    new_link_item_language = comicbagi_openapi.NewLinkItemLanguage() # NewLinkItemLanguage | 

    try:
        # Add link item language.
        api_response = api_instance.add_link_item_language(link_href, new_link_item_language)
        print("The response of LinkApi->add_link_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->add_link_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_href** | **str**|  | 
 **new_link_item_language** | [**NewLinkItemLanguage**](NewLinkItemLanguage.md)|  | 

### Return type

[**LinkItemLanguage**](LinkItemLanguage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Link item language added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_link**
> delete_link(href)

Delete link.

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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    href = 'href_example' # str | 

    try:
        # Delete link.
        api_instance.delete_link(href)
    except Exception as e:
        print("Exception when calling LinkApi->delete_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | **str**|  | 

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
**204** | Link deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_link_item_language**
> delete_link_item_language(link_href, lang)

Delete link item language.

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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    link_href = 'link_href_example' # str | 
    lang = 'lang_example' # str | 

    try:
        # Delete link item language.
        api_instance.delete_link_item_language(link_href, lang)
    except Exception as e:
        print("Exception when calling LinkApi->delete_link_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_href** | **str**|  | 
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
**204** | Link item language deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link**
> Link get_link(href)

Get link.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.link import Link
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    href = 'href_example' # str | 

    try:
        # Get link.
        api_response = api_instance.get_link(href)
        print("The response of LinkApi->get_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->get_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | **str**|  | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_item_language**
> LinkItemLanguage get_link_item_language(link_href, lang)

Get link item language.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.link_item_language import LinkItemLanguage
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    link_href = 'link_href_example' # str | 
    lang = 'lang_example' # str | 

    try:
        # Get link item language.
        api_response = api_instance.get_link_item_language(link_href, lang)
        print("The response of LinkApi->get_link_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->get_link_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_href** | **str**|  | 
 **lang** | **str**|  | 

### Return type

[**LinkItemLanguage**](LinkItemLanguage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link item language gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_link**
> List[Link] list_link(page=page, limit=limit, order=order, order_by=order_by, website_host=website_host, relative_reference=relative_reference, href=href)

List link.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.link import Link
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    website_host = ['website_host_example'] # List[str] |  (optional)
    relative_reference = ['relative_reference_example'] # List[str] |  (optional)
    href = ['href_example'] # List[str] |  (optional)

    try:
        # List link.
        api_response = api_instance.list_link(page=page, limit=limit, order=order, order_by=order_by, website_host=website_host, relative_reference=relative_reference, href=href)
        print("The response of LinkApi->list_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->list_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **website_host** | [**List[str]**](str.md)|  | [optional] 
 **relative_reference** | [**List[str]**](str.md)|  | [optional] 
 **href** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Link]**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_link_item_language**
> List[LinkItemLanguage] list_link_item_language(link_href, page=page, limit=limit, order=order, order_by=order_by)

List link item language.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.link_item_language import LinkItemLanguage
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    link_href = 'link_href_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)

    try:
        # List link item language.
        api_response = api_instance.list_link_item_language(link_href, page=page, limit=limit, order=order, order_by=order_by)
        print("The response of LinkApi->list_link_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->list_link_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_href** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[LinkItemLanguage]**](LinkItemLanguage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link item language list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link**
> Link update_link(href, set_link)

Update link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.link import Link
from comicbagi_openapi.models.set_link import SetLink
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    href = 'href_example' # str | 
    set_link = comicbagi_openapi.SetLink() # SetLink | 

    try:
        # Update link.
        api_response = api_instance.update_link(href, set_link)
        print("The response of LinkApi->update_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->update_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | **str**|  | 
 **set_link** | [**SetLink**](SetLink.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link updated. |  * Location -  <br>  |
**204** | Link unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link_item_language**
> LinkItemLanguage update_link_item_language(link_href, lang, set_link_item_language)

Update link item language.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.link_item_language import LinkItemLanguage
from comicbagi_openapi.models.set_link_item_language import SetLinkItemLanguage
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
    api_instance = comicbagi_openapi.LinkApi(api_client)
    link_href = 'link_href_example' # str | 
    lang = 'lang_example' # str | 
    set_link_item_language = comicbagi_openapi.SetLinkItemLanguage() # SetLinkItemLanguage | 

    try:
        # Update link item language.
        api_response = api_instance.update_link_item_language(link_href, lang, set_link_item_language)
        print("The response of LinkApi->update_link_item_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->update_link_item_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_href** | **str**|  | 
 **lang** | **str**|  | 
 **set_link_item_language** | [**SetLinkItemLanguage**](SetLinkItemLanguage.md)|  | 

### Return type

[**LinkItemLanguage**](LinkItemLanguage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Link item language updated. |  * Location -  <br>  |
**204** | Link item language unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

