# OrganizationDependabotSecret

Secrets for GitHub Dependabot for an organization.

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
from github_openapi.models.organization_dependabot_secret import OrganizationDependabotSecret

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDependabotSecret from a JSON string
organization_dependabot_secret_instance = OrganizationDependabotSecret.from_json(json)
# print the JSON string representation of the object
print(OrganizationDependabotSecret.to_json())

# convert the object into a dict
organization_dependabot_secret_dict = organization_dependabot_secret_instance.to_dict()
# create an instance of OrganizationDependabotSecret from a dict
organization_dependabot_secret_from_dict = OrganizationDependabotSecret.from_dict(organization_dependabot_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


