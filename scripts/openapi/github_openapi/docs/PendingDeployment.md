# PendingDeployment

Details of a deployment that is waiting for protection rules to pass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**PendingDeploymentEnvironment**](PendingDeploymentEnvironment.md) |  | 
**wait_timer** | **int** | The set duration of the wait timer | 
**wait_timer_started_at** | **datetime** | The time that the wait timer began. | 
**current_user_can_approve** | **bool** | Whether the currently authenticated user can approve the deployment | 
**reviewers** | [**List[PendingDeploymentReviewersInner]**](PendingDeploymentReviewersInner.md) | The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed. | 

## Example

```python
from github_openapi.models.pending_deployment import PendingDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of PendingDeployment from a JSON string
pending_deployment_instance = PendingDeployment.from_json(json)
# print the JSON string representation of the object
print(PendingDeployment.to_json())

# convert the object into a dict
pending_deployment_dict = pending_deployment_instance.to_dict()
# create an instance of PendingDeployment from a dict
pending_deployment_from_dict = PendingDeployment.from_dict(pending_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


