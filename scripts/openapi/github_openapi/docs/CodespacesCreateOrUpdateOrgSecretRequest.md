# CodespacesCreateOrUpdateOrgSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** | The value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an organization public key](https://docs.github.com/rest/codespaces/organization-secrets#get-an-organization-public-key) endpoint. | [optional] 
**key_id** | **str** | The ID of the key you used to encrypt the secret. | [optional] 
**visibility** | **str** | Which type of organization repositories have access to the organization secret. &#x60;selected&#x60; means only the repositories specified by &#x60;selected_repository_ids&#x60; can access the secret. | 
**selected_repository_ids** | **List[int]** | An array of repository IDs that can access the organization secret. You can only provide a list of repository IDs when the &#x60;visibility&#x60; is set to &#x60;selected&#x60;. You can manage the list of selected repositories using the [List selected repositories for an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#list-selected-repositories-for-an-organization-secret), [Set selected repositories for an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#set-selected-repositories-for-an-organization-secret), and [Remove selected repository from an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#remove-selected-repository-from-an-organization-secret) endpoints. | [optional] 

## Example

```python
from github_openapi.models.codespaces_create_or_update_org_secret_request import CodespacesCreateOrUpdateOrgSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesCreateOrUpdateOrgSecretRequest from a JSON string
codespaces_create_or_update_org_secret_request_instance = CodespacesCreateOrUpdateOrgSecretRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesCreateOrUpdateOrgSecretRequest.to_json())

# convert the object into a dict
codespaces_create_or_update_org_secret_request_dict = codespaces_create_or_update_org_secret_request_instance.to_dict()
# create an instance of CodespacesCreateOrUpdateOrgSecretRequest from a dict
codespaces_create_or_update_org_secret_request_from_dict = CodespacesCreateOrUpdateOrgSecretRequest.from_dict(codespaces_create_or_update_org_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


