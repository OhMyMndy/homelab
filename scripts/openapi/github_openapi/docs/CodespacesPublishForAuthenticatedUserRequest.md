# CodespacesPublishForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the new repository. | [optional] 
**private** | **bool** | Whether the new repository should be private. | [optional] [default to False]

## Example

```python
from github_openapi.models.codespaces_publish_for_authenticated_user_request import CodespacesPublishForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesPublishForAuthenticatedUserRequest from a JSON string
codespaces_publish_for_authenticated_user_request_instance = CodespacesPublishForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesPublishForAuthenticatedUserRequest.to_json())

# convert the object into a dict
codespaces_publish_for_authenticated_user_request_dict = codespaces_publish_for_authenticated_user_request_instance.to_dict()
# create an instance of CodespacesPublishForAuthenticatedUserRequest from a dict
codespaces_publish_for_authenticated_user_request_from_dict = CodespacesPublishForAuthenticatedUserRequest.from_dict(codespaces_publish_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


