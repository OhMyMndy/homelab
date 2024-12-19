# PullRequestSimple

Pull Request Simple

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**html_url** | **str** |  | 
**diff_url** | **str** |  | 
**patch_url** | **str** |  | 
**issue_url** | **str** |  | 
**commits_url** | **str** |  | 
**review_comments_url** | **str** |  | 
**review_comment_url** | **str** |  | 
**comments_url** | **str** |  | 
**statuses_url** | **str** |  | 
**number** | **int** |  | 
**state** | **str** |  | 
**locked** | **bool** |  | 
**title** | **str** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**body** | **str** |  | 
**labels** | [**List[PullRequestSimpleLabelsInner]**](PullRequestSimpleLabelsInner.md) |  | 
**milestone** | [**NullableMilestone**](NullableMilestone.md) |  | 
**active_lock_reason** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**closed_at** | **datetime** |  | 
**merged_at** | **datetime** |  | 
**merge_commit_sha** | **str** |  | 
**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**assignees** | [**List[SimpleUser]**](SimpleUser.md) |  | [optional] 
**requested_reviewers** | [**List[SimpleUser]**](SimpleUser.md) |  | [optional] 
**requested_teams** | [**List[Team]**](Team.md) |  | [optional] 
**head** | [**PullRequestSimpleHead**](PullRequestSimpleHead.md) |  | 
**base** | [**PullRequestSimpleHead**](PullRequestSimpleHead.md) |  | 
**links** | [**PullRequestSimpleLinks**](PullRequestSimpleLinks.md) |  | 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**auto_merge** | [**AutoMerge**](AutoMerge.md) |  | 
**draft** | **bool** | Indicates whether or not the pull request is a draft. | [optional] 

## Example

```python
from github_openapi.models.pull_request_simple import PullRequestSimple

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestSimple from a JSON string
pull_request_simple_instance = PullRequestSimple.from_json(json)
# print the JSON string representation of the object
print(PullRequestSimple.to_json())

# convert the object into a dict
pull_request_simple_dict = pull_request_simple_instance.to_dict()
# create an instance of PullRequestSimple from a dict
pull_request_simple_from_dict = PullRequestSimple.from_dict(pull_request_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


