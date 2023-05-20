# -*- coding: utf-8 -*-
# Hello Iam Manars
from odoo import http
import json
import time
from datetime import datetime, date , timedelta
from dateutil import parser
from collections import Counter
from itertools import groupby
import base64
from io import BytesIO
import json
import lxml
import requests
import logging
import werkzeug.exceptions
import werkzeug.urls
import werkzeug.wrappers
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.website_profile.controllers.main import WebsiteProfile
from odoo.addons.portal.controllers.portal import _build_url_w_params
from odoo.http import request

class Tanmawi(http.Controller):
    
    # Rout FOR Home Pgae "/"
    @http.route('/', auth='public')
    def index(self, **kw):
        value={}
        
        return request.render("tanmawi.home_page",value)

    @http.route('/about', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def about_control(self,**kw):
        return request.render("tanmawi.about_page")
        

    @http.route('/projects', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def projects_control(self,**kw):
        return request.render("tanmawi.projects_page")

    @http.route('/projects/<int:projectid>', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def project_control(self, projectid, **kw):
        value={}
        value['projectid'] = request.env['projects'].sudo().browse(projectid)
        return request.render("tanmawi.project_view", value)     

    @http.route('/features', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def advantage_compete_control(self,**kw):
        
        return request.render("tanmawi.features_page") 
        

    
    @http.route('/opportunities', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def opportunities_control(self,**kw):
        
        return request.render("tanmawi.opportunities_page")     
             
            

    @http.route('/ideas', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def ideas_control(self,**kw):
        return request.render("tanmawi.ideas_page")    

    @http.route('/projectstatics', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def projectstatics_control(self,**kw):
        return request.render("tanmawi.projectstatics_page")   
           

    @http.route('/supports/<int:supportid>', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def supports_control(self, supportid, **kw):
        return f"Hello, {supportid}"
        
    @http.route('/mediacenter/<int:mediacenterid>', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def mediacenter_control(self, mediacenterid, **kw):
        return f"Hello, {mediacenterid}"    

    @http.route('/contactus', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def contactus_control(self,**kw):
        return request.render("tanmawi.contactus_page")   
