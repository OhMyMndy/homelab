# GistsGet403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**GistsGet403ResponseBlock**](GistsGet403ResponseBlock.md) |  | [optional] 
**message** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.gists_get403_response import GistsGet403Response

# TODO update the JSON string below
json = "{}"
# create an instance of GistsGet403Response from a JSON string
gists_get403_response_instance = GistsGet403Response.from_json(json)
# print the JSON string representation of the object
print(GistsGet403Response.to_json())

# convert the object into a dict
gists_get403_response_dict = gists_get403_response_instance.to_dict()
# create an instance of GistsGet403Response from a dict
gists_get403_response_from_dict = GistsGet403Response.from_dict(gists_get403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


