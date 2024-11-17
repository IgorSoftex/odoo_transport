from odoo import models, fields


class TransportDeliveriesContactPerson(models.Model):
    """
    This is a model for Contact Persons
    res_partner
    """
    _inherit = "res.partner"
    _description = 'Contact Persons'

    is_carrier_contact_person = fields.Boolean(
        string="Is Carrier Contact Person",
        help="The partner is a carrier contact person (manager or transport driver)",
        default=False,
        # required=True,
    )
