from odoo import models, fields, api


class TransportDeliveriesTransportOrderLine(models.Model):
    """
    This is a model for transport orders lines
    transport_deliveries_transport_order_line
    """
    _name = 'transport.deliveries.transport.order.line'
    _description = 'Transport Order Line'
    # _rec_name = 'full_name'
    # _order = "order_date DESC"

    transport_order_id = fields.Many2one(
        comodel_name='transport.deliveries.transport.order',
        string='Transport Order',
        help='Transport Order',
        index=True,
    )
    transport_id = fields.Many2one(
        comodel_name='transport.deliveries.transport',
        string='Transport',
        help='Transport',
    )
    transport_id_registration_number = fields.Char(
        string='Registration number',
        help='Transport registration number',
        compute='_compute_transport_registration_number',
        store=False,
        readonly=True,
        # translate=True,
    )
    description = fields.Text(
        # translate=True,
    )
    active = fields.Boolean(
        default=True
    )

    @api.depends('transport_id')
    def _compute_transport_registration_number(self):
        for record in self:
            record.transport_id_registration_number = record.transport_id.registration_number
