# ReposCreateOrUpdateEnvironmentRequestReviewersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DeploymentReviewerType**](DeploymentReviewerType.md) |  | [optional] 
**id** | **int** | The id of the user or team who can review the deployment | [optional] 

## Example

```python
from github_openapi.models.repos_create_or_update_environment_request_reviewers_inner import ReposCreateOrUpdateEnvironmentRequestReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateOrUpdateEnvironmentRequestReviewersInner from a JSON string
repos_create_or_update_environment_request_reviewers_inner_instance = ReposCreateOrUpdateEnvironmentRequestReviewersInner.from_json(json)
# print the JSON string representation of the object
print(ReposCreateOrUpdateEnvironmentRequestReviewersInner.to_json())

# convert the object into a dict
repos_create_or_update_environment_request_reviewers_inner_dict = repos_create_or_update_environment_request_reviewers_inner_instance.to_dict()
# create an instance of ReposCreateOrUpdateEnvironmentRequestReviewersInner from a dict
repos_create_or_update_environment_request_reviewers_inner_from_dict = ReposCreateOrUpdateEnvironmentRequestReviewersInner.from_dict(repos_create_or_update_environment_request_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


