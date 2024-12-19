# OrganizationActionsSecret

Secrets for GitHub Actions for an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**visibility** | **str** | Visibility of a secret | 
**selected_repositories_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.organization_actions_secret import OrganizationActionsSecret

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationActionsSecret from a JSON string
organization_actions_secret_instance = OrganizationActionsSecret.from_json(json)
# print the JSON string representation of the object
print(OrganizationActionsSecret.to_json())

# convert the object into a dict
organization_actions_secret_dict = organization_actions_secret_instance.to_dict()
# create an instance of OrganizationActionsSecret from a dict
organization_actions_secret_from_dict = OrganizationActionsSecret.from_dict(organization_actions_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


