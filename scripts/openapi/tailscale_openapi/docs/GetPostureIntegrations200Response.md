# GetPostureIntegrations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | [**List[PostureIntegration]**](PostureIntegration.md) | List of PostureIntegrations. | [optional] 

## Example

```python
from tailscale_openapi.models.get_posture_integrations200_response import GetPostureIntegrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostureIntegrations200Response from a JSON string
get_posture_integrations200_response_instance = GetPostureIntegrations200Response.from_json(json)
# print the JSON string representation of the object
print(GetPostureIntegrations200Response.to_json())

# convert the object into a dict
get_posture_integrations200_response_dict = get_posture_integrations200_response_instance.to_dict()
# create an instance of GetPostureIntegrations200Response from a dict
get_posture_integrations200_response_from_dict = GetPostureIntegrations200Response.from_dict(get_posture_integrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


