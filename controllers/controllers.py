# -*- coding: utf-8 -*-
from odoo import http

# class Rhoesada(http.Controller):
#     @http.route('/rhoesada/rhoesada/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rhoesada/rhoesada/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rhoesada.listing', {
#             'root': '/rhoesada/rhoesada',
#             'objects': http.request.env['rhoesada.rhoesada'].search([]),
#         })

#     @http.route('/rhoesada/rhoesada/objects/<model("rhoesada.rhoesada"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rhoesada.object', {
#             'object': obj
#         })