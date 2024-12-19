# WebhooksSecurityAdvisoryCvss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** |  | 
**vector_string** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_security_advisory_cvss import WebhooksSecurityAdvisoryCvss

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSecurityAdvisoryCvss from a JSON string
webhooks_security_advisory_cvss_instance = WebhooksSecurityAdvisoryCvss.from_json(json)
# print the JSON string representation of the object
print(WebhooksSecurityAdvisoryCvss.to_json())

# convert the object into a dict
webhooks_security_advisory_cvss_dict = webhooks_security_advisory_cvss_instance.to_dict()
# create an instance of WebhooksSecurityAdvisoryCvss from a dict
webhooks_security_advisory_cvss_from_dict = WebhooksSecurityAdvisoryCvss.from_dict(webhooks_security_advisory_cvss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


