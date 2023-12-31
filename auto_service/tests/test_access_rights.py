from common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'auto_service', 'access')
class TestAccessRights(TestCommon):

    def test_01_auto_service_user_access_rights(self):
        with self.assertRaises(AccessError):
            self.env['auto.service'].with_user(self.auto_service_user).create(
                {'name': 'Test Vehicle'})
        with self.assertRaises(AccessError):
            self.vehicle_demo.with_user(self.auto_service_user).unlink()

    def test_02_auto_service_admin_access_rights(self):
        vehicle = self.env['auto.service'].with_user(self.auto_service_admin).create(
            {'name': 'Test Vehicle'})
        vehicle.with_user(self.auto_service_admin).read()
        vehicle.with_user(self.auto_service_admin).write({
            'name': 'Test Vehicle'})
        vehicle.with_user(self.auto_service_admin).unlink()
