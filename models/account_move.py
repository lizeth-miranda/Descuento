# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models, api


class descuento(models.Model):
    _inherit = "account.move"

    des = fields.Float(compute="compute_get_descuento",
                       string="Amortizacion Anticipo",)

    price = fields.Float(compute="compute_price", string="Importe Base",)

    @api.depends("discount")
    def compute_get_descuento(self):
        for record in self:
            record.des = sum(self.env['account.move.line'].search([
                ('discount', '>', 0),
            ]).mapped('descuento'))

    @api.depends("discount")
    def compute_price(self):
        for record in self:
            record.price = sum(self.env['account.move.line'].search([
                ('discount', '>', 0),
            ]).mapped('precio'))
