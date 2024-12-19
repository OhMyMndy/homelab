# PaginatedInvitationStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[InvitationStage]**](InvitationStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_invitation_stage_list import PaginatedInvitationStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInvitationStageList from a JSON string
paginated_invitation_stage_list_instance = PaginatedInvitationStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedInvitationStageList.to_json())

# convert the object into a dict
paginated_invitation_stage_list_dict = paginated_invitation_stage_list_instance.to_dict()
# create an instance of PaginatedInvitationStageList from a dict
paginated_invitation_stage_list_from_dict = PaginatedInvitationStageList.from_dict(paginated_invitation_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


