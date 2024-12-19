# EnvironmentProtectionRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**type** | **str** |  | 
**wait_timer** | **int** | The amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days). | [optional] 
**prevent_self_review** | **bool** | Whether deployments to this environment can be approved by the user who created the deployment. | [optional] 
**reviewers** | [**List[PendingDeploymentReviewersInner]**](PendingDeploymentReviewersInner.md) | The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed. | [optional] 

## Example

```python
from github_openapi.models.environment_protection_rules_inner import EnvironmentProtectionRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentProtectionRulesInner from a JSON string
environment_protection_rules_inner_instance = EnvironmentProtectionRulesInner.from_json(json)
# print the JSON string representation of the object
print(EnvironmentProtectionRulesInner.to_json())

# convert the object into a dict
environment_protection_rules_inner_dict = environment_protection_rules_inner_instance.to_dict()
# create an instance of EnvironmentProtectionRulesInner from a dict
environment_protection_rules_inner_from_dict = EnvironmentProtectionRulesInner.from_dict(environment_protection_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


