# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class ModelElementUpdate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator
    (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, type=None, param=None):  # noqa: E501
        """ModelElementUpdate - a model defined in OpenAPI

        :param name: The name of this ModelElementUpdate.  # noqa: E501
        :type name: str
        :param type: The type of this ModelElementUpdate.  # noqa: E501
        :type type: str
        :param param: The param of this ModelElementUpdate.  # noqa: E501
        :type param: object
        """
        self.openapi_types = {
            'name': str,
            'type': str,
            'param': object
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'param': 'param'
        }

        self._name = name
        self._type = type
        self._param = param

    @classmethod
    def from_dict(cls, dikt) -> 'ModelElementUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelElementUpdate of this ModelElementUpdate.  # noqa: E501
        :rtype: ModelElementUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ModelElementUpdate.

        Name of model element  # noqa: E501

        :return: The name of this ModelElementUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelElementUpdate.

        Name of model element  # noqa: E501

        :param name: The name of this ModelElementUpdate.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ModelElementUpdate.

        CIM type of model element  # noqa: E501

        :return: The type of this ModelElementUpdate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelElementUpdate.

        CIM type of model element  # noqa: E501

        :param type: The type of this ModelElementUpdate.
        :type type: str
        """

        self._type = type

    @property
    def param(self):
        """Gets the param of this ModelElementUpdate.

        Element attributes, e.g. strings and numbers  # noqa: E501

        :return: The param of this ModelElementUpdate.
        :rtype: object
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this ModelElementUpdate.

        Element attributes, e.g. strings and numbers  # noqa: E501

        :param param: The param of this ModelElementUpdate.
        :type param: object
        """

        self._param = param
