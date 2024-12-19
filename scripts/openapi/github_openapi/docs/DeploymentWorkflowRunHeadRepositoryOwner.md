# DeploymentWorkflowRunHeadRepositoryOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**login** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**organizations_url** | **str** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.deployment_workflow_run_head_repository_owner import DeploymentWorkflowRunHeadRepositoryOwner

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentWorkflowRunHeadRepositoryOwner from a JSON string
deployment_workflow_run_head_repository_owner_instance = DeploymentWorkflowRunHeadRepositoryOwner.from_json(json)
# print the JSON string representation of the object
print(DeploymentWorkflowRunHeadRepositoryOwner.to_json())

# convert the object into a dict
deployment_workflow_run_head_repository_owner_dict = deployment_workflow_run_head_repository_owner_instance.to_dict()
# create an instance of DeploymentWorkflowRunHeadRepositoryOwner from a dict
deployment_workflow_run_head_repository_owner_from_dict = DeploymentWorkflowRunHeadRepositoryOwner.from_dict(deployment_workflow_run_head_repository_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


