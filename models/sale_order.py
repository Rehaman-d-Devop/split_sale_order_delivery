# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare
from odoo.tools import format_date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    f_delivery_split = fields.Boolean(string="Delivery split")    
    
    @api.onchange("commitment_date")
    def _onchange_commitment_date(self):
        """Update empty commitment date order lines with commitment date from sale order"""
        result = super()._onchange_commitment_date() or {}
        if "warning" not in result:
            for line in self.order_line:
                if not line.f_planned_date:
                    line.f_planned_date = self.commitment_date
        return result
    
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if self.f_delivery_split:
            if not self.commitment_date:
                raise UserError("Please set the delivery date on the header.")
            if self.order_line:
                for line in self.order_line:
                    if not line.f_planned_date:
                        line.f_planned_date = self.commitment_date
        return res
    
