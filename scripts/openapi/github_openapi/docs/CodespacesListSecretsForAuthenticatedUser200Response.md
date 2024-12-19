# CodespacesListSecretsForAuthenticatedUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**secrets** | [**List[CodespacesSecret]**](CodespacesSecret.md) |  | 

## Example

```python
from github_openapi.models.codespaces_list_secrets_for_authenticated_user200_response import CodespacesListSecretsForAuthenticatedUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesListSecretsForAuthenticatedUser200Response from a JSON string
codespaces_list_secrets_for_authenticated_user200_response_instance = CodespacesListSecretsForAuthenticatedUser200Response.from_json(json)
# print the JSON string representation of the object
print(CodespacesListSecretsForAuthenticatedUser200Response.to_json())

# convert the object into a dict
codespaces_list_secrets_for_authenticated_user200_response_dict = codespaces_list_secrets_for_authenticated_user200_response_instance.to_dict()
# create an instance of CodespacesListSecretsForAuthenticatedUser200Response from a dict
codespaces_list_secrets_for_authenticated_user200_response_from_dict = CodespacesListSecretsForAuthenticatedUser200Response.from_dict(codespaces_list_secrets_for_authenticated_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


