from odoo.addons.transport_deliveries.tests.common import TestCommon
from odoo.tests import tagged


@tagged('post_install', '-at_install')
class TestSystemHealth(TestCommon):
    """
    This test created for testing system health
    """

    @classmethod
    def setUpClass(cls):
        super(TestSystemHealth, cls).setUpClass()

    def test_01_system_health(self):
        """
        System health
        """
        # print('test_01_system_health')
        return True
