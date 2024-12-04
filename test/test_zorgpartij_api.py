# coding: utf-8

"""
    Vektis.AGB.WebAPI.Raadplegen (test-agb-api.vektis.nl/) v2

    De raadpleegdienst biedt de mogelijkheid voor diverse bevragingen op AGB. De informatie die beschikbaar is, kan gebruikt worden voor het aanvragen van AGB-codes met de aanvraagdienst.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vektis_api.api.zorgpartij_api import ZorgpartijApi


class TestZorgpartijApi(unittest.TestCase):
    """ZorgpartijApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ZorgpartijApi()

    def tearDown(self) -> None:
        pass

    def test_zorgpartij_zorgpartij_mutaties(self) -> None:
        """Test case for zorgpartij_zorgpartij_mutaties

        Raadplegen van zorgpartijen met mutaties
        """
        pass

    def test_zorgpartij_zorgpartij_mutaties_0(self) -> None:
        """Test case for zorgpartij_zorgpartij_mutaties_0

        Raadplegen van zorgpartijen met mutaties binnen het opgegeven zorgsoort.
        """
        pass

    def test_zorgpartij_zorgpartijen(self) -> None:
        """Test case for zorgpartij_zorgpartijen

        Raadplegen van actieve zorgpartijen.
        """
        pass

    def test_zorgpartij_zorgpartijen_0(self) -> None:
        """Test case for zorgpartij_zorgpartijen_0

        Raadplegen van actieve zorgpartijen binnen het opgegeven zorgsoort.
        """
        pass


if __name__ == '__main__':
    unittest.main()