# WebhooksSecurityAdvisoryIdentifiersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_security_advisory_identifiers_inner import WebhooksSecurityAdvisoryIdentifiersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSecurityAdvisoryIdentifiersInner from a JSON string
webhooks_security_advisory_identifiers_inner_instance = WebhooksSecurityAdvisoryIdentifiersInner.from_json(json)
# print the JSON string representation of the object
print(WebhooksSecurityAdvisoryIdentifiersInner.to_json())

# convert the object into a dict
webhooks_security_advisory_identifiers_inner_dict = webhooks_security_advisory_identifiers_inner_instance.to_dict()
# create an instance of WebhooksSecurityAdvisoryIdentifiersInner from a dict
webhooks_security_advisory_identifiers_inner_from_dict = WebhooksSecurityAdvisoryIdentifiersInner.from_dict(webhooks_security_advisory_identifiers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


