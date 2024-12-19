# PageDeploymentId

The ID of the GitHub Pages deployment. This is the Git SHA of the deployed commit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from github_openapi.models.page_deployment_id import PageDeploymentId

# TODO update the JSON string below
json = "{}"
# create an instance of PageDeploymentId from a JSON string
page_deployment_id_instance = PageDeploymentId.from_json(json)
# print the JSON string representation of the object
print(PageDeploymentId.to_json())

# convert the object into a dict
page_deployment_id_dict = page_deployment_id_instance.to_dict()
# create an instance of PageDeploymentId from a dict
page_deployment_id_from_dict = PageDeploymentId.from_dict(page_deployment_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


