Flask-Jsonpify
==============

Flask-Jsonpify is an extension to Flask's core jsonify function,
returning JSON-Padded responses when a callback is specified as
request's arguments. It's usage and implementation is the same as
flask.jsonify, differing only when a request has a ``callback``
specified in the request arguments, in which case the response body is
JSON-Padded, or JSONP, using the callback.

To add JSONP support to all routes which previously used flask.jsonify,
simply import jsonify from flask.ext.jsonpify instead of importing it
from flask. The arguments and responses are fully compatible.
Alternatively, import jsonpify from flask.ext.jsonpify to support JSONP
in certain places.

Installation
------------

Install the extension with one of the following commands:

.. code:: bash

    $ easy_install flask-jsonpify

or alternatively if you have pip installed (which you should):

.. code:: bash

    $ pip install flask-jsonpify

Usage
-----

The best way to use Flask-Jsonpify is to completely replace Flask's
jsonify with this module's jsonify function, as shown below. The method
is fully compatible.

.. code:: Python

    from flask import Flask
    from flask.ext.jsonpify import jsonify

    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify(user="lala")


    if __name__ == "__main__":
        app.run(debug=True)

