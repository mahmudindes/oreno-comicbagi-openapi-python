# WebsiteItemLanguage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**language_lang** | **str** |  | 
**machine_translate** | **int** |  | [optional] 

## Example

```python
from comicbagi_openapi.models.website_item_language import WebsiteItemLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteItemLanguage from a JSON string
website_item_language_instance = WebsiteItemLanguage.from_json(json)
# print the JSON string representation of the object
print(WebsiteItemLanguage.to_json())

# convert the object into a dict
website_item_language_dict = website_item_language_instance.to_dict()
# create an instance of WebsiteItemLanguage from a dict
website_item_language_form_dict = website_item_language.from_dict(website_item_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


