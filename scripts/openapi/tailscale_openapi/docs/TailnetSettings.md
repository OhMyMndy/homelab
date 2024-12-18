# TailnetSettings

Settings for a tailnet. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices_approval_on** | **bool** | Whether [device approval](/kb/1099/device-approval) is enabled for the tailnet.  | [optional] 
**devices_auto_updates_on** | **bool** | Whether [auto updates](/kb/1067/update#auto-updates) are enabled for devices that belong to this tailnet.  | [optional] 
**devices_key_duration_days** | **int** | The [key expiry](/kb/1028/key-expiry) duration for devices on this tailnet.  | [optional] 
**users_approval_on** | **bool** | Whether [user approval](/kb/1239/user-approval) is enabled for this tailnet.  | [optional] 
**users_role_allowed_to_join_external_tailnets** | **str** | Which user roles are allowed to [join external tailnets](/kb/1271/invite-any-user).  | [optional] 
**network_flow_logging_on** | **bool** | Whether [network flog logs](/kb/1219/network-flow-logs) are enabled for the tailnet.  | [optional] 
**regional_routing_on** | **bool** | Whether [regional routing](/kb/1115/high-availability#regional-routing) is enabled for the tailnet.  | [optional] 
**posture_identity_collection_on** | **bool** | Whether [identity collection](/kb/1326/device-identity) is enabled for [device posture](/kb/1288/device-posture) integrations for the tailnet.  | [optional] 

## Example

```python
from tailscale_openapi.models.tailnet_settings import TailnetSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TailnetSettings from a JSON string
tailnet_settings_instance = TailnetSettings.from_json(json)
# print the JSON string representation of the object
print(TailnetSettings.to_json())

# convert the object into a dict
tailnet_settings_dict = tailnet_settings_instance.to_dict()
# create an instance of TailnetSettings from a dict
tailnet_settings_from_dict = TailnetSettings.from_dict(tailnet_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


