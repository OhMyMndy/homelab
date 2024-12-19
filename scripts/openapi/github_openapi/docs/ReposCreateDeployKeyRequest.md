# ReposCreateDeployKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A name for the key. | [optional] 
**key** | **str** | The contents of the key. | 
**read_only** | **bool** | If &#x60;true&#x60;, the key will only be able to read repository contents. Otherwise, the key will be able to read and write.      Deploy keys with write access can perform the same actions as an organization member with admin access, or a collaborator on a personal repository. For more information, see \&quot;[Repository permission levels for an organization](https://docs.github.com/articles/repository-permission-levels-for-an-organization/)\&quot; and \&quot;[Permission levels for a user account repository](https://docs.github.com/articles/permission-levels-for-a-user-account-repository/).\&quot; | [optional] 

## Example

```python
from github_openapi.models.repos_create_deploy_key_request import ReposCreateDeployKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateDeployKeyRequest from a JSON string
repos_create_deploy_key_request_instance = ReposCreateDeployKeyRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateDeployKeyRequest.to_json())

# convert the object into a dict
repos_create_deploy_key_request_dict = repos_create_deploy_key_request_instance.to_dict()
# create an instance of ReposCreateDeployKeyRequest from a dict
repos_create_deploy_key_request_from_dict = ReposCreateDeployKeyRequest.from_dict(repos_create_deploy_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


