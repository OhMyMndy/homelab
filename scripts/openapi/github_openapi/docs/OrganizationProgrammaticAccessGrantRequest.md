# OrganizationProgrammaticAccessGrantRequest

Minimal representation of an organization programmatic access grant request for enumerations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the request for access via fine-grained personal access token. The &#x60;pat_request_id&#x60; used to review PAT requests. | 
**reason** | **str** | Reason for requesting access. | 
**owner** | [**SimpleUser**](SimpleUser.md) |  | 
**repository_selection** | **str** | Type of repository selection requested. | 
**repositories_url** | **str** | URL to the list of repositories requested to be accessed via fine-grained personal access token. Should only be followed when &#x60;repository_selection&#x60; is &#x60;subset&#x60;. | 
**permissions** | [**OrganizationProgrammaticAccessGrantRequestPermissions**](OrganizationProgrammaticAccessGrantRequestPermissions.md) |  | 
**created_at** | **str** | Date and time when the request for access was created. | 
**token_id** | **int** | Unique identifier of the user&#39;s token. This field can also be found in audit log events and the organization&#39;s settings for their PAT grants. | 
**token_name** | **str** | The name given to the user&#39;s token. This field can also be found in an organization&#39;s settings page for Active Tokens. | 
**token_expired** | **bool** | Whether the associated fine-grained personal access token has expired. | 
**token_expires_at** | **str** | Date and time when the associated fine-grained personal access token expires. | 
**token_last_used_at** | **str** | Date and time when the associated fine-grained personal access token was last used for authentication. | 

## Example

```python
from github_openapi.models.organization_programmatic_access_grant_request import OrganizationProgrammaticAccessGrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationProgrammaticAccessGrantRequest from a JSON string
organization_programmatic_access_grant_request_instance = OrganizationProgrammaticAccessGrantRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationProgrammaticAccessGrantRequest.to_json())

# convert the object into a dict
organization_programmatic_access_grant_request_dict = organization_programmatic_access_grant_request_instance.to_dict()
# create an instance of OrganizationProgrammaticAccessGrantRequest from a dict
organization_programmatic_access_grant_request_from_dict = OrganizationProgrammaticAccessGrantRequest.from_dict(organization_programmatic_access_grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


