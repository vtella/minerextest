# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@argil.mx)
############################################################################
#    Coded by: german_442 email: (german.ponce@argil.mx)

##############################################################################

{
    'name' : 'Complemento - Leyendas Fiscales E.E.',
    'description' : """ 

    Este Modulo Permite incorporar el Complemento de Leyendas Fiscales al generar Facturas CFDI.

    Configuracion

    - Activamos el Campo Leyendas Fiscales, en la Ficha de Clientes.

    - Al generar la Factura en el Sistema, el campo Comentario (Comment), debe incluir el texto que se llevara al nodo Comentario, en la generacion del Complemento.


    """,
    'version' : '1.0',
    'author' : 'German Ponce Dominguez',
    'website' : 'http://poncesoft.blogspot.com',
    'license' : 'GPL-3',
    'category' : 'Nishikawa',
    'depends' : [
                'account',
                'account_invoicing',
                'sale',
                'l10n_mx_edi',
                ],
    'init_xml' : [],
    'data' : [
                    'views/res_partner_view.xml',
                    'views/extra_fit_view.xml',
                    'data/complemento_view.xml',
                    'security/ir.model.access.csv'
                    ],
    'demo_xml' : [],
    'installable' : True,
    'active' : False
}