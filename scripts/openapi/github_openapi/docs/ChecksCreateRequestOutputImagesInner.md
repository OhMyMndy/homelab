# ChecksCreateRequestOutputImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt** | **str** | The alternative text for the image. | 
**image_url** | **str** | The full URL of the image. | 
**caption** | **str** | A short image description. | [optional] 

## Example

```python
from github_openapi.models.checks_create_request_output_images_inner import ChecksCreateRequestOutputImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksCreateRequestOutputImagesInner from a JSON string
checks_create_request_output_images_inner_instance = ChecksCreateRequestOutputImagesInner.from_json(json)
# print the JSON string representation of the object
print(ChecksCreateRequestOutputImagesInner.to_json())

# convert the object into a dict
checks_create_request_output_images_inner_dict = checks_create_request_output_images_inner_instance.to_dict()
# create an instance of ChecksCreateRequestOutputImagesInner from a dict
checks_create_request_output_images_inner_from_dict = ChecksCreateRequestOutputImagesInner.from_dict(checks_create_request_output_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


