from flask import current_app, json, request


def __pad(strdata):
    """ Pads `strdata` with a Request's callback argument, if specified, or does
    nothing.
    """
    if request.args.get('callback'):
        return "%s(%s);" % (request.args.get('callback'), strdata)
    else:
        return strdata


def __mimetype():
    if request.args.get('callback'):
        return 'application/javascript'
    else:
        return 'application/json'


def __dumps(*args, **kwargs):
    """ Serializes `args` and `kwargs` as JSON. Supports serializing an array
    as the top-level object, if it is the only argument.
    """
    indent = None
    if (current_app.config.get('JSONIFY_PRETTYPRINT_REGULAR', False)
            and not request.is_xhr):
        indent = 2
    return json.dumps(args[0] if len(args) is 1 else dict(*args, **kwargs),
                      indent=indent)


def jsonpify(*args, **kwargs):
    """Creates a :class:`~flask.Response` with the JSON or JSON-P
    representation of the given arguments with an `application/json`
    or `application/javascript` mimetype, respectively.  The arguments
    to this function are the same as to the :class:`dict` constructor,
    but also accept an array. If a `callback` is specified in the
    request arguments, the response is JSON-Padded.

    Example usage::

        @app.route('/_get_current_user')
        def get_current_user():
            return jsonify(username=g.user.username,
                           email=g.user.email,
                           id=g.user.id)


    GET /_get_current_user:
    This will send a JSON response like this to the browser::

        {
            "username": "admin",
            "email": "admin@localhost",
            "id": 42
        }

    or, if a callback is specified,

    GET /_get_current_user?callback=displayUsers

    Will result in a JSON response like this to the browser::
        displayUsers({
            "username": "admin",
            "email": "admin@localhost",
            "id": 42
        });

    This requires Python 2.6 or an installed version of simplejson.  For
    security reasons only objects are supported toplevel.  For more
    information about this, have a look at :ref:`json-security`.

    .. versionadded:: 0.2

    """
    return current_app.response_class(__pad(__dumps(*args, **kwargs)),
                                      mimetype=__mimetype())


jsonify = jsonpify  # allow override of Flask's jsonify.
