# ConfigurationAuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_time** | **str** | Timestamp of the audit log event, in RFC 3339 format. | 
**type** | **str** | The type of log (always \&quot;CONFIG\&quot;). | 
**deferred_at** | **str** | Timestamp recording the time that the audit log rate limiter enqueued the record to be logged at a future time, in RFC 3339 format. | [optional] 
**event_group_id** | **str** | Identifier assigned to one or more audit log events, all of which are the result of a single operation. | 
**origin** | **str** | The initiator of the action that generated the event, typically an API or user interface, like the Tailscale admin panel. | 
**actor** | [**ConfigurationAuditLogActor**](ConfigurationAuditLogActor.md) |  | 
**target** | [**ConfigurationAuditLogTarget**](ConfigurationAuditLogTarget.md) |  | 
**action** | **str** | The type of change attempted against the &#x60;target&#x60;. | 
**old** | **object** | The value of &#x60;target.property&#x60;&#x60; prior to the event. | [optional] 
**new** | **object** | The value of &#x60;target.property&#x60; after the event. | [optional] 
**action_details** | **str** | Additional information about the event, such as a client-provided reason, if it exists. | [optional] 
**error** | **str** | Provided when the configuration change failed to be completed. It is a user-presentable reason for the failure. | [optional] 

## Example

```python
from tailscale_openapi.models.configuration_audit_log import ConfigurationAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationAuditLog from a JSON string
configuration_audit_log_instance = ConfigurationAuditLog.from_json(json)
# print the JSON string representation of the object
print(ConfigurationAuditLog.to_json())

# convert the object into a dict
configuration_audit_log_dict = configuration_audit_log_instance.to_dict()
# create an instance of ConfigurationAuditLog from a dict
configuration_audit_log_from_dict = ConfigurationAuditLog.from_dict(configuration_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


