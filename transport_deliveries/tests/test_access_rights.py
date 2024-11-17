from odoo.addons.transport_deliveries.tests.common import TestCommon
from odoo.tests import tagged, users
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install')
class TestAccessRights(TestCommon):
    """
    This test created for testing access rights
    """

    @classmethod
    def setUpClass(cls):
        super(TestAccessRights, cls).setUpClass()

    @users('transport_deliveries_car_manager')
    def test_02_access_rights_car_manager_can_create_transport_truck(self):
        """
        Access rights: Car Manager can create a transport category and a transport (truck)
        """
        # print('test_02_access_rights_car_manager_can_create_transport_truck')

        transport_category = self.env['transport.deliveries.transportation.category'].create({
            'name': 'Test Transport Category',
            'full_name': 'Test Transport Category',
            'description': 'Test Transport Category',
            'type': 'car',
        })
        # print('transport_category:', transport_category, transport_category.name)

        vehicle_brand = self.env['transport.deliveries.vehicle.brand'].create({
            'name': 'Test Vehicle Brand',
            'description': 'Test Vehicle Brand',
        })
        # print('vehicle_brand:', vehicle_brand, vehicle_brand.name)

        transport = self.env['transport.deliveries.transport'].create({
            'name': 'Test truck',
            'description': 'Test truck',
            'category_id': transport_category.id,
            'vehicle_brand_id': vehicle_brand.id,
            'registration_number': 'CA 2518 TT',
        })
        # print('transport:', transport, transport.full_name)

        return True

    @users('transport_deliveries_car_manager')
    def test_03_access_rights_car_manager_cannot_create_transport_truck(self):
        """
                Access rights: Car Manager cannot create a transport category and a transport (ship)
        """
        # print('test_03_access_rights_car_manager_cannot_create_transport_truck')
        with self.assertRaises(AccessError):
            transport_category = self.env['transport.deliveries.transportation.category'].create({
                'name': 'Test Transport Category',
                'full_name': 'Test Transport Category',
                'description': 'Test Transport Category',
                'type': 'sea',
            })
            # print('transport_category:', transport_category, transport_category.name)

            # vehicle_brand = self.env['transport.deliveries.vehicle.brand'].create({
            #     'name': 'Test Vehicle Brand',
            #     'description': 'Test Vehicle Brand',
            # })
            # # print('vehicle_brand:', vehicle_brand, vehicle_brand.name)

            transport = self.env['transport.deliveries.transport'].create({
                'name': 'Test ship',
                'description': 'Test ship',
                'category_id': transport_category.id,
                # 'vehicle_brand_id': vehicle_brand.id,
                'registration_number': 'Container 001-777',
            })
            # print('transport:', transport, transport.full_name)
        return True
