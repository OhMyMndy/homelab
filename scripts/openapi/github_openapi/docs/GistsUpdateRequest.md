# GistsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the gist. | [optional] 
**files** | [**Dict[str, GistsUpdateRequestFilesValue]**](GistsUpdateRequestFilesValue.md) | The gist files to be updated, renamed, or deleted. Each &#x60;key&#x60; must match the current filename (including extension) of the targeted gist file. For example: &#x60;hello.py&#x60;.  To delete a file, set the whole file to null. For example: &#x60;hello.py : null&#x60;. The file will also be deleted if the specified object does not contain at least one of &#x60;content&#x60; or &#x60;filename&#x60;. | [optional] 

## Example

```python
from github_openapi.models.gists_update_request import GistsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GistsUpdateRequest from a JSON string
gists_update_request_instance = GistsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GistsUpdateRequest.to_json())

# convert the object into a dict
gists_update_request_dict = gists_update_request_instance.to_dict()
# create an instance of GistsUpdateRequest from a dict
gists_update_request_from_dict = GistsUpdateRequest.from_dict(gists_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


