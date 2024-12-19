# CodespacesSetSelectedReposForOrgSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_repository_ids** | **List[int]** | An array of repository ids that can access the organization secret. You can only provide a list of repository ids when the &#x60;visibility&#x60; is set to &#x60;selected&#x60;. You can add and remove individual repositories using the [Set selected repositories for an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#set-selected-repositories-for-an-organization-secret) and [Remove selected repository from an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#remove-selected-repository-from-an-organization-secret) endpoints. | 

## Example

```python
from github_openapi.models.codespaces_set_selected_repos_for_org_secret_request import CodespacesSetSelectedReposForOrgSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesSetSelectedReposForOrgSecretRequest from a JSON string
codespaces_set_selected_repos_for_org_secret_request_instance = CodespacesSetSelectedReposForOrgSecretRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesSetSelectedReposForOrgSecretRequest.to_json())

# convert the object into a dict
codespaces_set_selected_repos_for_org_secret_request_dict = codespaces_set_selected_repos_for_org_secret_request_instance.to_dict()
# create an instance of CodespacesSetSelectedReposForOrgSecretRequest from a dict
codespaces_set_selected_repos_for_org_secret_request_from_dict = CodespacesSetSelectedReposForOrgSecretRequest.from_dict(codespaces_set_selected_repos_for_org_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


