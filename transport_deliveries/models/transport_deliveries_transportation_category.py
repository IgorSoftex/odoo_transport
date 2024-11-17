from odoo import models, fields, api


class TransportDeliveriesTransportationCategory(models.Model):
    """
    This is a model for transportation categories
    transport_deliveries_transportation_category
    """
    _name = 'transport.deliveries.transportation.category'
    _description = 'Transportation category'
    _parent_name = "parent_id"
    _parent_store = True
    # _rec_name = 'full_name'
    _order = 'name'

    name = fields.Char(
        size=100,
        required=True,
        translate=True,
    )
    full_name = fields.Char(
        string='Complete Name',
        compute='_compute_full_name',
        recursive=True,
        store=True,
        translate=True,
    )
    type = fields.Selection(
        default='car',
        selection=[('car', 'Truck'),
                   ('sea', 'Sea'),
                   ('air', 'Air'),
                   ('railway', 'Railway'),
                   ],
        required=True,
    )
    parent_id = fields.Many2one(
        comodel_name='transport.deliveries.transportation.category',
        string='Parent Category',
        index=True,
        ondelete='cascade',
    )
    parent_path = fields.Char(
        index=True,
        unaccent=False
    )
    child_id = fields.One2many(
        comodel_name='transport.deliveries.transportation.category',
        inverse_name='parent_id',
        string='Child Category',
    )
    description = fields.Text(
        # translate=True,
    )
    cargo_volume = fields.Integer(
        string='Cargo volume (cubic meters)',
        # required=True,
        # default=2,
    )
    cargo_weight = fields.Integer(
        string='Cargo weight (kg)',
        # required=True,
        # default=2,
    )
    active = fields.Boolean(
        default=True
    )

    @api.depends('name', 'parent_id.full_name')
    def _compute_full_name(self):
        """
        This method computes a complete name
        """
        for record in self:
            if record.parent_id:
                record.full_name = '%s / %s' % (
                    record.parent_id.full_name,
                    record.name
                )
            else:
                record.full_name = record.name
