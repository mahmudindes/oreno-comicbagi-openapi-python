# ComicDestinationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**ulid** | **str** |  | 
**link_website_host** | **str** |  | 
**link_website_name** | **str** |  | 
**link_relative_reference** | **str** |  | [optional] 
**released_at** | **datetime** |  | [optional] 

## Example

```python
from comicbagi_openapi.models.comic_destination_link import ComicDestinationLink

# TODO update the JSON string below
json = "{}"
# create an instance of ComicDestinationLink from a JSON string
comic_destination_link_instance = ComicDestinationLink.from_json(json)
# print the JSON string representation of the object
print(ComicDestinationLink.to_json())

# convert the object into a dict
comic_destination_link_dict = comic_destination_link_instance.to_dict()
# create an instance of ComicDestinationLink from a dict
comic_destination_link_form_dict = comic_destination_link.from_dict(comic_destination_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


