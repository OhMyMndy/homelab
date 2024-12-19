# EnvironmentApprovalsEnvironmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the environment. | [optional] 
**node_id** | **str** |  | [optional] 
**name** | **str** | The name of the environment. | [optional] 
**url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**created_at** | **datetime** | The time that the environment was created, in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | The time that the environment was last updated, in ISO 8601 format. | [optional] 

## Example

```python
from github_openapi.models.environment_approvals_environments_inner import EnvironmentApprovalsEnvironmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApprovalsEnvironmentsInner from a JSON string
environment_approvals_environments_inner_instance = EnvironmentApprovalsEnvironmentsInner.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApprovalsEnvironmentsInner.to_json())

# convert the object into a dict
environment_approvals_environments_inner_dict = environment_approvals_environments_inner_instance.to_dict()
# create an instance of EnvironmentApprovalsEnvironmentsInner from a dict
environment_approvals_environments_inner_from_dict = EnvironmentApprovalsEnvironmentsInner.from_dict(environment_approvals_environments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


