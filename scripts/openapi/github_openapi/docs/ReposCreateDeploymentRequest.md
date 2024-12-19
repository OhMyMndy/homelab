# ReposCreateDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | The ref to deploy. This can be a branch, tag, or SHA. | 
**task** | **str** | Specifies a task to execute (e.g., &#x60;deploy&#x60; or &#x60;deploy:migrations&#x60;). | [optional] [default to 'deploy']
**auto_merge** | **bool** | Attempts to automatically merge the default branch into the requested ref, if it&#39;s behind the default branch. | [optional] [default to True]
**required_contexts** | **List[str]** | The [status](https://docs.github.com/rest/commits/statuses) contexts to verify against commit status checks. If you omit this parameter, GitHub verifies all unique contexts before creating a deployment. To bypass checking entirely, pass an empty array. Defaults to all unique contexts. | [optional] 
**payload** | [**ReposCreateDeploymentRequestPayload**](ReposCreateDeploymentRequestPayload.md) |  | [optional] 
**environment** | **str** | Name for the target deployment environment (e.g., &#x60;production&#x60;, &#x60;staging&#x60;, &#x60;qa&#x60;). | [optional] [default to 'production']
**description** | **str** | Short description of the deployment. | [optional] [default to '']
**transient_environment** | **bool** | Specifies if the given environment is specific to the deployment and will no longer exist at some point in the future. Default: &#x60;false&#x60; | [optional] [default to False]
**production_environment** | **bool** | Specifies if the given environment is one that end-users directly interact with. Default: &#x60;true&#x60; when &#x60;environment&#x60; is &#x60;production&#x60; and &#x60;false&#x60; otherwise. | [optional] 

## Example

```python
from github_openapi.models.repos_create_deployment_request import ReposCreateDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateDeploymentRequest from a JSON string
repos_create_deployment_request_instance = ReposCreateDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateDeploymentRequest.to_json())

# convert the object into a dict
repos_create_deployment_request_dict = repos_create_deployment_request_instance.to_dict()
# create an instance of ReposCreateDeploymentRequest from a dict
repos_create_deployment_request_from_dict = ReposCreateDeploymentRequest.from_dict(repos_create_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


