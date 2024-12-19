# CodespacesListInOrganization200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**codespaces** | [**List[Codespace]**](Codespace.md) |  | 

## Example

```python
from github_openapi.models.codespaces_list_in_organization200_response import CodespacesListInOrganization200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesListInOrganization200Response from a JSON string
codespaces_list_in_organization200_response_instance = CodespacesListInOrganization200Response.from_json(json)
# print the JSON string representation of the object
print(CodespacesListInOrganization200Response.to_json())

# convert the object into a dict
codespaces_list_in_organization200_response_dict = codespaces_list_in_organization200_response_instance.to_dict()
# create an instance of CodespacesListInOrganization200Response from a dict
codespaces_list_in_organization200_response_from_dict = CodespacesListInOrganization200Response.from_dict(codespaces_list_in_organization200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


