# ReposCreateUsingTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** | The organization or person who will own the new repository. To create a new repository in an organization, the authenticated user must be a member of the specified organization. | [optional] 
**name** | **str** | The name of the new repository. | 
**description** | **str** | A short description of the new repository. | [optional] 
**include_all_branches** | **bool** | Set to &#x60;true&#x60; to include the directory structure and files from all branches in the template repository, and not just the default branch. Default: &#x60;false&#x60;. | [optional] [default to False]
**private** | **bool** | Either &#x60;true&#x60; to create a new private repository or &#x60;false&#x60; to create a new public one. | [optional] [default to False]

## Example

```python
from github_openapi.models.repos_create_using_template_request import ReposCreateUsingTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateUsingTemplateRequest from a JSON string
repos_create_using_template_request_instance = ReposCreateUsingTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateUsingTemplateRequest.to_json())

# convert the object into a dict
repos_create_using_template_request_dict = repos_create_using_template_request_instance.to_dict()
# create an instance of ReposCreateUsingTemplateRequest from a dict
repos_create_using_template_request_from_dict = ReposCreateUsingTemplateRequest.from_dict(repos_create_using_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


