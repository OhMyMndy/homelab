# ReposCreateOrUpdateFileContents409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**metadata** | [**RepositoryRuleViolationErrorMetadata**](RepositoryRuleViolationErrorMetadata.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_create_or_update_file_contents409_response import ReposCreateOrUpdateFileContents409Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateOrUpdateFileContents409Response from a JSON string
repos_create_or_update_file_contents409_response_instance = ReposCreateOrUpdateFileContents409Response.from_json(json)
# print the JSON string representation of the object
print(ReposCreateOrUpdateFileContents409Response.to_json())

# convert the object into a dict
repos_create_or_update_file_contents409_response_dict = repos_create_or_update_file_contents409_response_instance.to_dict()
# create an instance of ReposCreateOrUpdateFileContents409Response from a dict
repos_create_or_update_file_contents409_response_from_dict = ReposCreateOrUpdateFileContents409Response.from_dict(repos_create_or_update_file_contents409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


