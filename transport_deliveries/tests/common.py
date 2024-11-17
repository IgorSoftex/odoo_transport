from odoo.tests import TransactionCase

"""
TransactionCase
   setUpClass()         - метод, котрий викликається перед виконанням тестових методів
       setUp()          - дозволяє виконувати певні дії перед виконанням тестового методу.
       test_method_1() 
       tearDown()       - дозволяє виконувати певні дії після виконанням тестового методу.

       setUp()
       test_method_1()
       tearDown()
   tearDownClass()      - метод, котрий викликається після виконання всіх тестових методів
"""


class TestCommon(TransactionCase):
    """
    This test created for learning only
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        """Let's create access groups"""
        cls.access_group_administrator = cls.env.ref(
            'transport_deliveries.group_transport_deliveries_administrator')
        cls.access_group_car_manager = cls.env.ref(
            'transport_deliveries.group_transport_deliveries_car_manager')
        cls.access_group_railway_manager = cls.env.ref(
            'transport_deliveries.group_transport_deliveries_railway_manager')
        cls.access_group_airplanes_manager = cls.env.ref(
            'transport_deliveries.group_transport_deliveries_airplanes_manager')
        cls.access_group_ship_manager = cls.env.ref(
            'transport_deliveries.group_transport_deliveries_ship_manager')
        cls.access_group_accountant = cls.env.ref(
            'transport_deliveries.group_transport_deliveries_accountant')

        """Let's create users"""
        cls.transport_deliveries_administrator = cls.env['res.users'].create({
            'name': 'Administrator user for test',
            'login': 'transport_deliveries_administrator',
            'password': 'transport_deliveries_administrator',
            'email': 'transport_deliveries_administrator@ukr.net',
            'groups_id': [(6, 0, cls.access_group_administrator.ids)],
        })

        cls.transport_deliveries_car_manager = cls.env['res.users'].create({
            'name': 'Car manager user for test',
            'login': 'transport_deliveries_car_manager',
            'password': 'transport_deliveries_car_manager',
            'email': 'transport_deliveries_car_manager@ukr.net',
            'groups_id': [(6, 0, cls.access_group_car_manager.ids)],
        })

        cls.transport_deliveries_railway_manager = cls.env['res.users'].create({
            'name': 'Railway manager user for test',
            'login': 'transport_deliveries_railway_manager',
            'password': 'transport_deliveries_railway_manager',
            'email': 'transport_deliveries_railway_manager@ukr.net',
            'groups_id': [(6, 0, cls.access_group_railway_manager.ids)],
        })

        cls.transport_deliveries_airplanes_manager = cls.env['res.users'].create({
            'name': 'Airplanes manager user for test',
            'login': 'transport_deliveries_airplanes_manager',
            'password': 'transport_deliveries_airplanes_manager',
            'email': 'transport_deliveries_airplanes_manager@ukr.net',
            'groups_id': [(6, 0, cls.access_group_airplanes_manager.ids)],
        })

        cls.transport_deliveries_ship_manager = cls.env['res.users'].create({
            'name': 'Ship manager user for test',
            'login': 'transport_deliveries_ship_manager',
            'password': 'transport_deliveries_ship_manager',
            'email': 'transport_deliveries_ship_manager@ukr.net',
            'groups_id': [(6, 0, cls.access_group_ship_manager.ids)],
        })

        cls.transport_deliveries_accountant = cls.env['res.users'].create({
            'name': 'Car manager user for test',
            'login': 'transport_deliveries_accountant',
            'password': 'transport_deliveries_accountant',
            'email': 'transport_deliveries_accountant@ukr.net',
            'groups_id': [(6, 0, cls.access_group_accountant.ids)],
        })
