# WebhookPush


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** | The SHA of the most recent commit on &#x60;ref&#x60; after the push. | 
**base_ref** | **str** |  | 
**before** | **str** | The SHA of the most recent commit on &#x60;ref&#x60; before the push. | 
**commits** | [**List[Commit]**](Commit.md) | An array of commit objects describing the pushed commits. (Pushed commits are all commits that are included in the &#x60;compare&#x60; between the &#x60;before&#x60; commit and the &#x60;after&#x60; commit.) The array includes a maximum of 2048 commits. If necessary, you can use the [Commits API](https://docs.github.com/rest/commits) to fetch additional commits. | 
**compare** | **str** | URL that shows the changes in this &#x60;ref&#x60; update, from the &#x60;before&#x60; commit to the &#x60;after&#x60; commit. For a newly created &#x60;ref&#x60; that is directly based on the default branch, this is the comparison between the head of the default branch and the &#x60;after&#x60; commit. Otherwise, this shows all commits until the &#x60;after&#x60; commit. | 
**created** | **bool** | Whether this push created the &#x60;ref&#x60;. | 
**deleted** | **bool** | Whether this push deleted the &#x60;ref&#x60;. | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**forced** | **bool** | Whether this push was a force push of the &#x60;ref&#x60;. | 
**head_commit** | [**Commit1**](Commit1.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pusher** | [**Committer1**](Committer1.md) |  | 
**ref** | **str** | The full git ref that was pushed. Example: &#x60;refs/heads/main&#x60; or &#x60;refs/tags/v3.14.1&#x60;. | 
**repository** | [**Repository2**](Repository2.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_push import WebhookPush

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPush from a JSON string
webhook_push_instance = WebhookPush.from_json(json)
# print the JSON string representation of the object
print(WebhookPush.to_json())

# convert the object into a dict
webhook_push_dict = webhook_push_instance.to_dict()
# create an instance of WebhookPush from a dict
webhook_push_from_dict = WebhookPush.from_dict(webhook_push_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


