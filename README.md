# FossRsvp

FossRsvp is a Python wrapper for [RSVP Rest API](https://rsvp.fossnsbm.org/)

## Usage Examples

Below are some basic examples of how to use FossRsvp. Please read the documentation below to see all the methods and more examples.

```python
from fossrsvp import FossRsvp

service = FossRsvp()

events = service.events()
print(events)
```
