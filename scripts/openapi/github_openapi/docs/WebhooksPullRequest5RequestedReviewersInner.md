# WebhooksPullRequest5RequestedReviewersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** | Unique identifier of the team | 
**login** | **str** |  | 
**name** | **str** | Name of the team | 
**node_id** | **str** |  | [optional] 
**organizations_url** | **str** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** | URL for the team | [optional] 
**description** | **str** | Description of the team | [optional] 
**members_url** | **str** |  | [optional] 
**parent** | [**TeamParent**](TeamParent.md) |  | [optional] 
**permission** | **str** | Permission that the team will have for its repositories | [optional] 
**privacy** | **str** |  | [optional] 
**repositories_url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_pull_request5_requested_reviewers_inner import WebhooksPullRequest5RequestedReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksPullRequest5RequestedReviewersInner from a JSON string
webhooks_pull_request5_requested_reviewers_inner_instance = WebhooksPullRequest5RequestedReviewersInner.from_json(json)
# print the JSON string representation of the object
print(WebhooksPullRequest5RequestedReviewersInner.to_json())

# convert the object into a dict
webhooks_pull_request5_requested_reviewers_inner_dict = webhooks_pull_request5_requested_reviewers_inner_instance.to_dict()
# create an instance of WebhooksPullRequest5RequestedReviewersInner from a dict
webhooks_pull_request5_requested_reviewers_inner_from_dict = WebhooksPullRequest5RequestedReviewersInner.from_dict(webhooks_pull_request5_requested_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


