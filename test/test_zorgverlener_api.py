# coding: utf-8

"""
    Vektis.AGB.WebAPI.Raadplegen (test-agb-api.vektis.nl/) v2

    De raadpleegdienst biedt de mogelijkheid voor diverse bevragingen op AGB. De informatie die beschikbaar is, kan gebruikt worden voor het aanvragen van AGB-codes met de aanvraagdienst.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vektis_api.api.zorgverlener_api import ZorgverlenerApi


class TestZorgverlenerApi(unittest.TestCase):
    """ZorgverlenerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ZorgverlenerApi()

    def tearDown(self) -> None:
        pass

    def test_zorgverlener_basisinformatie(self) -> None:
        """Test case for zorgverlener_basisinformatie

        Raadplegen van basisinformatie van een zorgverlener
        """
        pass

    def test_zorgverlener_basisinformatie_0(self) -> None:
        """Test case for zorgverlener_basisinformatie_0

        Raadplegen van basisinformatie van een zorgverlener op peildatum
        """
        pass

    def test_zorgverlener_zorgpartij_mutaties(self) -> None:
        """Test case for zorgverlener_zorgpartij_mutaties

        Raadplegen van zorgverleners met mutaties
        """
        pass

    def test_zorgverlener_zorgpartij_mutaties_0(self) -> None:
        """Test case for zorgverlener_zorgpartij_mutaties_0

        Raadplegen van zorgverleners met mutaties binnen het opgegeven zorgsoort.
        """
        pass

    def test_zorgverlener_zorgverlener_relaties_totaal_v2(self) -> None:
        """Test case for zorgverlener_zorgverlener_relaties_totaal_v2

        Raadplegen van alle relaties van een zorgverlener
        """
        pass

    def test_zorgverlener_zorgverlener_relaties_v2(self) -> None:
        """Test case for zorgverlener_zorgverlener_relaties_v2

        Raadplegen van de huidige actieve relaties van een zorgverlener
        """
        pass

    def test_zorgverlener_zorgverlener_relaties_v2_0(self) -> None:
        """Test case for zorgverlener_zorgverlener_relaties_v2_0

        Raadplegen relaties van een zorgverlener op peildatum
        """
        pass


if __name__ == '__main__':
    unittest.main()
