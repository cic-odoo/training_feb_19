# -*- coding: utf-8 -*-
from odoo import http

# class ExtraFeatures(http.Controller):
#     @http.route('/extra_features/extra_features/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra_features/extra_features/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra_features.listing', {
#             'root': '/extra_features/extra_features',
#             'objects': http.request.env['extra_features.extra_features'].search([]),
#         })

#     @http.route('/extra_features/extra_features/objects/<model("extra_features.extra_features"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra_features.object', {
#             'object': obj
#         })