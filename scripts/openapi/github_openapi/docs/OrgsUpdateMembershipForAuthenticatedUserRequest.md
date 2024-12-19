# OrgsUpdateMembershipForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state that the membership should be in. Only &#x60;\&quot;active\&quot;&#x60; will be accepted. | 

## Example

```python
from github_openapi.models.orgs_update_membership_for_authenticated_user_request import OrgsUpdateMembershipForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsUpdateMembershipForAuthenticatedUserRequest from a JSON string
orgs_update_membership_for_authenticated_user_request_instance = OrgsUpdateMembershipForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsUpdateMembershipForAuthenticatedUserRequest.to_json())

# convert the object into a dict
orgs_update_membership_for_authenticated_user_request_dict = orgs_update_membership_for_authenticated_user_request_instance.to_dict()
# create an instance of OrgsUpdateMembershipForAuthenticatedUserRequest from a dict
orgs_update_membership_for_authenticated_user_request_from_dict = OrgsUpdateMembershipForAuthenticatedUserRequest.from_dict(orgs_update_membership_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


