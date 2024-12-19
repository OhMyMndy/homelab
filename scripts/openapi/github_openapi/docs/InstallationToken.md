# InstallationToken

Authentication token for a GitHub App installed on a user or org.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**expires_at** | **str** |  | 
**permissions** | [**AppPermissions**](AppPermissions.md) |  | [optional] 
**repository_selection** | **str** |  | [optional] 
**repositories** | [**List[Repository]**](Repository.md) |  | [optional] 
**single_file** | **str** |  | [optional] 
**has_multiple_single_files** | **bool** |  | [optional] 
**single_file_paths** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.installation_token import InstallationToken

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationToken from a JSON string
installation_token_instance = InstallationToken.from_json(json)
# print the JSON string representation of the object
print(InstallationToken.to_json())

# convert the object into a dict
installation_token_dict = installation_token_instance.to_dict()
# create an instance of InstallationToken from a dict
installation_token_from_dict = InstallationToken.from_dict(installation_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


