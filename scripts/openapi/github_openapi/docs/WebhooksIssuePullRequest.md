# WebhooksIssuePullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff_url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**merged_at** | **datetime** |  | [optional] 
**patch_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhooks_issue_pull_request import WebhooksIssuePullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksIssuePullRequest from a JSON string
webhooks_issue_pull_request_instance = WebhooksIssuePullRequest.from_json(json)
# print the JSON string representation of the object
print(WebhooksIssuePullRequest.to_json())

# convert the object into a dict
webhooks_issue_pull_request_dict = webhooks_issue_pull_request_instance.to_dict()
# create an instance of WebhooksIssuePullRequest from a dict
webhooks_issue_pull_request_from_dict = WebhooksIssuePullRequest.from_dict(webhooks_issue_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


