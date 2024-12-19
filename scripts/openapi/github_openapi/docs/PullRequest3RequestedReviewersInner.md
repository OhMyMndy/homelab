# PullRequest3RequestedReviewersInner


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
**user_view_type** | **str** |  | [optional] 
**description** | **str** | Description of the team | [optional] 
**members_url** | **str** |  | [optional] 
**parent** | [**TeamParent**](TeamParent.md) |  | [optional] 
**permission** | **str** | Permission that the team will have for its repositories | [optional] 
**privacy** | **str** |  | [optional] 
**repositories_url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.pull_request3_requested_reviewers_inner import PullRequest3RequestedReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest3RequestedReviewersInner from a JSON string
pull_request3_requested_reviewers_inner_instance = PullRequest3RequestedReviewersInner.from_json(json)
# print the JSON string representation of the object
print(PullRequest3RequestedReviewersInner.to_json())

# convert the object into a dict
pull_request3_requested_reviewers_inner_dict = pull_request3_requested_reviewers_inner_instance.to_dict()
# create an instance of PullRequest3RequestedReviewersInner from a dict
pull_request3_requested_reviewers_inner_from_dict = PullRequest3RequestedReviewersInner.from_dict(pull_request3_requested_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


