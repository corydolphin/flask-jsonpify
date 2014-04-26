# -*- coding: utf-8 -*-
"""
    test
    ~~~~

    Flask-JSONPIFY tests module
"""

try:
    import unittest2 as unittest
except ImportError:
    import unittest
try:
    # this is how you would normally import
    from flask.ext.jsonpify import jsonify
except:
    # support local usage without installed package
    from flask_cors import jsonify

from flask import Flask
from flask.ext.testing import TestCase

ContentType = 'Content-Type'

test_list_int = [i for i in range(10)]
test_list_dicts = [{'user_id':i} for i in range(10)]
test_dict = {'foo':'bar'}

def _create_app():
    app = Flask(__name__)
    @app.route('/list_test')
    def list_test():
        return jsonify(test_list_int)

    @app.route('/list_test_dict')
    def list_test_dict():
        return jsonify(test_list_dicts)    

    @app.route('/')
    def simple():
        return jsonify(test_dict)    


    return app

class FlaskJsonifyTestCase(TestCase):
    def create_app(self):
        return _create_app()


class SerializationTestCase(FlaskJsonifyTestCase):
    def test_list(self):
        resp = self.client.get('/list_test')
        self.assertEqual(resp.json, test_list_int)

    def test_list_dicts(self):
        resp = self.client.get('/list_test_dict')
        self.assertEqual(resp.json, test_list_dicts)

    def test_dict(self):
        resp = self.client.get('/')
        self.assertEqual(resp.json, test_dict)



class ContentTypeTestCase(FlaskJsonifyTestCase):
    def test_unpadded(self):
        for url in ['/','/list_test','/list_test_dict']:
            resp = self.client.get(url)
            self.assertEqual(resp.headers[ContentType], u'application/json')


    def test_padded(self):
        for url in ['/','/list_test','/list_test_dict']:
            resp = self.client.get("%s?callback=example" % url)
            self.assertEqual(resp.headers[ContentType], u'application/javascript')
            self.assertEqual("example(" in resp.data.decode("utf-8"), True)


if __name__ == "__main__":
    unittest.main()