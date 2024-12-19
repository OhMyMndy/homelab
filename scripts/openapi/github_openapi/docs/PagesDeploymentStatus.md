# PagesDeploymentStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current status of the deployment. | [optional] 

## Example

```python
from github_openapi.models.pages_deployment_status import PagesDeploymentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PagesDeploymentStatus from a JSON string
pages_deployment_status_instance = PagesDeploymentStatus.from_json(json)
# print the JSON string representation of the object
print(PagesDeploymentStatus.to_json())

# convert the object into a dict
pages_deployment_status_dict = pages_deployment_status_instance.to_dict()
# create an instance of PagesDeploymentStatus from a dict
pages_deployment_status_from_dict = PagesDeploymentStatus.from_dict(pages_deployment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


