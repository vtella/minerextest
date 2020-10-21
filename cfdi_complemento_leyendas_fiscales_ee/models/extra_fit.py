# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from odoo import api, fields, models, _, tools, release
from odoo.exceptions import UserError, RedirectWarning, ValidationError


class AccountMove(models.Model):
    _name = 'account.move'
    _inherit ='account.move'

    complemento_leyendas_fiscales = fields.Boolean('C. Leyendas Fiscales', help='Este Campo activa el complemento Leyendas Fiscales en el XML durante la Facturacion.')

    leyendas_fiscales_ids = fields.Many2many('complemento.leyenda.fiscal', 'invoice_leyendas_rel', 'move_id',
        'leyenda_id', 'Leyendas Fiscales')


    @api.constrains('leyendas_fiscales_ids','complemento_leyendas_fiscales')
    def _constraint_complemento_leyendas_fiscales(self):
        if self.complemento_leyendas_fiscales and not self.leyendas_fiscales_ids:
            raise UserError("Si se habilita el complemento de leyendas fiscales, debes ingresar las leyendas fiscales que incluira el comprobante.\nPestaña -> Leyendas Fiscales.")
        return True
    

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        res = super(AccountMove, self)._onchange_partner_id()
        if self.partner_id.complemento_leyendas_fiscales:
            self.complemento_leyendas_fiscales = True
            leyendas_ids = [x.id for x in self.partner_id.leyendas_fiscales_ids]
            self.leyendas_fiscales_ids = [(6,0, leyendas_ids)]
        return res