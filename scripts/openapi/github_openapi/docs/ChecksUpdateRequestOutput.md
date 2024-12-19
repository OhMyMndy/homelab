# ChecksUpdateRequestOutput

Check runs can accept a variety of data in the `output` object, including a `title` and `summary` and can optionally provide descriptive details about the run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | **Required**. | [optional] 
**summary** | **str** | Can contain Markdown. | 
**text** | **str** | Can contain Markdown. | [optional] 
**annotations** | [**List[ChecksCreateRequestOutputAnnotationsInner]**](ChecksCreateRequestOutputAnnotationsInner.md) | Adds information from your analysis to specific lines of code. Annotations are visible in GitHub&#39;s pull request UI. Annotations are visible in GitHub&#39;s pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to the [Update a check run](https://docs.github.com/rest/checks/runs#update-a-check-run) endpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about annotations in the UI, see \&quot;[About status checks](https://docs.github.com/articles/about-status-checks#checks)\&quot;. | [optional] 
**images** | [**List[ChecksCreateRequestOutputImagesInner]**](ChecksCreateRequestOutputImagesInner.md) | Adds images to the output displayed in the GitHub pull request UI. | [optional] 

## Example

```python
from github_openapi.models.checks_update_request_output import ChecksUpdateRequestOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksUpdateRequestOutput from a JSON string
checks_update_request_output_instance = ChecksUpdateRequestOutput.from_json(json)
# print the JSON string representation of the object
print(ChecksUpdateRequestOutput.to_json())

# convert the object into a dict
checks_update_request_output_dict = checks_update_request_output_instance.to_dict()
# create an instance of ChecksUpdateRequestOutput from a dict
checks_update_request_output_from_dict = ChecksUpdateRequestOutput.from_dict(checks_update_request_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


