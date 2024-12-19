# Installation

Installation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the installation. | 
**account** | [**InstallationAccount**](InstallationAccount.md) |  | 
**repository_selection** | **str** | Describe whether all repositories have been selected or there&#39;s a selection involved | 
**access_tokens_url** | **str** |  | 
**repositories_url** | **str** |  | 
**html_url** | **str** |  | 
**app_id** | **int** |  | 
**target_id** | **int** | The ID of the user or organization this token is being scoped to. | 
**target_type** | **str** |  | 
**permissions** | [**AppPermissions**](AppPermissions.md) |  | 
**events** | **List[str]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**single_file_name** | **str** |  | 
**has_multiple_single_files** | **bool** |  | [optional] 
**single_file_paths** | **List[str]** |  | [optional] 
**app_slug** | **str** |  | 
**suspended_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**suspended_at** | **datetime** |  | 
**contact_email** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.installation import Installation

# TODO update the JSON string below
json = "{}"
# create an instance of Installation from a JSON string
installation_instance = Installation.from_json(json)
# print the JSON string representation of the object
print(Installation.to_json())

# convert the object into a dict
installation_dict = installation_instance.to_dict()
# create an instance of Installation from a dict
installation_from_dict = Installation.from_dict(installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


