# -*- coding: utf-8 -*-
from odoo import models, fields, api
import base64
import tempfile

class OrgChartEmployee(models.Model):
	_name = 'org.chart.employee'

	name = fields.Char("Org Chart Employee")

	@api.model
	def get_employee_data(self):
		company = self.env.user.company_id
		data = {
			'name': company.name,
			'title': company.country_id.name,
			'children': [],
			'office': "<img src='/logo.png' />",
		}
		employees = self.env['hr.employee'].search([('parent_id','=',False)])
		for employee in employees:
			data['children'].append(self.get_children(employee, 'middle-level'))

		return {'values': data}


	@api.model
	def get_children(self, emp, style=False):
		data = []
		emp_data = {'name': emp.name, 'title': self._get_position(emp), 'office': self._get_image(emp)}
		childrens = self.env['hr.employee'].search([('parent_id','=',emp.id)])
		for child in childrens:
			sub_child = self.env['hr.employee'].search([('parent_id','=',child.id)])
			next_style= self._get_style(style)
			if not sub_child:
				data.append({'name': child.name, 'title': self._get_position(child), 'className': next_style, 'office': self._get_image(child)})
			else:
				data.append(self.get_children(child, next_style))

		if childrens:
			emp_data['children'] = data
		if style:
			emp_data['className'] = style

		return emp_data


	def _get_style(self, last_style):
		if last_style == 'middle-level':
			return 'product-dept'
		if last_style == 'product-dept':
			return 'rd-dept'
		if last_style == 'rd-dept':
			return 'pipeline1'
		if last_style == 'pipeline1':
			return 'frontend1'

		return 'middle-level'

	def _get_image(self, emp):
		if emp.image:
			image_path = "/web/image/hr.employee/%s/image" %(emp.id)
			return '<img src=%s />' % (image_path)

		image_path = "/org_chart_employee/static/src/img/default_image.png"
		return '<img src=%s />' % (image_path)

	def _get_position(self, emp):
		if emp.sudo().job_id:
			return emp.sudo().job_id.name
		return ""
