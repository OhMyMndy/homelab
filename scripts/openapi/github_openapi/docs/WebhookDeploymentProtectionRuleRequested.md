# WebhookDeploymentProtectionRuleRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**environment** | **str** | The name of the environment that has the deployment protection rule. | [optional] 
**event** | **str** | The event that triggered the deployment protection rule. | [optional] 
**deployment_callback_url** | **str** | The URL to review the deployment protection rule. | [optional] 
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 
**pull_requests** | [**List[PullRequest]**](PullRequest.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_deployment_protection_rule_requested import WebhookDeploymentProtectionRuleRequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentProtectionRuleRequested from a JSON string
webhook_deployment_protection_rule_requested_instance = WebhookDeploymentProtectionRuleRequested.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentProtectionRuleRequested.to_json())

# convert the object into a dict
webhook_deployment_protection_rule_requested_dict = webhook_deployment_protection_rule_requested_instance.to_dict()
# create an instance of WebhookDeploymentProtectionRuleRequested from a dict
webhook_deployment_protection_rule_requested_from_dict = WebhookDeploymentProtectionRuleRequested.from_dict(webhook_deployment_protection_rule_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


