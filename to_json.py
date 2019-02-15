import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args,**kwargs):
        obj = str(func(*args,**kwargs))
        print(json.dumps(obj))
    return wrapped
@to_json
def get_data():
  return {
      'data': 42
  }
get_data()  # вернёт '{"data": 42}'
