# DeploymentWorkflowRun1HeadRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_url** | **str** |  | [optional] 
**assignees_url** | **str** |  | [optional] 
**blobs_url** | **str** |  | [optional] 
**branches_url** | **str** |  | [optional] 
**collaborators_url** | **str** |  | [optional] 
**comments_url** | **str** |  | [optional] 
**commits_url** | **str** |  | [optional] 
**compare_url** | **str** |  | [optional] 
**contents_url** | **str** |  | [optional] 
**contributors_url** | **str** |  | [optional] 
**deployments_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**downloads_url** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**fork** | **bool** |  | [optional] 
**forks_url** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**git_commits_url** | **str** |  | [optional] 
**git_refs_url** | **str** |  | [optional] 
**git_tags_url** | **str** |  | [optional] 
**hooks_url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**issue_comment_url** | **str** |  | [optional] 
**issue_events_url** | **str** |  | [optional] 
**issues_url** | **str** |  | [optional] 
**keys_url** | **str** |  | [optional] 
**labels_url** | **str** |  | [optional] 
**languages_url** | **str** |  | [optional] 
**merges_url** | **str** |  | [optional] 
**milestones_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**notifications_url** | **str** |  | [optional] 
**owner** | [**WebhooksSponsorshipMaintainer**](WebhooksSponsorshipMaintainer.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**pulls_url** | **str** |  | [optional] 
**releases_url** | **str** |  | [optional] 
**stargazers_url** | **str** |  | [optional] 
**statuses_url** | **str** |  | [optional] 
**subscribers_url** | **str** |  | [optional] 
**subscription_url** | **str** |  | [optional] 
**tags_url** | **str** |  | [optional] 
**teams_url** | **str** |  | [optional] 
**trees_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.deployment_workflow_run1_head_repository import DeploymentWorkflowRun1HeadRepository

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentWorkflowRun1HeadRepository from a JSON string
deployment_workflow_run1_head_repository_instance = DeploymentWorkflowRun1HeadRepository.from_json(json)
# print the JSON string representation of the object
print(DeploymentWorkflowRun1HeadRepository.to_json())

# convert the object into a dict
deployment_workflow_run1_head_repository_dict = deployment_workflow_run1_head_repository_instance.to_dict()
# create an instance of DeploymentWorkflowRun1HeadRepository from a dict
deployment_workflow_run1_head_repository_from_dict = DeploymentWorkflowRun1HeadRepository.from_dict(deployment_workflow_run1_head_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


