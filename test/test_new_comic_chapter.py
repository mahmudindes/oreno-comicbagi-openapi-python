# coding: utf-8

"""
    ComicBagi

    PHP Symfony-based comic hosting catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicbagi_openapi.models.new_comic_chapter import NewComicChapter

class TestNewComicChapter(unittest.TestCase):
    """NewComicChapter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewComicChapter:
        """Test NewComicChapter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewComicChapter`
        """
        model = NewComicChapter()
        if include_optional:
            return NewComicChapter(
                number = 1.337,
                version = ''
            )
        else:
            return NewComicChapter(
                number = 1.337,
        )
        """

    def testNewComicChapter(self):
        """Test NewComicChapter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
