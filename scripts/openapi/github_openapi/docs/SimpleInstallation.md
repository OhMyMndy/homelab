# SimpleInstallation

The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured for and sent to a GitHub App. For more information, see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the installation. | 
**node_id** | **str** | The global node ID of the installation. | 

## Example

```python
from github_openapi.models.simple_installation import SimpleInstallation

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleInstallation from a JSON string
simple_installation_instance = SimpleInstallation.from_json(json)
# print the JSON string representation of the object
print(SimpleInstallation.to_json())

# convert the object into a dict
simple_installation_dict = simple_installation_instance.to_dict()
# create an instance of SimpleInstallation from a dict
simple_installation_from_dict = SimpleInstallation.from_dict(simple_installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


