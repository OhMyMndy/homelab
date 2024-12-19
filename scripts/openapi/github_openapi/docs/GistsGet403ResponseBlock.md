# GistsGet403ResponseBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.gists_get403_response_block import GistsGet403ResponseBlock

# TODO update the JSON string below
json = "{}"
# create an instance of GistsGet403ResponseBlock from a JSON string
gists_get403_response_block_instance = GistsGet403ResponseBlock.from_json(json)
# print the JSON string representation of the object
print(GistsGet403ResponseBlock.to_json())

# convert the object into a dict
gists_get403_response_block_dict = gists_get403_response_block_instance.to_dict()
# create an instance of GistsGet403ResponseBlock from a dict
gists_get403_response_block_from_dict = GistsGet403ResponseBlock.from_dict(gists_get403_response_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


