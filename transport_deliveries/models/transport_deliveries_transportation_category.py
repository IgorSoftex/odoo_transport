from odoo import models, fields, api


class TransportDeliveriesTransportationCategory(models.Model):
    """
    This is a module for transportation categories
    """
    _name = 'transport.deliveries.transportation.category'
    _description = 'Transportation category'
    _parent_name = "parent_id"
    _parent_store = True
    # _rec_name = 'complete_name'
    _order = 'name'

    name = fields.Char(
        translate=True,
    )
    complete_name = fields.Char(
        string='Complete Name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
        translate=True,
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
    active = fields.Boolean(
        default=True
    )
    description = fields.Text(
        translate=True,
    )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        """
        This method computes a complete name
        """
        for record in self:
            if record.parent_id:
                record.complete_name = '%s / %s' % (
                    record.parent_id.complete_name,
                    record.name
                )
            else:
                record.complete_name = record.name
