# GistsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the gist | [optional] 
**files** | [**Dict[str, GistsCreateRequestFilesValue]**](GistsCreateRequestFilesValue.md) | Names and content for the files that make up the gist | 
**public** | [**GistsCreateRequestPublic**](GistsCreateRequestPublic.md) |  | [optional] 

## Example

```python
from github_openapi.models.gists_create_request import GistsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GistsCreateRequest from a JSON string
gists_create_request_instance = GistsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GistsCreateRequest.to_json())

# convert the object into a dict
gists_create_request_dict = gists_create_request_instance.to_dict()
# create an instance of GistsCreateRequest from a dict
gists_create_request_from_dict = GistsCreateRequest.from_dict(gists_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


