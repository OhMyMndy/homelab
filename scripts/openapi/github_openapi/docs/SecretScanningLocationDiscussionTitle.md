# SecretScanningLocationDiscussionTitle

Represents a 'discussion_title' secret scanning location type. This location type shows that a secret was detected in the title of a discussion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discussion_title_url** | **str** | The URL to the discussion where the secret was detected. | 

## Example

```python
from github_openapi.models.secret_scanning_location_discussion_title import SecretScanningLocationDiscussionTitle

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningLocationDiscussionTitle from a JSON string
secret_scanning_location_discussion_title_instance = SecretScanningLocationDiscussionTitle.from_json(json)
# print the JSON string representation of the object
print(SecretScanningLocationDiscussionTitle.to_json())

# convert the object into a dict
secret_scanning_location_discussion_title_dict = secret_scanning_location_discussion_title_instance.to_dict()
# create an instance of SecretScanningLocationDiscussionTitle from a dict
secret_scanning_location_discussion_title_from_dict = SecretScanningLocationDiscussionTitle.from_dict(secret_scanning_location_discussion_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


