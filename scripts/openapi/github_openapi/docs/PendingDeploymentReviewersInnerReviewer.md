# PendingDeploymentReviewersInnerReviewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | [optional] 
**login** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**avatar_url** | **str** |  | 
**gravatar_id** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**followers_url** | **str** |  | 
**following_url** | **str** |  | 
**gists_url** | **str** |  | 
**starred_url** | **str** |  | 
**subscriptions_url** | **str** |  | 
**organizations_url** | **str** |  | 
**repos_url** | **str** |  | 
**events_url** | **str** |  | 
**received_events_url** | **str** |  | 
**type** | **str** |  | 
**site_admin** | **bool** |  | 
**starred_at** | **str** |  | [optional] 
**user_view_type** | **str** |  | [optional] 
**slug** | **str** |  | 
**description** | **str** |  | 
**privacy** | **str** |  | [optional] 
**notification_setting** | **str** |  | [optional] 
**permission** | **str** |  | 
**permissions** | [**TeamPermissions**](TeamPermissions.md) |  | [optional] 
**members_url** | **str** |  | 
**repositories_url** | **str** |  | 
**parent** | [**NullableTeamSimple**](NullableTeamSimple.md) |  | 

## Example

```python
from github_openapi.models.pending_deployment_reviewers_inner_reviewer import PendingDeploymentReviewersInnerReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of PendingDeploymentReviewersInnerReviewer from a JSON string
pending_deployment_reviewers_inner_reviewer_instance = PendingDeploymentReviewersInnerReviewer.from_json(json)
# print the JSON string representation of the object
print(PendingDeploymentReviewersInnerReviewer.to_json())

# convert the object into a dict
pending_deployment_reviewers_inner_reviewer_dict = pending_deployment_reviewers_inner_reviewer_instance.to_dict()
# create an instance of PendingDeploymentReviewersInnerReviewer from a dict
pending_deployment_reviewers_inner_reviewer_from_dict = PendingDeploymentReviewersInnerReviewer.from_dict(pending_deployment_reviewers_inner_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


