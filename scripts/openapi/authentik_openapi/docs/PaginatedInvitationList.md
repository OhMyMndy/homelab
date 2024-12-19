# PaginatedInvitationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Invitation]**](Invitation.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_invitation_list import PaginatedInvitationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInvitationList from a JSON string
paginated_invitation_list_instance = PaginatedInvitationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedInvitationList.to_json())

# convert the object into a dict
paginated_invitation_list_dict = paginated_invitation_list_instance.to_dict()
# create an instance of PaginatedInvitationList from a dict
paginated_invitation_list_from_dict = PaginatedInvitationList.from_dict(paginated_invitation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


