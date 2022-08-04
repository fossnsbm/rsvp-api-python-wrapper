from . import session


class FossRsvp(object):
    def __init__(self, base="https://rsvp-api.fossnsbm.org/api/v1/"):
        self.base = base

    def _get(self, endpoint: str, extension=None, slug=None):
        url = f"{self.base}{endpoint}"

        if extension is not None:
            url += f"/{extension}"

        if slug is not None:
            url += f"/{slug}"

        resp = session.get(url)
        return resp.json()

    """
    Get all the events
    /api/v1/events/
    """

    def events(self, slug=None, extension=None):
        return self._get(f"events", slug=slug, extension=extension)

    """
    Get event details by slug
    /api/v1/event/slug
    """

    def event(self, slug: str, extension="info"):
        return self._get(f"event", slug=slug, extension=extension)
