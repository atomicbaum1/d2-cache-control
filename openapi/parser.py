"""OpenAPI parsing objects and methods.
Specification used: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md
"""

import re
# import yaml # TODO: YAML support
import requests


class Object:
    """Basic OpenApi object."""

    def __init__(self, object_type, extendable):
        """Initialize the object data.
        Args:
            object_type - name of the object (string) as defined in the OpenAPI specification.
            extendable - boolean value
        """
        # Data defined by the OpenAPI Specification
        self._accepted_required = ['REQUIRED', 'RECOMMENDED', 'OPTIONAL']
        self._primitive_data_types = {
            # Common Name: (type, format)
            'integer': ('integer', 'int32'),  # Signed 32 bits
            'long': ('integer', 'int64'),  # Signed 64 bits
            'float': ('number', 'float'),  #
            'double': ('number', 'double'),  #
            'string': ('string', None),  #
            'byte': ('string', 'byte'),  # Base64 encoded characters
            'binary': ('string', 'binary'),  # Any sequence of octets
            'boolean': ('boolean', None),  #
            'date': ('string', 'date'),  # As defined by full-date RFC3339
            'dateTime': ('string', 'date-time'),  # As defined by date-time RFC3339
            'password': ('string', 'password'),  # A hint to UIs to obscure input.
        }
        # Standard objects defined in the OpenAPI standard
        self._standard_objects = ['string', 'Info Object', 'Server Object', 'Paths Object', 'Components Object',
                                  'Security Requirement Object', 'Tag Object', 'External Documentation Object']
        self.object_type = object_type
        self.extendable = extendable

        self.field_list = []  # List of field names in this object
        self.field_type = {}  # A map of a field names to a list of types
        self.field_required = {}  # A map of field names to the required status
        self.field_data_type = {}  # A map of a list of field data types (scalar or list)

    # TODO: Return a list of types
    def _get_field_type(self, data):
        """Returns the field type name without the data type metadata.  That is '[Contact Object]' will be turned into
        'Contact Object''.

        Args:
            data - data type to get the type
            """
        array_pattern = re.compile(r'^\[(.+)\]$')
        match = array_pattern.match(data)

        def type_splitter(type_data):
            return [x.strip() for x in type_data.split('|')]

        if match is None:
            return type_splitter(data)
        return type_splitter(match.group(1))

    # TODO: Returns a list of types
    def _get_data_type(self, data):
        """Returns 'scalar' if the type is a scalar type, and returns 'list' if the type is an array or a list.
        Args:
            data - data type to get the type
            """
        array_pattern = re.compile(r'^\[.+\]$')
        if array_pattern.findall(data):
            return 'list'
        return 'scalar'

    def add_filed(self, field_name, field_type, field_required='OPTIONAL'):
        """Add an expected field type.  These are the allowed children.
        Args:
            field_name - Field name string
            field_type - Type of the object as a string
            field_required - REQUIRED, RECOMMENDED, or OPTIONAL status as a string
        Raises:
            Exception on unexpected input.
        """

        if field_name in self.field_list:
            raise Exception('"{name}" is already a field in this object.'.format(name=field_name))
        self.field_list.append(field_name)

        self.field_type[field_name] = self._get_field_type(field_type)

        if field_required not in self._accepted_required:
            raise Exception('"{required}" not in accepted list of required fields.'.format(required=field_required))
        self.field_required[field_name] = field_required

        self.field_data_type[field_name] = self._get_data_type(field_type)


class Schema:
    """OpenApi document schema."""

    def __init__(self):
        """Initialize the schema."""
        self.objects = []
        self._load_schema()

    def _add_object(self, object):
        """Add an object to the schema."""
        self.objects.append(object)

    def _load_schema(self):
        """Load the standard schema object definitions.

        Currently implemented objects:
            OpenAPI Object

        """

        # OpenAPI Object
        open_api_object = Object('OpenAPI Object', True)
        open_api_object.add_filed('openapi', 'string', 'REQUIRED')
        open_api_object.add_filed('info', 'Info Object', 'REQUIRED')
        open_api_object.add_filed('servers', '[Server Object]')
        open_api_object.add_filed('paths', 'Paths Object', 'REQUIRED')
        open_api_object.add_filed('components', 'Components Object')
        open_api_object.add_filed('security', '[Security Requirement Object]')
        open_api_object.add_filed('tags', '[Tag Object]')
        open_api_object.add_filed('externalDocs', 'External Documentation Object')
        self._add_object(open_api_object)

        # Info Object
        info_object = Object('Info Object', True)
        info_object.add_filed('title', 'string', 'REQUIRED')
        info_object.add_field('description', 'string')
        info_object.add_filed('termsOfService', 'string')
        info_object.add_filed('contact', 'Contact Object')
        info_object.add_filed('license', 'License Object')
        info_object.add_filed('version', 'string', 'REQUIRED')
        self._add_object(info_object)


class OpenApiObject:
    """OpenApi base object"""

    def __init__(self):
        self.json_object = None


    def _load_schema(self):
        """Load the dynamic schema rules"""


    def _load(self, json):
        """Load the object based on text."""
        # TODO: Support other types (only supports JSON)
        print(json['openapi'])


class OpenApiLoader:
    """OpenApi loader object for loading OpenApi media."""

    def __init__(self, url=''):
        self.url = url
        self.request = None

    def load(self):
        """Load the URL.
        Raises an exception if the status code is not 200.
        """
        self.request = requests.get(self.url)
        if self.request.status_code != 200:
            raise Exception('Bad status code when getting file.\nCode {status} Text: {text}'.format(
                            status=self.request.status_code, text=self.request.text))


if __name__ == '__main__': # TEST_URL = 'https://raw.githubusercontent.com/Bungie-net/api/master/openapi.json'
    s = Schema()
