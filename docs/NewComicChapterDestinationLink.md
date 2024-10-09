# NewComicChapterDestinationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_website_host** | **str** |  | 
**link_relative_reference** | **str** |  | [optional] 
**released_at** | **datetime** |  | [optional] 

## Example

```python
from comicbagi_openapi.models.new_comic_chapter_destination_link import NewComicChapterDestinationLink

# TODO update the JSON string below
json = "{}"
# create an instance of NewComicChapterDestinationLink from a JSON string
new_comic_chapter_destination_link_instance = NewComicChapterDestinationLink.from_json(json)
# print the JSON string representation of the object
print(NewComicChapterDestinationLink.to_json())

# convert the object into a dict
new_comic_chapter_destination_link_dict = new_comic_chapter_destination_link_instance.to_dict()
# create an instance of NewComicChapterDestinationLink from a dict
new_comic_chapter_destination_link_form_dict = new_comic_chapter_destination_link.from_dict(new_comic_chapter_destination_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


