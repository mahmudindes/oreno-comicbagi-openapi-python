# coding: utf-8

"""
    ComicBagi

    PHP Symfony-based comic hosting catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicbagi_openapi.models.set_language import SetLanguage

class TestSetLanguage(unittest.TestCase):
    """SetLanguage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetLanguage:
        """Test SetLanguage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetLanguage`
        """
        model = SetLanguage()
        if include_optional:
            return SetLanguage(
                lang = '',
                name = ''
            )
        else:
            return SetLanguage(
        )
        """

    def testSetLanguage(self):
        """Test SetLanguage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
