from flask import request, jsonify, render_template
import json


def post_request(spec_class=None):
    def wrapper(func):
        def call_post_request(*args, **kwargs):
            json_file = request.get_json()
            if spec_class and json_file:
                spec = spec_class()
                spec.__dict__ = json_file
                return func(spec)
            else:
                return func()

        return call_post_request

    return wrapper


def api_request(spec_class=None):
    def wrapper(func):
        def call_api_request(*args, **kwargs):
            return_object = post_request(spec_class=spec_class)(func)()
            return_json = json.dumps(return_object, default=lambda o: o.__dict__)
            return jsonify(data=return_json)

        return call_api_request

    return wrapper


def post_and_redirect(spec_class=None, filename=None):
    def wrapper(func):
        def call_post_and_redirect(*args, **kwargs):
            return_object = post_request(spec_class=spec_class)(func)()
            return render_template(filename, data=return_object)

        return call_post_and_redirect

    return wrapper
