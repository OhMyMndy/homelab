# IntegrationInstallationRequest

Request to install an integration on a target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the request installation. | 
**node_id** | **str** |  | [optional] 
**account** | [**IntegrationInstallationRequestAccount**](IntegrationInstallationRequestAccount.md) |  | 
**requester** | [**SimpleUser**](SimpleUser.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.integration_installation_request import IntegrationInstallationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationInstallationRequest from a JSON string
integration_installation_request_instance = IntegrationInstallationRequest.from_json(json)
# print the JSON string representation of the object
print(IntegrationInstallationRequest.to_json())

# convert the object into a dict
integration_installation_request_dict = integration_installation_request_instance.to_dict()
# create an instance of IntegrationInstallationRequest from a dict
integration_installation_request_from_dict = IntegrationInstallationRequest.from_dict(integration_installation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


