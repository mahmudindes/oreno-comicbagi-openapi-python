# coding: utf-8

"""
    ComicBagi

    PHP Symfony-based comic hosting catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from comicbagi_openapi.models.new_comic_chapter_destination_link import NewComicChapterDestinationLink

class TestNewComicChapterDestinationLink(unittest.TestCase):
    """NewComicChapterDestinationLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewComicChapterDestinationLink:
        """Test NewComicChapterDestinationLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewComicChapterDestinationLink`
        """
        model = NewComicChapterDestinationLink()
        if include_optional:
            return NewComicChapterDestinationLink(
                link_website_host = '',
                link_relative_reference = '',
                released_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return NewComicChapterDestinationLink(
                link_website_host = '',
        )
        """

    def testNewComicChapterDestinationLink(self):
        """Test NewComicChapterDestinationLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()