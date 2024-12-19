# RepositoryInvitation

Repository invitations let you manage who you collaborate with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the repository invitation. | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 
**invitee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**inviter** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**permissions** | **str** | The permission associated with the invitation. | 
**created_at** | **datetime** |  | 
**expired** | **bool** | Whether or not the invitation has expired | [optional] 
**url** | **str** | URL for the repository invitation | 
**html_url** | **str** |  | 
**node_id** | **str** |  | 

## Example

```python
from github_openapi.models.repository_invitation import RepositoryInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryInvitation from a JSON string
repository_invitation_instance = RepositoryInvitation.from_json(json)
# print the JSON string representation of the object
print(RepositoryInvitation.to_json())

# convert the object into a dict
repository_invitation_dict = repository_invitation_instance.to_dict()
# create an instance of RepositoryInvitation from a dict
repository_invitation_from_dict = RepositoryInvitation.from_dict(repository_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


