# ConfigurationAuditLogTarget

The object of this event's action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID (user id, tailnet SID, or node id) of the target. | [optional] 
**name** | **str** | Name of the entity at time of the action. | [optional] 
**type** | **str** | The entity type of Target. | [optional] 
**is_ephemeral** | **bool** | Indicates whether the target is ephemeral. Its value should only be set if &#x60;type&#x60; is &#x60;NODE&#x60;&#x60;. | [optional] 
**var_property** | **str** | The property name on this target which was updated by the event. When empty, the event didn&#39;t update any fields on this target. | [optional] 

## Example

```python
from tailscale_openapi.models.configuration_audit_log_target import ConfigurationAuditLogTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationAuditLogTarget from a JSON string
configuration_audit_log_target_instance = ConfigurationAuditLogTarget.from_json(json)
# print the JSON string representation of the object
print(ConfigurationAuditLogTarget.to_json())

# convert the object into a dict
configuration_audit_log_target_dict = configuration_audit_log_target_instance.to_dict()
# create an instance of ConfigurationAuditLogTarget from a dict
configuration_audit_log_target_from_dict = ConfigurationAuditLogTarget.from_dict(configuration_audit_log_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


