from odoo.addons.transport_deliveries.tests.common import TestCommon
from odoo.tests import tagged


@tagged('post_install', '-at_install')
class TestModelMethods(TestCommon):
    """
    This test created for testing model methods
    """

    @classmethod
    def setUpClass(cls):
        super(TestModelMethods, cls).setUpClass()

    def test_04_model_methods_compute_full_name_for_transport(self):
        """
        Compute full_name for transport
        """
        # print('test_04_model_methods_compute_full_name_for_transport')

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

        self.assertEqual(transport.full_name, "{} {}".format(transport.name, transport.registration_number, ))
        return True
