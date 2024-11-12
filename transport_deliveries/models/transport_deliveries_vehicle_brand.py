from odoo import models, fields, api


class TransportDeliveriesVehicleBrand(models.Model):
    """
    This is a model for vehicle brands
    transport_deliveries_vehicle_brand
    """
    _name = 'transport.deliveries.vehicle.brand'
    _description = 'Vehicle brands'
    _order = 'name'

    name = fields.Char(
        size=100,
        help='Name',
        # translate=True,
    )
    description = fields.Text(
        help='Description',
        # translate=True,
    )
    active = fields.Boolean(
        default=True
    )
