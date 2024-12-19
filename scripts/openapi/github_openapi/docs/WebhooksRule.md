# WebhooksRule

The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_enforced** | **bool** |  | 
**allow_deletions_enforcement_level** | **str** |  | 
**allow_force_pushes_enforcement_level** | **str** |  | 
**authorized_actor_names** | **List[str]** |  | 
**authorized_actors_only** | **bool** |  | 
**authorized_dismissal_actors_only** | **bool** |  | 
**create_protected** | **bool** |  | [optional] 
**created_at** | **datetime** |  | 
**dismiss_stale_reviews_on_push** | **bool** |  | 
**id** | **int** |  | 
**ignore_approvals_from_contributors** | **bool** |  | 
**linear_history_requirement_enforcement_level** | **str** |  | 
**lock_branch_enforcement_level** | **str** | The enforcement level of the branch lock setting. &#x60;off&#x60; means the branch is not locked, &#x60;non_admins&#x60; means the branch is read-only for non_admins, and &#x60;everyone&#x60; means the branch is read-only for everyone. | 
**lock_allows_fork_sync** | **bool** | Whether users can pull changes from upstream when the branch is locked. Set to &#x60;true&#x60; to allow users to pull changes from upstream when the branch is locked. This setting is only applicable for forks. | [optional] 
**merge_queue_enforcement_level** | **str** |  | 
**name** | **str** |  | 
**pull_request_reviews_enforcement_level** | **str** |  | 
**repository_id** | **int** |  | 
**require_code_owner_review** | **bool** |  | 
**require_last_push_approval** | **bool** | Whether the most recent push must be approved by someone other than the person who pushed it | [optional] 
**required_approving_review_count** | **int** |  | 
**required_conversation_resolution_level** | **str** |  | 
**required_deployments_enforcement_level** | **str** |  | 
**required_status_checks** | **List[str]** |  | 
**required_status_checks_enforcement_level** | **str** |  | 
**signature_requirement_enforcement_level** | **str** |  | 
**strict_required_status_checks_policy** | **bool** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.webhooks_rule import WebhooksRule

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksRule from a JSON string
webhooks_rule_instance = WebhooksRule.from_json(json)
# print the JSON string representation of the object
print(WebhooksRule.to_json())

# convert the object into a dict
webhooks_rule_dict = webhooks_rule_instance.to_dict()
# create an instance of WebhooksRule from a dict
webhooks_rule_from_dict = WebhooksRule.from_dict(webhooks_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


