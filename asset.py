from odoo import models, fields, api

class Asset(models.Model):
    _name = 'rhoesada.fixed.asset'

    name = fields.Char('Name')
    description = fields.Text('Description')
    purchase_date = fields.Date('Purchase Date')
    asset_life = fields.Integer('Asset Life')
    acquisition_cost = fields.Float('Acquisition Cost')