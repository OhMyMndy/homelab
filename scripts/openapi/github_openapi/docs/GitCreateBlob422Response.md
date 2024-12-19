# GitCreateBlob422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**documentation_url** | **str** |  | 
**errors** | [**List[ValidationErrorErrorsInner]**](ValidationErrorErrorsInner.md) |  | [optional] 
**status** | **str** |  | [optional] 
**metadata** | [**RepositoryRuleViolationErrorMetadata**](RepositoryRuleViolationErrorMetadata.md) |  | [optional] 

## Example

```python
from github_openapi.models.git_create_blob422_response import GitCreateBlob422Response

# TODO update the JSON string below
json = "{}"
# create an instance of GitCreateBlob422Response from a JSON string
git_create_blob422_response_instance = GitCreateBlob422Response.from_json(json)
# print the JSON string representation of the object
print(GitCreateBlob422Response.to_json())

# convert the object into a dict
git_create_blob422_response_dict = git_create_blob422_response_instance.to_dict()
# create an instance of GitCreateBlob422Response from a dict
git_create_blob422_response_from_dict = GitCreateBlob422Response.from_dict(git_create_blob422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


