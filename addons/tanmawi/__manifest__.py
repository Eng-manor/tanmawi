# -*- coding: utf-8 -*-
{
    'name': "Tanmawi",

    'summary': """ Tanmawi App By GRAV!TA """,

    'description': """ Long description about app by gravita-adv can change later """,

    'author': "GRAV!TA",
    'website': "https://gravita-adv.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','website','mail','board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
		'views/tree.xml',
		'views/kanban.xml',
		'views/form.xml',
		'views/qweb.xml',
		'views/search.xml',
		'views/activity.xml',
		'views/calendar.xml',
		'views/dashboard.xml',
		'views/pivot.xml',
		'views/graph.xml',
		'views/grid.xml',
		'views/snippit.xml',
		'views/setting.xml',
		'views/templates.xml',
        'views/template_home_page.xml',
        'views/template_about_page.xml',
        'views/template_projects_page.xml',
        'views/template_features_page.xml',
        'views/template_opportunities_page.xml',
        'views/template_ideas_page.xml',
        'views/template_project.xml',
        'views/template_projectstatics_page.xml',
        'views/template_contactus_page.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	'sequence': 1,
	'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
