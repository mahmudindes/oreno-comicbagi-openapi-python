# NewComicDestinationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_website_host** | **str** |  | 
**link_relative_reference** | **str** |  | [optional] 
**released_at** | **datetime** |  | [optional] 

## Example

```python
from comicbagi_openapi.models.new_comic_destination_link import NewComicDestinationLink

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicDestinationLink from a JSON string
new_comic_destination_link_instance = NewComicDestinationLink.from_json(json)
# print the JSON string representation of the object
print(NewComicDestinationLink.to_json())

# convert the object into a dict
new_comic_destination_link_dict = new_comic_destination_link_instance.to_dict()
# create an instance of NewComicDestinationLink from a dict
new_comic_destination_link_form_dict = new_comic_destination_link.from_dict(new_comic_destination_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


