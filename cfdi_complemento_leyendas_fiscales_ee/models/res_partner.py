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


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit ='res.partner'

    complemento_leyendas_fiscales = fields.Boolean('C. Leyendas Fiscales', help='Este Campo activa el complemento Leyendas Fiscales en el XML durante la Facturacion.')

    leyendas_fiscales_ids = fields.One2many('complemento.leyenda.fiscal', 'partner_id', 'Leyendas Fiscales')


    @api.constrains('leyendas_fiscales_ids','complemento_leyendas_fiscales')
    def _constraint_complemento_leyendas_fiscales(self):
        if self.complemento_leyendas_fiscales and not self.leyendas_fiscales_ids:
        	raise UserError("Si se habilita el complemento de leyendas fiscales, debes ingresar las leyendas fiscales que incluira el comprobante.\nPestaña -> Leyendas Fiscales.")
        return True
    


class ComplementoLeyendaFiscal(models.Model):
    _name = 'complemento.leyenda.fiscal'
    _description = 'Normativas para agregar al Complemento'
    _rec_name = 'disposicion' 

    partner_id = fields.Many2one('res.partner', 'ID Ref')

    norma = fields.Char('Norma', size=128, required=True)
    disposicion = fields.Char('Disposicion Fiscal', size=128, required=True)
    texto_leyenda = fields.Char('Texto Leyenda', size=128, required=True)
