# comicbagi_openapi.ComicApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comic**](ComicApi.md#add_comic) | **POST** /rest/comics | Add comic.
[**add_comic_destination_link**](ComicApi.md#add_comic_destination_link) | **POST** /rest/comics/{comicCode}/destination-links | Add comic destination link.
[**delete_comic**](ComicApi.md#delete_comic) | **DELETE** /rest/comics/{code} | Delete comic.
[**delete_comic_destination_link**](ComicApi.md#delete_comic_destination_link) | **DELETE** /rest/comics/{comicCode}/destination-links/{ulid} | Delete comic destination link.
[**get_comic**](ComicApi.md#get_comic) | **GET** /rest/comics/{code} | Get comic.
[**get_comic_destination_link**](ComicApi.md#get_comic_destination_link) | **GET** /rest/comics/{comicCode}/destination-links/{ulid} | Get comic destination link.
[**list_comic**](ComicApi.md#list_comic) | **GET** /rest/comics | List comic.
[**list_comic_destination_link**](ComicApi.md#list_comic_destination_link) | **GET** /rest/comics/{comicCode}/destination-links | List comic destination link.
[**update_comic**](ComicApi.md#update_comic) | **PATCH** /rest/comics/{code} | Update comic.
[**update_comic_destination_link**](ComicApi.md#update_comic_destination_link) | **PATCH** /rest/comics/{comicCode}/destination-links/{ulid} | Update comic destination link.


# **add_comic**
> Comic add_comic(new_comic)

Add comic.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.comic import Comic
from comicbagi_openapi.models.new_comic import NewComic
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    new_comic = comicbagi_openapi.NewComic() # NewComic | 

    try:
        # Add comic.
        api_response = api_instance.add_comic(new_comic)
        print("The response of ComicApi->add_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_comic** | [**NewComic**](NewComic.md)|  | 

### Return type

[**Comic**](Comic.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comic_destination_link**
> ComicDestinationLink add_comic_destination_link(comic_code, new_comic_destination_link)

Add comic destination link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.comic_destination_link import ComicDestinationLink
from comicbagi_openapi.models.new_comic_destination_link import NewComicDestinationLink
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    new_comic_destination_link = comicbagi_openapi.NewComicDestinationLink() # NewComicDestinationLink | 

    try:
        # Add comic destination link.
        api_response = api_instance.add_comic_destination_link(comic_code, new_comic_destination_link)
        print("The response of ComicApi->add_comic_destination_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->add_comic_destination_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **new_comic_destination_link** | [**NewComicDestinationLink**](NewComicDestinationLink.md)|  | 

### Return type

[**ComicDestinationLink**](ComicDestinationLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comic destination link added. |  * Location -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic**
> delete_comic(code)

Delete comic.

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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Delete comic.
        api_instance.delete_comic(code)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

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
**204** | Comic deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comic_destination_link**
> delete_comic_destination_link(comic_code, ulid)

Delete comic destination link.

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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Delete comic destination link.
        api_instance.delete_comic_destination_link(comic_code, ulid)
    except Exception as e:
        print("Exception when calling ComicApi->delete_comic_destination_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 

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
**204** | Comic destination link deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic**
> Comic get_comic(code)

Get comic.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.comic import Comic
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    code = 'code_example' # str | 

    try:
        # Get comic.
        api_response = api_instance.get_comic(code)
        print("The response of ComicApi->get_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**Comic**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comic_destination_link**
> ComicDestinationLink get_comic_destination_link(comic_code, ulid)

Get comic destination link.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.comic_destination_link import ComicDestinationLink
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 

    try:
        # Get comic destination link.
        api_response = api_instance.get_comic_destination_link(comic_code, ulid)
        print("The response of ComicApi->get_comic_destination_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->get_comic_destination_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 

### Return type

[**ComicDestinationLink**](ComicDestinationLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic destination link gets. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic**
> List[Comic] list_comic(page=page, limit=limit, order=order, order_by=order_by, destination_link=destination_link)

List comic.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.comic import Comic
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    destination_link = ['destination_link_example'] # List[str] |  (optional)

    try:
        # List comic.
        api_response = api_instance.list_comic(page=page, limit=limit, order=order, order_by=order_by, destination_link=destination_link)
        print("The response of ComicApi->list_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **destination_link** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Comic]**](Comic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_comic_destination_link**
> List[ComicDestinationLink] list_comic_destination_link(comic_code, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)

List comic destination link.

### Example


```python
import comicbagi_openapi
from comicbagi_openapi.models.comic_destination_link import ComicDestinationLink
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    order_by = ['order_by_example'] # List[str] |  (optional)
    link_website_host = ['link_website_host_example'] # List[str] |  (optional)
    link_relative_reference = ['link_relative_reference_example'] # List[str] |  (optional)
    link_href = ['link_href_example'] # List[str] |  (optional)

    try:
        # List comic destination link.
        api_response = api_instance.list_comic_destination_link(comic_code, page=page, limit=limit, order=order, order_by=order_by, link_website_host=link_website_host, link_relative_reference=link_relative_reference, link_href=link_href)
        print("The response of ComicApi->list_comic_destination_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->list_comic_destination_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | [**List[str]**](str.md)|  | [optional] 
 **link_website_host** | [**List[str]**](str.md)|  | [optional] 
 **link_relative_reference** | [**List[str]**](str.md)|  | [optional] 
 **link_href** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ComicDestinationLink]**](ComicDestinationLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic destination link list. |  * X-Total-Count -  <br>  * X-Pagination-Limit -  <br>  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic**
> Comic update_comic(code, set_comic)

Update comic.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.comic import Comic
from comicbagi_openapi.models.set_comic import SetComic
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    code = 'code_example' # str | 
    set_comic = comicbagi_openapi.SetComic() # SetComic | 

    try:
        # Update comic.
        api_response = api_instance.update_comic(code, set_comic)
        print("The response of ComicApi->update_comic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **set_comic** | [**SetComic**](SetComic.md)|  | 

### Return type

[**Comic**](Comic.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic updated. |  * Location -  <br>  |
**204** | Comic unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comic_destination_link**
> ComicDestinationLink update_comic_destination_link(comic_code, ulid, set_comic_destination_link)

Update comic destination link.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import comicbagi_openapi
from comicbagi_openapi.models.comic_destination_link import ComicDestinationLink
from comicbagi_openapi.models.set_comic_destination_link import SetComicDestinationLink
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
    api_instance = comicbagi_openapi.ComicApi(api_client)
    comic_code = 'comic_code_example' # str | 
    ulid = 'ulid_example' # str | 
    set_comic_destination_link = comicbagi_openapi.SetComicDestinationLink() # SetComicDestinationLink | 

    try:
        # Update comic destination link.
        api_response = api_instance.update_comic_destination_link(comic_code, ulid, set_comic_destination_link)
        print("The response of ComicApi->update_comic_destination_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComicApi->update_comic_destination_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comic_code** | **str**|  | 
 **ulid** | **str**|  | 
 **set_comic_destination_link** | [**SetComicDestinationLink**](SetComicDestinationLink.md)|  | 

### Return type

[**ComicDestinationLink**](ComicDestinationLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comic destination link updated. |  * Location -  <br>  |
**204** | Comic destination link unmodified. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

