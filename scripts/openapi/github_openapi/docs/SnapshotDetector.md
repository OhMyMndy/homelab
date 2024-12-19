# SnapshotDetector

A description of the detector used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the detector used. | 
**version** | **str** | The version of the detector used. | 
**url** | **str** | The url of the detector used. | 

## Example

```python
from github_openapi.models.snapshot_detector import SnapshotDetector

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDetector from a JSON string
snapshot_detector_instance = SnapshotDetector.from_json(json)
# print the JSON string representation of the object
print(SnapshotDetector.to_json())

# convert the object into a dict
snapshot_detector_dict = snapshot_detector_instance.to_dict()
# create an instance of SnapshotDetector from a dict
snapshot_detector_from_dict = SnapshotDetector.from_dict(snapshot_detector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


