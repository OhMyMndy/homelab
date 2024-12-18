# ConfigurationAuditLogActor

The person who caused the action related to this event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID (user ID or node ID) of the actor. | [optional] 
**type** | **str** | The entity type of the actor. | [optional] 
**login_name** | **str** | The login name of the actor at time of the action. | [optional] 
**display_name** | **str** | The display name of the actor at time of the action. | [optional] 
**tags** | **List[str]** | Indicates the tags owning a node. Its value is only set if &#x60;type&#x60; is &#x60;NODE&#x60;. | [optional] 

## Example

```python
from tailscale_openapi.models.configuration_audit_log_actor import ConfigurationAuditLogActor

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationAuditLogActor from a JSON string
configuration_audit_log_actor_instance = ConfigurationAuditLogActor.from_json(json)
# print the JSON string representation of the object
print(ConfigurationAuditLogActor.to_json())

# convert the object into a dict
configuration_audit_log_actor_dict = configuration_audit_log_actor_instance.to_dict()
# create an instance of ConfigurationAuditLogActor from a dict
configuration_audit_log_actor_from_dict = ConfigurationAuditLogActor.from_dict(configuration_audit_log_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


