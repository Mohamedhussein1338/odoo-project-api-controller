from odoo import http
from odoo.http import request
import json
from odoo.exceptions import ValidationError
import requests
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class ProjectApiController(http.Controller):

    @http.route('/create_project', type='http', auth='public', methods=['POST'], csrf=False)
    def create_project(self, **post):

        # Extract data from the request
        data = json.loads(request.httprequest.data)


        # Extract individual fields from the data
        name = data.get('name')
        description = data.get('description')
        postcode = data.get('postcode')
        date_availability = data.get('date_availability')

        # Log the received data
        _logger.info("Received data: Name=%s, Description=%s, Postcode=%s, Date Availability=%s", name, description,
                     postcode, date_availability)

        # Create a new record in the 'project.api' model
        project_obj = request.env['project.api']
        try:
            new_record = project_obj.create({
                'name': name,
                'description': description,
                'postcode': postcode,
                'date_availability': date_availability
            })

            return "Record created successfully with ID: %s" % new_record.id
        except ValidationError as e:
            return "Error: %s" % e

