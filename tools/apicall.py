import time
import hashlib
import requests
import json

from .errors import ParamCheckError, AuthenticationError

class _ParamCheck:
    def __init__(self, check_params, params_format, params):
        self._checks_config = check_params
        try:
            params_format["dyn_url_param"]
        except KeyError:
            self._params_format = params_format["params"]
        else:
            self._params_format = params_format["dyn_url_param"] + params_format["params"]
        self._params = params
        self._errors = []

        self.do_the_checks()

    def do_the_checks(self):
        if self._checks_config == 'all' or self._checks_config == True:
            self._check_all()
        else:
            if "t" in self._checks_config:
                self._check_type()
            if "r" in self._checks_config:
                self._check_required()
            if "v" in self._checks_config:
                self._check_value()

    def _check_all(self):
        self._check_type()
        self._check_required()
        self._check_value()

    def _check_type(self):
        for param_format in self._params_format:
            if type(self._params[param_format[0]]) != param_format[1] and self._params[param_format[0]] is not None:
                self._errors.append((param_format[0],
                                    f"The parameter {param_format[0]} needs to be {str(param_format[1])}."))

    def _check_required(self):
        for param_format in self._params_format:
            if param_format[2] is True and self._params[param_format[0]] is None:
                self._errors.append((param_format[0],
                                    f"The parameter {param_format[0]} is required."))

    def _check_value(self):
        for param_format in self._params_format:
            if param_format[3] and self._params[param_format[0]] not in [*param_format[3], None]:
                self._errors.append((param_format[0],
                                    f"The parameter {param_format[0]} must be one of these values: {param_format[3]}."))

    def get_result(self):
        if self._errors:
            return list(error[1] for error in sorted(self._errors))
        else:
            return []


class APICall:

    _request_type = {
        "get": requests.get,
        "post": requests.post,
        "put": requests.put,
        "delete": requests.delete
    }

    def __init__(self, config, params_format, params):
        self._access_id = config['access_id']
        self._secret_key = config['secret_key']
        self._check_params = config['check_params']
        self._param_err_msg = config['param_err_msg']
        self._response_format = config['response_format']
        self._params_format = params_format
        self._params = params
        self._data = None

        self._errors = []
        self._header = None
        self._authorization = ''
        self._response_object = None
        self._http_status_code = None

        self._do_param_check()
        self._manage_errors()
        self._do_dynamic_url_check()
        self._do_auth_check()
        self._call_api()

    def _do_param_check(self):
        if self._check_params not in [False, None]:
            self._errors = _ParamCheck(self._check_params, self._params_format, self._params).get_result()

    def _manage_errors(self):
        if self._errors:
            if self._param_err_msg == 'exception':
                raise ParamCheckError(self._errors)
            elif self._param_err_msg == 'print':
                for error in self._errors:
                    print(error)

    def _do_dynamic_url_check(self):
        try:
            self._params_format["dyn_url_param"]
        except KeyError:
            pass
        else:
            self._params_format["url"] += str(self._params[self._params_format["dyn_url_param"][0][0]])

    def _do_auth_check(self):
        if self._params_format["authorization"]:
            if self._access_id and self._secret_key:
                self._params["access_id"] = self._access_id
                self._params["tonce"] = time.time_ns() // 1000000
                self._params = {k: self._params[k] for k in sorted(self._params.keys())}
                authorization_string = ""
                for param in self._params:
                    if self._params[param] is not None:
                        authorization_string += param + '=' + str(self._params[param]) + '&'
                authorization_string += "secret_key=" + self._secret_key
                self._authorization = hashlib.md5(authorization_string.encode('utf-8')).hexdigest().upper()
                self._header = {"authorization": self._authorization}
            else:
                raise AuthenticationError(self._params_format["endpoint"])

    def _call_api(self):
        if self._params_format["params_as_data"]:
            self._data = self._params
            self._params = None
        self._response_object = self._request_type[self._params_format["type"]](
            self._params_format["url"],
            params=self._params,
            data=json.dumps(self._data),
            headers=self._header
        )
        self._http_status_code = self._response_object.status_code

    def get_result(self):
        if self._response_format == 'json':
            return self._response_object.json()
        elif self._response_format == 'simplified':
            return self._response_object.json()["data"]

    def get_errors(self):
        return self._errors