# CodespacesOrgSecret

Secrets for a GitHub Codespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret | 
**created_at** | **datetime** | The date and time at which the secret was created, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 
**updated_at** | **datetime** | The date and time at which the secret was created, in ISO 8601 format&#39;:&#39; YYYY-MM-DDTHH:MM:SSZ. | 
**visibility** | **str** | The type of repositories in the organization that the secret is visible to | 
**selected_repositories_url** | **str** | The API URL at which the list of repositories this secret is visible to can be retrieved | [optional] 

## Example

```python
from github_openapi.models.codespaces_org_secret import CodespacesOrgSecret

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesOrgSecret from a JSON string
codespaces_org_secret_instance = CodespacesOrgSecret.from_json(json)
# print the JSON string representation of the object
print(CodespacesOrgSecret.to_json())

# convert the object into a dict
codespaces_org_secret_dict = codespaces_org_secret_instance.to_dict()
# create an instance of CodespacesOrgSecret from a dict
codespaces_org_secret_from_dict = CodespacesOrgSecret.from_dict(codespaces_org_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


