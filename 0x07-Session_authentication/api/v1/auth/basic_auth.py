#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, List
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            str_bytes = base64.b64decode(base64_bytes)
            the_str = str_bytes.decode('utf-8')
            return the_str
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user_info = decoded_base64_authorization_header.split(":")
        user = user_info[0]
        password = user_info[1]
        return user, password
        # separator = decoded_base64_authorization_header.find(":")
        # user = decoded_base64_authorization_header[:separator]
        # pswd = decoded_base64_authorization_header[separator + 1:]
        # return user, pswd

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password.
        """
        if user_email is None:
            return None
        if type(user_email) is not str:
            return None
        if user_pwd is None:
            return None
        if type(user_pwd) is not str:
            return None
        try:
            user_info = User.search({"email": user_email})
        except Exception:
            return None
        if len(user_info) == 0:
            return None
        valid_psw = user_info[0].is_valid_password(user_pwd)
        if not valid_psw:
            return None
        return user_info[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request
        """
        try:
            header = self.authorization_header(request)
            base64 = self.extract_base64_authorization_header(header)
            decoded = self.decode_base64_authorization_header(base64)
            cred = self.extract_user_credentials(decoded)
            user = self.user_object_from_credentials(cred[0], cred[1])
            return user
        except Exception:
            return None
