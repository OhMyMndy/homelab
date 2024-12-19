# PullRequestRequestedReviewersInner


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
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the team | 
**login** | **str** |  | 
**name** | **str** | Name of the team | 
**node_id** | **str** |  | 
**organizations_url** | **str** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** | URL for the team | 
**user_view_type** | **str** |  | [optional] 
**description** | **str** | Description of the team | 
**members_url** | **str** |  | 
**parent** | [**TeamParent**](TeamParent.md) |  | [optional] 
**permission** | **str** | Permission that the team will have for its repositories | 
**privacy** | **str** |  | 
**repositories_url** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from github_openapi.models.pull_request_requested_reviewers_inner import PullRequestRequestedReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestRequestedReviewersInner from a JSON string
pull_request_requested_reviewers_inner_instance = PullRequestRequestedReviewersInner.from_json(json)
# print the JSON string representation of the object
print(PullRequestRequestedReviewersInner.to_json())

# convert the object into a dict
pull_request_requested_reviewers_inner_dict = pull_request_requested_reviewers_inner_instance.to_dict()
# create an instance of PullRequestRequestedReviewersInner from a dict
pull_request_requested_reviewers_inner_from_dict = PullRequestRequestedReviewersInner.from_dict(pull_request_requested_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


