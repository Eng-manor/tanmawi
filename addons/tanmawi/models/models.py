# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tanmawi(models.Model):
    _name = 'tanmawi'
    _description = 'tanmawi'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'website.seo.metadata']

    name = fields.Char(string='الاسم', tracking=True)
    state = fields.Selection([ ('pending', 'Waiting Validation'), ('active', 'Active')], string='الحالة', default='pending', tracking=True)



class Projects(models.Model):
    _name = 'projects'
    _description = 'project'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'website.seo.metadata']

    name = fields.Char(string='Name', tracking=True)
    header = fields.Text(string='Header', tracking=True)
    icon = fields.Binary('Icon')
    project_points_ids = fields.One2many('project.points', 'project_id', string='Project Points')
    # state = fields.Selection([ ('pending', 'Waiting Validation'), ('active', 'Active')], string='الحالة', default='pending', tracking=True)


class ProjectPoints(models.Model):
    _name = "project.points"
    _description = "points"

    name = fields.Char('Point')
    has_parent = fields.Boolean("Has Parent")
    parent = fields.Many2one('project.points',"Parent")
    project_id = fields.Many2one('projects', string='Projects')



