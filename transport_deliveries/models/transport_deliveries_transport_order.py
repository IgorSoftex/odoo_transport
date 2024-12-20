from odoo import models, fields


class TransportDeliveriesTransportOrder(models.Model):
    """
    This is a model for transport orders
    transport_deliveries_transport_order
    """
    _name = 'transport.deliveries.transport.order'
    _description = 'Transport Order'
    # _rec_name = 'full_name'
    _order = "order_date DESC"

    order_date = fields.Datetime(
        string='Order date',
        required=True,
        help='Order date',
    )
    delivery_date = fields.Date(
        string='Delivery date',
        required=True,
        help='Delivery date',
    )
    carrier_id = fields.Many2one(
        comodel_name='res.partner',
        string='Carrier',
        help='Carrier (Transport Company)',
    )
    contact_person_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contact Person',
        help='Transport Company Contact Person',
    )
    shipment_place = fields.Char(
        string='Shipment Place',
        help='Shipment Place',
        size=200,
        required=True,
        # translate=True,
    )
    delivery_place = fields.Char(
        string='Delivery Place',
        help='Delivery Place',
        size=200,
        required=True,
        # translate=True,
    )
    transport_type = fields.Selection(
        default='car',
        selection=[('car', 'Truck'),
                   ('sea', 'Sea'),
                   ('air', 'Air'),
                   ('railway', 'Railway'),
                   ],
        required=True,
    )
    order_state = fields.Selection(
        string="Order state",
        default='draft',
        selection=[('draft', 'Draft'),
                   ('confirmed', 'Confirmed'),
                   ('in_progress', 'In Progress'),
                   ('completed', 'Completed'),
                   ('cancelled', 'Cancelled'),
                   ]
    )
    order_amount = fields.Float(string="Order Amount",
                                help='Order Amount',
                                # required=True,
                                )
    transport_order_line_ids = fields.One2many(
        comodel_name='transport.deliveries.transport.order.line',
        inverse_name='transport_order_id',
        string='Transport Order Line',
        help='Transport Order Line',
    )
    company_id = fields.Many2one('res.company',
                                 string='Company',
                                 compute='compute_company_id',
                                 # stored='False',
                                 )
    description = fields.Text(
        # translate=True,
    )
    active = fields.Boolean(
        default=True
    )

    def compute_company_id(self):
        """
        This method computes a company_id
        """
        for record in self:
            record.company_id = record.env.company
