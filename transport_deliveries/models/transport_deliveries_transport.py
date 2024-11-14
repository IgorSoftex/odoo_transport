from odoo import models, fields, api


class TransportDeliveriesTransport(models.Model):
    """
    This is a model for transport
    transport_deliveries_transport
    """
    _name = 'transport.deliveries.transport'
    _description = 'Transport'
    _order = 'name'

    name = fields.Char(
        help='Name',
        size=100,
        required=True,
        # translate=True,
    )
    full_name = fields.Char(
        string="Transport name",
        compute='_compute_full_name',
        store=False,
        readonly=True,
    )
    category_id = fields.Many2one(
        comodel_name='transport.deliveries.transportation.category',
        string='Category',
        index=True,
        required=True,
        # ondelete='cascade',
    )
    vehicle_brand_id = fields.Many2one(
        comodel_name='transport.deliveries.vehicle.brand',
        string='Brand',
        index=True,
        # ondelete='cascade',
    )
    picture = fields.Image(
        max_width=128,
        max_height=128,
    )
    description = fields.Text(
        help='Description',
        # translate=True,
    )
    registration_number = fields.Char(
        string='Registration number',
        size=40,
        help='Registration number',
        # translate=True,
    )
    active = fields.Boolean(
        default=True,
    )

    @api.depends('name', 'registration_number')
    def _compute_full_name(self):
        """
        This method computes full_name
        """
        for record in self:
            if record.name and record.registration_number:
                record.full_name = record.name + ' ' + record.registration_number
            elif record.name:
                record.full_name = record.name
            elif record.registration_number:
                record.full_name = record.registration_number
            else:
                record.full_name = ''
