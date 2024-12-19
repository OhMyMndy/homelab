# OrgsSetMembershipForUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role to give the user in the organization. Can be one of:    * &#x60;admin&#x60; - The user will become an owner of the organization.    * &#x60;member&#x60; - The user will become a non-owner member of the organization. | [optional] [default to 'member']

## Example

```python
from github_openapi.models.orgs_set_membership_for_user_request import OrgsSetMembershipForUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsSetMembershipForUserRequest from a JSON string
orgs_set_membership_for_user_request_instance = OrgsSetMembershipForUserRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsSetMembershipForUserRequest.to_json())

# convert the object into a dict
orgs_set_membership_for_user_request_dict = orgs_set_membership_for_user_request_instance.to_dict()
# create an instance of OrgsSetMembershipForUserRequest from a dict
orgs_set_membership_for_user_request_from_dict = OrgsSetMembershipForUserRequest.from_dict(orgs_set_membership_for_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


