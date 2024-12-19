# GroupMemberRequest

Stripped down user serializer to show relevant users for groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**name** | **str** | User&#39;s display name. | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_openapi.models.group_member_request import GroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberRequest from a JSON string
group_member_request_instance = GroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print(GroupMemberRequest.to_json())

# convert the object into a dict
group_member_request_dict = group_member_request_instance.to_dict()
# create an instance of GroupMemberRequest from a dict
group_member_request_from_dict = GroupMemberRequest.from_dict(group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


