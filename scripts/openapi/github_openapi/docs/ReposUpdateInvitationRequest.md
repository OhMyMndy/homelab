# ReposUpdateInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **str** | The permissions that the associated user will have on the repository. Valid values are &#x60;read&#x60;, &#x60;write&#x60;, &#x60;maintain&#x60;, &#x60;triage&#x60;, and &#x60;admin&#x60;. | [optional] 

## Example

```python
from github_openapi.models.repos_update_invitation_request import ReposUpdateInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateInvitationRequest from a JSON string
repos_update_invitation_request_instance = ReposUpdateInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateInvitationRequest.to_json())

# convert the object into a dict
repos_update_invitation_request_dict = repos_update_invitation_request_instance.to_dict()
# create an instance of ReposUpdateInvitationRequest from a dict
repos_update_invitation_request_from_dict = ReposUpdateInvitationRequest.from_dict(repos_update_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


