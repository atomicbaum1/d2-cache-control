"""OpenAPI python file generator
Currently only supports Destiny 2."""

import os
import json
from collections import defaultdict
import requests
from openapi.lib import py_case_convert


OPEN_API_DOCUMENT_STR = """
\"\"\"OpenAPI {module} auto-gen API.
Copyright Notice:
   (c) 2017 Matthew A Baum
   atomicbaum1@gmail.com
   matt@baum.network
\"\"\"
#TODO: Make this file follow PEP 8 rules
import openapi.web_api
import openapi.oauth_client

{class_defs}
"""

CLASS_DEF_STR = """
class {class_name}Endpoint:
    \"\"\"Defines the endpoint for the {class_name} tag.\"\"\"
    def __init__(self, session):
        \"\"\"Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          \"\"\"
        self.session = session
        self.servers = {class_servers}
"""

# TODO: Add URI string and other useful info to the docstring
FUNCTION_DEF_STR = """
    def {function_name}:
        \"\"\"Defines the endpoint for the {function_name} tag.\"\"\"
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{{base}}{{request_url}}".format(base=self.servers[0], 
                                                                 request_url=F{request_url}))
"""


# TODO: This should be more generic when you know more
def get_class_method_map(openapi_map):
    """Generates Bungie endpoint data
    Args:
        openapi_map - map of the OpenAPI data
    Returns:
        Map of endpoints functions
    """

    # Build up the path indexes
    paths = [path for path in openapi_map['paths']]

    def get_params(path):
        """Gets the parameters from the path.
        Returns:
           String containing a function argument list (tuple looking string)
        """
        prefix = ''
        if 'get' in path:
            params = path['get']['parameters']
            prefix = '_get'
        elif 'post' in path:
            params = path['post']['parameters']
            prefix = '_post'
        else:
            raise Exception('Unknown type - not get or post')

        if len(params) == 0:
            return '(self)'
        if len(params) == 1:
            return '(self, {param})'.format(param=params[0]['name'])

        param_str = '(self, '
        for arg in params[:-1]:
            param_str += arg['name'] + ', '
        param_str += '{param})'.format(param=params[-1]['name'])
        return prefix + param_str

    # Get the class.method.(params) format the Bungie uses in the 'Summary' field
    class_method_format_list = ['{summary}:{params}.{path}'.format(
        summary=openapi_map['paths'][path]['summary'],
        params=get_params(openapi_map['paths'][path]),
        path=path) for path in paths]

    # Generate the information
    class_name_to_method_attribute_map_list = defaultdict(list)
    for cmf in class_method_format_list:
        class_name, method, path = cmf.split('.')
        method_name, method_params = method.split(':')
        py_fun_name = py_case_convert(method_name)
        py_fun_name += method_params
        method_attribute_map = defaultdict(str)
        method_attribute_map['method_type'] = 'autogen' # autogen type for future use
        method_attribute_map['function_name'] = py_fun_name
        method_attribute_map['path'] = '"{path}"'.format(path=path)
        class_name_to_method_attribute_map_list[class_name].append(method_attribute_map)

    return class_name_to_method_attribute_map_list


def generate_endpoint_method(endpoint_path_map, openapi_map):
    """Generate the function definition for the path map provided.
    Args:
        endpoint_path_map - openapi endpoint path map
        openapi_map - openapi map
    """
    # Focus only on what you need right now - weapons and armor and storage locations
    return f"""def {function_name}:
        \"\"\"Defines the endpoint for the {function_name} tag.\"\"\"
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{{base}}{{request_url}}".format(base=self.servers[0], 
                                                                     request_url=F{request_url}))"""


def generate_endpoint_file(openapi_map):
    """Generates the endpoint file for the openapi map provided.
    Args:
        openapi_map - OpenAPI map generated from openapi.json or openapi.yaml file
    Returns:
        String containting the class list
    """
    output_str = ''
    class_method_map = get_class_method_map(openapi_map)
    # Get the servers
    servers = [server['url'] for server in openapi_map['servers']]
    for class_name in class_method_map:
        output_str += CLASS_DEF_STR.format(class_name=class_name, class_servers=servers)
        for method_attribute_map in class_method_map[class_name]:
            output_str += FUNCTION_DEF_STR.format(function_name=method_attribute_map['function_name'],
                                                  function_params=method_attribute_map['function_params'],
                                                  request_url=method_attribute_map['path'])

    ret_str = OPEN_API_DOCUMENT_STR.format(module=openapi_map['info']['title'], class_defs=output_str)

    return ret_str


def load_openapi(resource):
    """Load the URL to the openapi resource.
    Raises an exception if the status code is not 200.
    Args:
        resource - URL of the resource
    Raises:
        Exception on bad file download or bad file type.
    """
    response = requests.get(resource)
    if response.status_code != 200:
        raise Exception('Bad status code when getting file.\nCode {status} Text: {text}'.format(
                        status=response.status_code, text=response.text))

    # https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#documentStructure
    # It is RECOMMENDED that the root OpenAPI document be named: openapi.json or openapi.yaml.
    # TODO: add logic so it is really recommended and not mandatory
    _, extension = os.path.splitext(resource)

    if extension == '.json':
        retobj = json.loads(response.content)
        return retobj

    raise Exception('{extension} type not yet supported.'.format(extension=extension))


if __name__ == '__main__':
    TEST_REMOTE = 'https://raw.githubusercontent.com/Bungie-net/api/master/openapi.json'
    bungie_map = load_openapi(TEST_REMOTE)
    output = generate_endpoint_file(bungie_map)
    print(output)

    with open("/tmp/autogen.py", "w") as text_file:
        print(output, file=text_file)
