# coding: utf-8

"""
    ComicBagi

    PHP Symfony-based comic hosting catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicbagi_openapi.models.comic_chapter import ComicChapter

class TestComicChapter(unittest.TestCase):
    """ComicChapter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComicChapter:
        """Test ComicChapter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComicChapter`
        """
        model = ComicChapter()
        if include_optional:
            return ComicChapter(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                number = 1.337,
                version = '',
                destination_link_count = 56
            )
        else:
            return ComicChapter(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                number = 1.337,
                destination_link_count = 56,
        )
        """

    def testComicChapter(self):
        """Test ComicChapter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()