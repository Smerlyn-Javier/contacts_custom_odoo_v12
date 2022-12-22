from odoo import api, fields, models


class ContactsInherited(models.Model):
    _inherit = 'res.partner'

    # Add new fields
    partners_multi_phones = fields.Char(string='Multi phones', store=True)
