from fossrsvp import Fossrsvp

service = Fossrsvp()


def test_fetch_events():
    resp = service.events()
    print(resp)


def test_fetch_one_event():
    resp = service.event(slug="shift-into-foss")
    print(resp)
