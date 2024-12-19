# WebhooksApprover


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
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_approver import WebhooksApprover

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksApprover from a JSON string
webhooks_approver_instance = WebhooksApprover.from_json(json)
# print the JSON string representation of the object
print(WebhooksApprover.to_json())

# convert the object into a dict
webhooks_approver_dict = webhooks_approver_instance.to_dict()
# create an instance of WebhooksApprover from a dict
webhooks_approver_from_dict = WebhooksApprover.from_dict(webhooks_approver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


