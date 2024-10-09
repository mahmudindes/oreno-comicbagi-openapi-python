# LinkItemLanguage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**language_lang** | **str** |  | 
**machine_translate** | **int** |  | [optional] 

## Example

```python
from comicbagi_openapi.models.link_item_language import LinkItemLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of LinkItemLanguage from a JSON string
link_item_language_instance = LinkItemLanguage.from_json(json)
# print the JSON string representation of the object
print(LinkItemLanguage.to_json())

# convert the object into a dict
link_item_language_dict = link_item_language_instance.to_dict()
# create an instance of LinkItemLanguage from a dict
link_item_language_form_dict = link_item_language.from_dict(link_item_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


