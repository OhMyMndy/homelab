# ReposCreateOrUpdateEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wait_timer** | **int** | The amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days). | [optional] 
**prevent_self_review** | **bool** | Whether or not a user who created the job is prevented from approving their own job. | [optional] 
**reviewers** | [**List[ReposCreateOrUpdateEnvironmentRequestReviewersInner]**](ReposCreateOrUpdateEnvironmentRequestReviewersInner.md) | The people or teams that may review jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed. | [optional] 
**deployment_branch_policy** | [**DeploymentBranchPolicySettings**](DeploymentBranchPolicySettings.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_create_or_update_environment_request import ReposCreateOrUpdateEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateOrUpdateEnvironmentRequest from a JSON string
repos_create_or_update_environment_request_instance = ReposCreateOrUpdateEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateOrUpdateEnvironmentRequest.to_json())

# convert the object into a dict
repos_create_or_update_environment_request_dict = repos_create_or_update_environment_request_instance.to_dict()
# create an instance of ReposCreateOrUpdateEnvironmentRequest from a dict
repos_create_or_update_environment_request_from_dict = ReposCreateOrUpdateEnvironmentRequest.from_dict(repos_create_or_update_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


