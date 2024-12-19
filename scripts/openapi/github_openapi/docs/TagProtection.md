# TagProtection

Tag protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**pattern** | **str** |  | 

## Example

```python
from github_openapi.models.tag_protection import TagProtection

# TODO update the JSON string below
json = "{}"
# create an instance of TagProtection from a JSON string
tag_protection_instance = TagProtection.from_json(json)
# print the JSON string representation of the object
print(TagProtection.to_json())

# convert the object into a dict
tag_protection_dict = tag_protection_instance.to_dict()
# create an instance of TagProtection from a dict
tag_protection_from_dict = TagProtection.from_dict(tag_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


