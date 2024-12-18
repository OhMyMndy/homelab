# Device

A Tailscale device (sometimes referred to as *node* or *machine*), is any computer or mobile device that joins a tailnet.  Each device has a unique ID (`nodeId` in the schema below) that is used to identify the device in API calls. This ID can be found by going to the [Machines](https://login.tailscale.com/admin/machines) page in the admin console, selecting the relevant device, then finding the ID in the Machine Details section. You can also [list all devices](#tag/devices/get/tailnet/{tailnet}/devices) in the tailnet to get their `nodeId` values. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | A list of Tailscale IP addresses for the device, including both IPv4 (formatted as 100.x.y.z) and IPv6 (formatted as fd7a:115c:a1e0:a:b:c:d:e) addresses.  | [optional] 
**id** | **str** | The legacy identifier for a device; you can supply this value wherever {deviceId} is indicated in the endpoint. Note that although \&quot;id\&quot; is still accepted, \&quot;nodeId\&quot; is preferred.  | [optional] 
**node_id** | **str** | The preferred identifier for a device; supply this value wherever {deviceId} is indicated in the endpoint.  | [optional] 
**user** | **str** | The user who registered the node. For untagged nodes,  this user is the device owner.  | [optional] 
**name** | **str** | The MagicDNS name of the device. Learn more about MagicDNS at https://tailscale.com/kb/1081/.  | [optional] 
**hostname** | **str** | The machine name in the admin console. Learn more about machine names at https://tailscale.com/kb/1098/.  | [optional] 
**client_version** | **str** | The version of the Tailscale client software; this is empty for external devices.  | [optional] 
**update_available** | **bool** | &#39;true&#39; if a Tailscale client version upgrade is available. This value is empty for external devices.  | [optional] 
**os** | **str** | The operating system that the device is running.  | [optional] 
**created** | **datetime** | The date on which the device was added to the tailnet; this is empty for external devices.  | [optional] 
**last_seen** | **datetime** | When device was last active on the tailnet.  | [optional] 
**key_expiry_disabled** | **bool** | &#39;true&#39; if the keys for the device will not expire. Learn more at https://tailscale.com/kb/1028/.  | [optional] 
**expires** | **datetime** | The expiration date of the device&#39;s auth key. Learn more about key expiry at https://tailscale.com/kb/1028/.  | [optional] 
**authorized** | **bool** | &#39;true&#39; if the device has been authorized to join the tailnet; otherwise, &#39;false&#39;. Learn more about device authorization at https://tailscale.com/kb/1099/.  | [optional] 
**is_external** | **bool** | &#39;true&#39;, indicates that a device is not a member of the tailnet, but is shared in to the tailnet; if &#39;false&#39;, the device is a member of the tailnet. Learn more about node sharing at https://tailscale.com/kb/1084/.  | [optional] 
**machine_key** | **str** | For internal use and is not required for any API operations. This value is empty for external devices.  | [optional] 
**node_key** | **str** | Mostly for internal use, required for select operations, such as adding a node to a locked tailnet. Learn about tailnet locks at https://tailscale.com/kb/1226/.  | [optional] 
**blocks_incoming_connections** | **bool** | &#39;true&#39; if the device is not allowed to accept any connections over Tailscale, including pings. Learn more in the \&quot;Allow incoming connections\&quot; section of https://tailscale.com/kb/1072/.  | [optional] 
**enabled_routes** | **List[str]** | The subnet routes for this device that have been approved by a tailnet admin. Learn more about subnet routes at https://tailscale.com/kb/1019/.  | [optional] 
**advertised_routes** | **List[str]** | The subnets this device requests to expose. Learn more about subnet routes at https://tailscale.com/kb/1019/.  | [optional] 
**client_connectivity** | [**DeviceClientConnectivity**](DeviceClientConnectivity.md) |  | [optional] 
**tags** | **List[str]** | Lets you assign an identity to a device that is separate from human users, and use it as part of an ACL to restrict access. Once a device is tagged, the tag is the owner of that device. A single node can have multiple tags assigned. This value is empty for external devices. Learn more about tags at https://tailscale.com/kb/1068/.  | [optional] 
**tailnet_lock_error** | **str** | Indicates an issue with the tailnet lock node-key signature on this device. This field is only populated when tailnet lock is enabled.  | [optional] 
**tailnet_lock_key** | **str** | The node&#39;s tailnet lock key. Every node generates a tailnet lock key (so the value will be present) even if tailnet lock is not enabled. Learn more about tailnet lock at https://tailscale.com/kb/1226/.  | [optional] 
**posture_identity** | [**DevicePostureIdentity**](DevicePostureIdentity.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


