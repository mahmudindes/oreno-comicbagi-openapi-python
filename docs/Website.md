# Website


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**host** | **str** |  | 
**name** | **str** |  | 
**item_language_count** | **int** |  | 
**link_count** | **int** |  | 

## Example

```python
from comicbagi_openapi.models.website import Website

# TODO update the JSON string below
json = "{}"
# create an instance of Website from a JSON string
website_instance = Website.from_json(json)
# print the JSON string representation of the object
print(Website.to_json())

# convert the object into a dict
website_dict = website_instance.to_dict()
# create an instance of Website from a dict
website_form_dict = website.from_dict(website_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


