# -*- coding: utf-8 -*-
{
	'name': "Organization Chart Employee",
	'summary': """Dynamic display of your Employee Hierarchy""",
	'description': """Dynamic display of your Employee Hierarchy""",
	'author': "SLife Organization, Amichia Fréjus Arnaud AKA",
	'category': 'Human Resources',
	'version': '1.0',
	'license': 'AGPL-3',
	'depends': ['hr'],
	'data': ['views/org_chart_views.xml'],
	'images': [
		'static/src/img/main_screenshot.png'
	],
	'qweb': [
        "static/src/xml/org_chart_employee.xml",
    ],
	'installable': True,
	'application': True,
	'auto_install': False,
}
