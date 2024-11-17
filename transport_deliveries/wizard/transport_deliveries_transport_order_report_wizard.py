from datetime import datetime
from odoo import models, fields, api


class TransportDeliveriesTransportOrderReport(models.TransientModel):
    _name = 'transport.deliveries.transport.order.report.wizard'
    _description = 'Transport Order Report'

    begin_date = fields.Date(
        string='Start of period',
    )
    end_date = fields.Date(
        string='Period end',
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

    def run_transport_order_report(self):
        print('run_transport_order_report')
        domain = [
            ('order_date', '>=', self.begin_date),
            ('order_date', '<=', self.end_date),
        ]
        if self.transport_type:
            domain.append(('transport_type', '=', self.transport_type))
        transport_orders = self.env['transport.deliveries.transport.order'].search(domain)
        for transport_order in transport_orders:
            print('transport_order:', transport_order)
        return {
            'name': 'Transport Order Report',
            'type': 'ir.actions.act_window',
            'res_model': 'transport.deliveries.transport.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', transport_orders.ids)],
            'context': {'group_by': 'transport_type'},
        }

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['begin_date'] = datetime.today().replace(day=1)
        res['end_date'] = datetime.now()
        # if self.env.context.get('active_ids'):
        #     doctor_ids = (self.env['odoo.project.hospital.doctors'].
        #                   browse(self.env.context.get('active_ids')))
        #     res['doctor_ids'] = doctor_ids
        return res
