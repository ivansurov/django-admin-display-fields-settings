from django.http import HttpResponse
try:
    import json
except ImportError:
    from django.utils import simplejson as json


class JsonResponse(HttpResponse):

  def __init__(self, data={}, errors=[], success=True):

    super(JsonResponse, self).__init__(
        json_response(data=data, errors=errors, success=success),
        content_type='application/json'
    )


def json_response(data={}, errors=[], success=True):
  data.update({
    'errors': errors,
    'success': len(errors) == 0 and success,
  })
  return json.dumps(data)
