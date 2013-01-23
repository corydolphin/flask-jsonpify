from flask import current_app, json, request


def __pad(strdata):
    """ Pads `strdata` with a Request's callback argument, if specified, or does
    nothing.
    """
    if request.args.get('callback'):
        return "%s(%s);" % (request.args.get('callback'), strdata)
    else:
        return strdata


def jsonpify(*args, **kwargs):
    """Creates a :class:`~flask.Response` with the JSON or JSON-P representation of
    the given arguments with an `application/json` mimetype.  The arguments
    to this function are the same as to the :class:`dict` constructor. If a
    `callback` is specified in the request arguments, the response is
    JSON-Padded.

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

    return current_app.response_class(__pad(json.dumps(dict(*args, **kwargs),
        indent=None if request.is_xhr else 2)),
        mimetype='application/json')

jsonify = jsonpify  # allow override of Flask's jsonify.
