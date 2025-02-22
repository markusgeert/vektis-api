# coding: utf-8

"""
    Vektis.AGB.WebAPI.Raadplegen (test-agb-api.vektis.nl/) v2

    De raadpleegdienst biedt de mogelijkheid voor diverse bevragingen op AGB. De informatie die beschikbaar is, kan gebruikt worden voor het aanvragen van AGB-codes met de aanvraagdienst.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_referentiegegevens_relatie_type import VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType

class TestVektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType(unittest.TestCase):
    """VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType:
        """Test VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType`
        """
        model = VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType()
        if include_optional:
            return VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType(
                code = '0',
                omschrijving = '0'
            )
        else:
            return VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType(
                code = '0',
                omschrijving = '0',
        )
        """

    def testVektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType(self):
        """Test VektisAGBWebAPIRaadplegenDataContractsReferentiegegevensRelatieType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
