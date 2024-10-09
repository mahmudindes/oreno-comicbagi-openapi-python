# SetComicDestinationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_website_host** | **str** |  | [optional] 
**link_relative_reference** | **str** |  | [optional] 
**released_at** | **datetime** |  | [optional] 

## Example

```python
from comicbagi_openapi.models.set_comic_destination_link import SetComicDestinationLink

# TODO update the JSON string below
json = "{}"
# create an instance of SetComicDestinationLink from a JSON string
set_comic_destination_link_instance = SetComicDestinationLink.from_json(json)
# print the JSON string representation of the object
print(SetComicDestinationLink.to_json())

# convert the object into a dict
set_comic_destination_link_dict = set_comic_destination_link_instance.to_dict()
# create an instance of SetComicDestinationLink from a dict
set_comic_destination_link_form_dict = set_comic_destination_link.from_dict(set_comic_destination_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


