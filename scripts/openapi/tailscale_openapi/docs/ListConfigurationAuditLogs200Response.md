# ListConfigurationAuditLogs200Response

A structured response for all of a Tailnet's audit logs over a period of time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version of audit logs response. | [optional] 
**tailnet** | **str** | The tailnet on which the logged configuration changes were made. | [optional] 
**logs** | [**List[ConfigurationAuditLog]**](ConfigurationAuditLog.md) | Matching log entries, ordered chronologically. | [optional] 

## Example

```python
from tailscale_openapi.models.list_configuration_audit_logs200_response import ListConfigurationAuditLogs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfigurationAuditLogs200Response from a JSON string
list_configuration_audit_logs200_response_instance = ListConfigurationAuditLogs200Response.from_json(json)
# print the JSON string representation of the object
print(ListConfigurationAuditLogs200Response.to_json())

# convert the object into a dict
list_configuration_audit_logs200_response_dict = list_configuration_audit_logs200_response_instance.to_dict()
# create an instance of ListConfigurationAuditLogs200Response from a dict
list_configuration_audit_logs200_response_from_dict = ListConfigurationAuditLogs200Response.from_dict(list_configuration_audit_logs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


