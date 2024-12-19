# OrganizationSimpleWebhooks

A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an organization, or when the event occurs from activity in a repository owned by an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**repos_url** | **str** |  | 
**events_url** | **str** |  | 
**hooks_url** | **str** |  | 
**issues_url** | **str** |  | 
**members_url** | **str** |  | 
**public_members_url** | **str** |  | 
**avatar_url** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from github_openapi.models.organization_simple_webhooks import OrganizationSimpleWebhooks

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSimpleWebhooks from a JSON string
organization_simple_webhooks_instance = OrganizationSimpleWebhooks.from_json(json)
# print the JSON string representation of the object
print(OrganizationSimpleWebhooks.to_json())

# convert the object into a dict
organization_simple_webhooks_dict = organization_simple_webhooks_instance.to_dict()
# create an instance of OrganizationSimpleWebhooks from a dict
organization_simple_webhooks_from_dict = OrganizationSimpleWebhooks.from_dict(organization_simple_webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


