# LinkWithType

Hypermedia Link with Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from github_openapi.models.link_with_type import LinkWithType

# TODO update the JSON string below
json = "{}"
# create an instance of LinkWithType from a JSON string
link_with_type_instance = LinkWithType.from_json(json)
# print the JSON string representation of the object
print(LinkWithType.to_json())

# convert the object into a dict
link_with_type_dict = link_with_type_instance.to_dict()
# create an instance of LinkWithType from a dict
link_with_type_from_dict = LinkWithType.from_dict(link_with_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


