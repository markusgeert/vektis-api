# coding: utf-8

"""
    Vektis.AGB.WebAPI.Raadplegen (test-agb-api.vektis.nl/) v2

    De raadpleegdienst biedt de mogelijkheid voor diverse bevragingen op AGB. De informatie die beschikbaar is, kan gebruikt worden voor het aanvragen van AGB-codes met de aanvraagdienst.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vektis_api.models.vektis_agb_web_api_raadplegen_data_contracts_v2_relatie_zorgpartij_relaties import VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties

class TestVektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties(unittest.TestCase):
    """VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties:
        """Test VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties`
        """
        model = VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties()
        if include_optional:
            return VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties(
                agb_code = '01234567',
                naam = '0',
                relaties = [
                    vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/v2/relatie/relatie.Vektis.AGB.WebAPI.Raadplegen.DataContracts.v2.Relatie.Relatie(
                        aanvang = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        einde = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        agb_code = '01234567', 
                        naam = '0', 
                        rol = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/relatie_rol.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.RelatieRol(
                            code = '0', 
                            omschrijving = '0', ), 
                        type = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/relatie_type.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.RelatieType(
                            code = '0', 
                            omschrijving = '0', ), 
                        zorgaanbod = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/zorgaanbod.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.Zorgaanbod(
                            code = '0', 
                            omschrijving = '0', ), 
                        zorgpartij_type = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/zorgpartij_type.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.ZorgpartijType(
                            code = '0', 
                            omschrijving = '0', ), )
                    ],
                zorgpartij_type = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/zorgpartij_type.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.ZorgpartijType(
                    code = '0', 
                    omschrijving = '0', )
            )
        else:
            return VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties(
                agb_code = '01234567',
                naam = '0',
                relaties = [
                    vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/v2/relatie/relatie.Vektis.AGB.WebAPI.Raadplegen.DataContracts.v2.Relatie.Relatie(
                        aanvang = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        einde = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        agb_code = '01234567', 
                        naam = '0', 
                        rol = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/relatie_rol.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.RelatieRol(
                            code = '0', 
                            omschrijving = '0', ), 
                        type = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/relatie_type.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.RelatieType(
                            code = '0', 
                            omschrijving = '0', ), 
                        zorgaanbod = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/zorgaanbod.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.Zorgaanbod(
                            code = '0', 
                            omschrijving = '0', ), 
                        zorgpartij_type = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/zorgpartij_type.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.ZorgpartijType(
                            code = '0', 
                            omschrijving = '0', ), )
                    ],
                zorgpartij_type = vektis_api.models.vektis/agb/web_api/raadplegen/data_contracts/referentiegegevens/zorgpartij_type.Vektis.AGB.WebAPI.Raadplegen.DataContracts.Referentiegegevens.ZorgpartijType(
                    code = '0', 
                    omschrijving = '0', ),
        )
        """

    def testVektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties(self):
        """Test VektisAGBWebAPIRaadplegenDataContractsV2RelatieZorgpartijRelaties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()