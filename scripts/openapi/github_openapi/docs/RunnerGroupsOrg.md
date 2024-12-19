# RunnerGroupsOrg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**visibility** | **str** |  | 
**default** | **bool** |  | 
**selected_repositories_url** | **str** | Link to the selected repositories resource for this runner group. Not present unless visibility was set to &#x60;selected&#x60; | [optional] 
**runners_url** | **str** |  | 
**hosted_runners_url** | **str** |  | [optional] 
**inherited** | **bool** |  | 
**inherited_allows_public_repositories** | **bool** |  | [optional] 
**allows_public_repositories** | **bool** |  | 
**workflow_restrictions_read_only** | **bool** | If &#x60;true&#x60;, the &#x60;restricted_to_workflows&#x60; and &#x60;selected_workflows&#x60; fields cannot be modified. | [optional] [default to False]
**restricted_to_workflows** | **bool** | If &#x60;true&#x60;, the runner group will be restricted to running only the workflows specified in the &#x60;selected_workflows&#x60; array. | [optional] [default to False]
**selected_workflows** | **List[str]** | List of workflows the runner group should be allowed to run. This setting will be ignored unless &#x60;restricted_to_workflows&#x60; is set to &#x60;true&#x60;. | [optional] 

## Example

```python
from github_openapi.models.runner_groups_org import RunnerGroupsOrg

# TODO update the JSON string below
json = "{}"
# create an instance of RunnerGroupsOrg from a JSON string
runner_groups_org_instance = RunnerGroupsOrg.from_json(json)
# print the JSON string representation of the object
print(RunnerGroupsOrg.to_json())

# convert the object into a dict
runner_groups_org_dict = runner_groups_org_instance.to_dict()
# create an instance of RunnerGroupsOrg from a dict
runner_groups_org_from_dict = RunnerGroupsOrg.from_dict(runner_groups_org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


