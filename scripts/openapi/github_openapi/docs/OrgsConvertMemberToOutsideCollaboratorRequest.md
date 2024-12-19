# OrgsConvertMemberToOutsideCollaboratorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** | When set to &#x60;true&#x60;, the request will be performed asynchronously. Returns a 202 status code when the job is successfully queued. | [optional] [default to False]

## Example

```python
from github_openapi.models.orgs_convert_member_to_outside_collaborator_request import OrgsConvertMemberToOutsideCollaboratorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsConvertMemberToOutsideCollaboratorRequest from a JSON string
orgs_convert_member_to_outside_collaborator_request_instance = OrgsConvertMemberToOutsideCollaboratorRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsConvertMemberToOutsideCollaboratorRequest.to_json())

# convert the object into a dict
orgs_convert_member_to_outside_collaborator_request_dict = orgs_convert_member_to_outside_collaborator_request_instance.to_dict()
# create an instance of OrgsConvertMemberToOutsideCollaboratorRequest from a dict
orgs_convert_member_to_outside_collaborator_request_from_dict = OrgsConvertMemberToOutsideCollaboratorRequest.from_dict(orgs_convert_member_to_outside_collaborator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


