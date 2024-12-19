# OrgsListAppInstallations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**installations** | [**List[Installation]**](Installation.md) |  | 

## Example

```python
from github_openapi.models.orgs_list_app_installations200_response import OrgsListAppInstallations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsListAppInstallations200Response from a JSON string
orgs_list_app_installations200_response_instance = OrgsListAppInstallations200Response.from_json(json)
# print the JSON string representation of the object
print(OrgsListAppInstallations200Response.to_json())

# convert the object into a dict
orgs_list_app_installations200_response_dict = orgs_list_app_installations200_response_instance.to_dict()
# create an instance of OrgsListAppInstallations200Response from a dict
orgs_list_app_installations200_response_from_dict = OrgsListAppInstallations200Response.from_dict(orgs_list_app_installations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

