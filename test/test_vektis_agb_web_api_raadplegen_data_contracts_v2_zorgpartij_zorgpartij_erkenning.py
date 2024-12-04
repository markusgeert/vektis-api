# coding: utf-8

"""
    Vektis.AGB.WebAPI.Raadplegen (test-agb-api.vektis.nl/) v2

    De raadpleegdienst biedt de mogelijkheid voor diverse bevragingen op AGB. De informatie die beschikbaar is, kan gebruikt worden voor het aanvragen van AGB-codes met de aanvraagdienst.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_zorgpartij_zorgpartij_erkenning import VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning

class TestVektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning(unittest.TestCase):
    """VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning:
        """Test VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning`
        """
        model = VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning()
        if include_optional:
            return VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning(
                aanvang = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                einde = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                code = '012345',
                omschrijving = '0',
                registratie_nummer = '0'
            )
        else:
            return VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning(
                aanvang = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                code = '012345',
                omschrijving = '0',
                registratie_nummer = '0',
        )
        """

    def testVektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning(self):
        """Test VektisAGBWebAPIRaadplegenDataContractsV2ZorgpartijZorgpartijErkenning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()