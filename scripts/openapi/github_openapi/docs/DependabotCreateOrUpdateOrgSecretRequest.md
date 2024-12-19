# DependabotCreateOrUpdateOrgSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an organization public key](https://docs.github.com/rest/dependabot/secrets#get-an-organization-public-key) endpoint. | [optional] 
**key_id** | **str** | ID of the key you used to encrypt the secret. | [optional] 
**visibility** | **str** | Which type of organization repositories have access to the organization secret. &#x60;selected&#x60; means only the repositories specified by &#x60;selected_repository_ids&#x60; can access the secret. | 
**selected_repository_ids** | **List[str]** | An array of repository ids that can access the organization secret. You can only provide a list of repository ids when the &#x60;visibility&#x60; is set to &#x60;selected&#x60;. You can manage the list of selected repositories using the [List selected repositories for an organization secret](https://docs.github.com/rest/dependabot/secrets#list-selected-repositories-for-an-organization-secret), [Set selected repositories for an organization secret](https://docs.github.com/rest/dependabot/secrets#set-selected-repositories-for-an-organization-secret), and [Remove selected repository from an organization secret](https://docs.github.com/rest/dependabot/secrets#remove-selected-repository-from-an-organization-secret) endpoints. | [optional] 

## Example

```python
from github_openapi.models.dependabot_create_or_update_org_secret_request import DependabotCreateOrUpdateOrgSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotCreateOrUpdateOrgSecretRequest from a JSON string
dependabot_create_or_update_org_secret_request_instance = DependabotCreateOrUpdateOrgSecretRequest.from_json(json)
# print the JSON string representation of the object
print(DependabotCreateOrUpdateOrgSecretRequest.to_json())

# convert the object into a dict
dependabot_create_or_update_org_secret_request_dict = dependabot_create_or_update_org_secret_request_instance.to_dict()
# create an instance of DependabotCreateOrUpdateOrgSecretRequest from a dict
dependabot_create_or_update_org_secret_request_from_dict = DependabotCreateOrUpdateOrgSecretRequest.from_dict(dependabot_create_or_update_org_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


