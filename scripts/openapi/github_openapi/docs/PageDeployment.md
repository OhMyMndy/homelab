# PageDeployment

The GitHub Pages deployment status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PageDeploymentId**](PageDeploymentId.md) |  | 
**status_url** | **str** | The URI to monitor GitHub Pages deployment status. | 
**page_url** | **str** | The URI to the deployed GitHub Pages. | 
**preview_url** | **str** | The URI to the deployed GitHub Pages preview. | [optional] 

## Example

```python
from github_openapi.models.page_deployment import PageDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of PageDeployment from a JSON string
page_deployment_instance = PageDeployment.from_json(json)
# print the JSON string representation of the object
print(PageDeployment.to_json())

# convert the object into a dict
page_deployment_dict = page_deployment_instance.to_dict()
# create an instance of PageDeployment from a dict
page_deployment_from_dict = PageDeployment.from_dict(page_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


