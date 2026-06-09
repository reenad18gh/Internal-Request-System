from odoo import models, fields, api
from odoo.exceptions import ValidationError

class InternalRequest(models.Model):
    _name = 'internal.request'
    _description = 'Internal Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Request Reference", required=True, copy=False, default="New")
    employee_name = fields.Char(string="Employee Name", required=True)
    request_type = fields.Selection([
        ('leave', 'Leave Request'),
        ('purchase', 'Purchase Request'),
        ('support', 'IT Support'),
        ('other', 'Other')
    ], string="Request Type", required=True)

    description = fields.Text(string="Description")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', tracking=True)

    def action_submit(self):
        for rec in self:
            rec.state = 'submitted'

    def action_approve(self):
        for rec in self:
            rec.state = 'approved'

    def action_reject(self):
        for rec in self:
            rec.state = 'rejected'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('internal.request.seq') or 'New'
        return super().create(vals)
