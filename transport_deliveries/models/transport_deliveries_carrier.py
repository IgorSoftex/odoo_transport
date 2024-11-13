from odoo import models, fields, api


class TransportDeliveriesCarrier(models.Model):
    """
    This is a model for Carriers
    res_partner
    """
    _inherit = "res.partner"
    _description = 'Carriers'

    is_carrier = fields.Boolean(
        string="Carrier",
        help="The partner is a carrier",
        default=False,
        required=True,
    )
