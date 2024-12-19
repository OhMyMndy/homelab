# ReposCreateForkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **str** | Optional parameter to specify the organization name if forking into an organization. | [optional] 
**name** | **str** | When forking from an existing repository, a new name for the fork. | [optional] 
**default_branch_only** | **bool** | When forking from an existing repository, fork with only the default branch. | [optional] 

## Example

```python
from github_openapi.models.repos_create_fork_request import ReposCreateForkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateForkRequest from a JSON string
repos_create_fork_request_instance = ReposCreateForkRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateForkRequest.to_json())

# convert the object into a dict
repos_create_fork_request_dict = repos_create_fork_request_instance.to_dict()
# create an instance of ReposCreateForkRequest from a dict
repos_create_fork_request_from_dict = ReposCreateForkRequest.from_dict(repos_create_fork_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


