# ReposCreatePagesDeploymentRequest

The object used to create GitHub Pages deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **float** | The ID of an artifact that contains the .zip or .tar of static assets to deploy. The artifact belongs to the repository. Either &#x60;artifact_id&#x60; or &#x60;artifact_url&#x60; are required. | [optional] 
**artifact_url** | **str** | The URL of an artifact that contains the .zip or .tar of static assets to deploy. The artifact belongs to the repository. Either &#x60;artifact_id&#x60; or &#x60;artifact_url&#x60; are required. | [optional] 
**environment** | **str** | The target environment for this GitHub Pages deployment. | [optional] [default to 'github-pages']
**pages_build_version** | **str** | A unique string that represents the version of the build for this deployment. | [default to 'GITHUB_SHA']
**oidc_token** | **str** | The OIDC token issued by GitHub Actions certifying the origin of the deployment. | 

## Example

```python
from github_openapi.models.repos_create_pages_deployment_request import ReposCreatePagesDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreatePagesDeploymentRequest from a JSON string
repos_create_pages_deployment_request_instance = ReposCreatePagesDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreatePagesDeploymentRequest.to_json())

# convert the object into a dict
repos_create_pages_deployment_request_dict = repos_create_pages_deployment_request_instance.to_dict()
# create an instance of ReposCreatePagesDeploymentRequest from a dict
repos_create_pages_deployment_request_from_dict = ReposCreatePagesDeploymentRequest.from_dict(repos_create_pages_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


