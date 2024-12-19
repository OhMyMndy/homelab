# ChecksCreateRequestOutput

Check runs can accept a variety of data in the `output` object, including a `title` and `summary` and can optionally provide descriptive details about the run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the check run. | 
**summary** | **str** | The summary of the check run. This parameter supports Markdown. **Maximum length**: 65535 characters. | 
**text** | **str** | The details of the check run. This parameter supports Markdown. **Maximum length**: 65535 characters. | [optional] 
**annotations** | [**List[ChecksCreateRequestOutputAnnotationsInner]**](ChecksCreateRequestOutputAnnotationsInner.md) | Adds information from your analysis to specific lines of code. Annotations are visible on GitHub in the **Checks** and **Files changed** tab of the pull request. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to the [Update a check run](https://docs.github.com/rest/checks/runs#update-a-check-run) endpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about how you can view annotations on GitHub, see \&quot;[About status checks](https://docs.github.com/articles/about-status-checks#checks)\&quot;. | [optional] 
**images** | [**List[ChecksCreateRequestOutputImagesInner]**](ChecksCreateRequestOutputImagesInner.md) | Adds images to the output displayed in the GitHub pull request UI. | [optional] 

## Example

```python
from github_openapi.models.checks_create_request_output import ChecksCreateRequestOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksCreateRequestOutput from a JSON string
checks_create_request_output_instance = ChecksCreateRequestOutput.from_json(json)
# print the JSON string representation of the object
print(ChecksCreateRequestOutput.to_json())

# convert the object into a dict
checks_create_request_output_dict = checks_create_request_output_instance.to_dict()
# create an instance of ChecksCreateRequestOutput from a dict
checks_create_request_output_from_dict = ChecksCreateRequestOutput.from_dict(checks_create_request_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


