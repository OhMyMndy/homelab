# ReposCreateDeploymentStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the status. When you set a transient deployment to &#x60;inactive&#x60;, the deployment will be shown as &#x60;destroyed&#x60; in GitHub. | 
**target_url** | **str** | The target URL to associate with this status. This URL should contain output to keep the user updated while the task is running or serve as historical information for what happened in the deployment.  &gt; [!NOTE] &gt; It&#39;s recommended to use the &#x60;log_url&#x60; parameter, which replaces &#x60;target_url&#x60;. | [optional] [default to '']
**log_url** | **str** | The full URL of the deployment&#39;s output. This parameter replaces &#x60;target_url&#x60;. We will continue to accept &#x60;target_url&#x60; to support legacy uses, but we recommend replacing &#x60;target_url&#x60; with &#x60;log_url&#x60;. Setting &#x60;log_url&#x60; will automatically set &#x60;target_url&#x60; to the same value. Default: &#x60;\&quot;\&quot;&#x60; | [optional] [default to '']
**description** | **str** | A short description of the status. The maximum description length is 140 characters. | [optional] [default to '']
**environment** | **str** | Name for the target deployment environment, which can be changed when setting a deploy status. For example, &#x60;production&#x60;, &#x60;staging&#x60;, or &#x60;qa&#x60;. If not defined, the environment of the previous status on the deployment will be used, if it exists. Otherwise, the environment of the deployment will be used. | [optional] 
**environment_url** | **str** | Sets the URL for accessing your environment. Default: &#x60;\&quot;\&quot;&#x60; | [optional] [default to '']
**auto_inactive** | **bool** | Adds a new &#x60;inactive&#x60; status to all prior non-transient, non-production environment deployments with the same repository and &#x60;environment&#x60; name as the created status&#39;s deployment. An &#x60;inactive&#x60; status is only added to deployments that had a &#x60;success&#x60; state. Default: &#x60;true&#x60; | [optional] 

## Example

```python
from github_openapi.models.repos_create_deployment_status_request import ReposCreateDeploymentStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateDeploymentStatusRequest from a JSON string
repos_create_deployment_status_request_instance = ReposCreateDeploymentStatusRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateDeploymentStatusRequest.to_json())

# convert the object into a dict
repos_create_deployment_status_request_dict = repos_create_deployment_status_request_instance.to_dict()
# create an instance of ReposCreateDeploymentStatusRequest from a dict
repos_create_deployment_status_request_from_dict = ReposCreateDeploymentStatusRequest.from_dict(repos_create_deployment_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


