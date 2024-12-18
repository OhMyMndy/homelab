# ListTailnetKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[Key]**](Key.md) | A list of the active keys. | [optional] 

## Example

```python
from tailscale_openapi.models.list_tailnet_keys200_response import ListTailnetKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTailnetKeys200Response from a JSON string
list_tailnet_keys200_response_instance = ListTailnetKeys200Response.from_json(json)
# print the JSON string representation of the object
print(ListTailnetKeys200Response.to_json())

# convert the object into a dict
list_tailnet_keys200_response_dict = list_tailnet_keys200_response_instance.to_dict()
# create an instance of ListTailnetKeys200Response from a dict
list_tailnet_keys200_response_from_dict = ListTailnetKeys200Response.from_dict(list_tailnet_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


