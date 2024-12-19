# EnvironmentApprovals

An entry in the reviews log for environment deployments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | [**List[EnvironmentApprovalsEnvironmentsInner]**](EnvironmentApprovalsEnvironmentsInner.md) | The list of environments that were approved or rejected | 
**state** | **str** | Whether deployment to the environment(s) was approved or rejected or pending (with comments) | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**comment** | **str** | The comment submitted with the deployment review | 

## Example

```python
from github_openapi.models.environment_approvals import EnvironmentApprovals

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApprovals from a JSON string
environment_approvals_instance = EnvironmentApprovals.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApprovals.to_json())

# convert the object into a dict
environment_approvals_dict = environment_approvals_instance.to_dict()
# create an instance of EnvironmentApprovals from a dict
environment_approvals_from_dict = EnvironmentApprovals.from_dict(environment_approvals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


