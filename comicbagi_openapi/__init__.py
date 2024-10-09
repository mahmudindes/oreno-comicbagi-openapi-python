# coding: utf-8

# flake8: noqa

"""
    ComicBagi

    PHP Symfony-based comic hosting catalog full-stack.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.1"

# import apis into sdk package
from comicbagi_openapi.api.comic_api import ComicApi
from comicbagi_openapi.api.comic_chapter_api import ComicChapterApi
from comicbagi_openapi.api.language_api import LanguageApi
from comicbagi_openapi.api.link_api import LinkApi
from comicbagi_openapi.api.website_api import WebsiteApi

# import ApiClient
from comicbagi_openapi.api_response import ApiResponse
from comicbagi_openapi.api_client import ApiClient
from comicbagi_openapi.configuration import Configuration
from comicbagi_openapi.exceptions import OpenApiException
from comicbagi_openapi.exceptions import ApiTypeError
from comicbagi_openapi.exceptions import ApiValueError
from comicbagi_openapi.exceptions import ApiKeyError
from comicbagi_openapi.exceptions import ApiAttributeError
from comicbagi_openapi.exceptions import ApiException

# import models into sdk package
from comicbagi_openapi.models.comic import Comic
from comicbagi_openapi.models.comic_chapter import ComicChapter
from comicbagi_openapi.models.comic_chapter_destination_link import ComicChapterDestinationLink
from comicbagi_openapi.models.comic_destination_link import ComicDestinationLink
from comicbagi_openapi.models.error import Error
from comicbagi_openapi.models.language import Language
from comicbagi_openapi.models.link import Link
from comicbagi_openapi.models.link_item_language import LinkItemLanguage
from comicbagi_openapi.models.new_comic import NewComic
from comicbagi_openapi.models.new_comic_chapter import NewComicChapter
from comicbagi_openapi.models.new_comic_chapter_destination_link import NewComicChapterDestinationLink
from comicbagi_openapi.models.new_comic_destination_link import NewComicDestinationLink
from comicbagi_openapi.models.new_language import NewLanguage
from comicbagi_openapi.models.new_link import NewLink
from comicbagi_openapi.models.new_link_item_language import NewLinkItemLanguage
from comicbagi_openapi.models.new_website import NewWebsite
from comicbagi_openapi.models.new_website_item_language import NewWebsiteItemLanguage
from comicbagi_openapi.models.set_comic import SetComic
from comicbagi_openapi.models.set_comic_chapter import SetComicChapter
from comicbagi_openapi.models.set_comic_chapter_destination_link import SetComicChapterDestinationLink
from comicbagi_openapi.models.set_comic_destination_link import SetComicDestinationLink
from comicbagi_openapi.models.set_language import SetLanguage
from comicbagi_openapi.models.set_link import SetLink
from comicbagi_openapi.models.set_link_item_language import SetLinkItemLanguage
from comicbagi_openapi.models.set_website import SetWebsite
from comicbagi_openapi.models.set_website_item_language import SetWebsiteItemLanguage
from comicbagi_openapi.models.website import Website
from comicbagi_openapi.models.website_item_language import WebsiteItemLanguage
