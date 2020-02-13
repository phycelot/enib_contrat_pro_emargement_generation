# -*-coding:utf8-*-

import copy
import http.cookiejar
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup


class EdtConnexion(object):
    def __init__(self, login, password, edt_url, proxy_enib=False, proxy_data=('https://proxy.enib.fr', 3128)):
        """ Setting up boring stuff """
        self.login = login
        self.password = password

        self.edt_url = edt_url

        self.login_data = None

        self.selects_dict = {}

        self.post_input = {
            'username': self.login,
            'password': self.password,
        }

        self.cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPRedirectHandler(),
            urllib.request.HTTPHandler(debuglevel=0),
            urllib.request.HTTPSHandler(debuglevel=0),
            urllib.request.HTTPCookieProcessor(self.cj)
        )

        # Add enib proxy
        if proxy_enib:
            self.opener.add_handler(
                urllib.request.ProxyHandler(
                    {'https': '{}:{}'.format(*proxy_data)}
                )
            )

        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                            'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

    def do_login(self):
        """
        Setting cookies and getting hidden inputs
        Populating cookie jar
        Login with username, password, cookies and hidden inputs
        """
        # Connecting to CAS
        try:
            response = self.opener.open("https://cas.enib.fr/login?service={}".format(
                urllib.parse.quote_plus(self.edt_url)))
        except urllib.error.URLError:
            return False

        try:
            # Parsing response
            res = response.read().decode(response.headers.get_content_charset())

            # Using beautifulsoup to extract hidden inputs

            soup = BeautifulSoup(res, 'html.parser')

            form = soup.find('form', {"id": "fm1"})

            inputs = form.find_all_next('input')

            # Parsing xml, populating self.post_input with every hidden input
            # except username, password, submit & reset

            for inp in inputs:
                if inp['name'] not in \
                        ("username", "password", "submit", "reset"):
                    self.post_input[inp['name']] = inp["value"]

            # With all new data, try to login

            self.login_data = urllib.parse.urlencode(self.post_input).encode("utf-8")
            self.opener.open("https://cas.enib.fr/login?service={}".format(
                urllib.parse.quote_plus(self.edt_url)), self.login_data)

            return True

        except:
            return False

    def get_groups(self):
        """

        :return:
        """

        try:
            response = self.opener.open(self.edt_url)
        except urllib.error.URLError:
            return None

        soup = BeautifulSoup(response, "html.parser")

        selects = soup.find("select", {"id": "student_grouping_id"})

        groups = selects.find_all_next("option")

        groups_dict = {}

        for group in groups:
            groups_dict[group.text] = group["value"]

        return groups_dict

    def get_students(self):
        """

        :return:
        """

        try:
            response = self.opener.open(self.edt_url)
        except urllib.error.URLError:
            return None

        soup = BeautifulSoup(response, "html.parser")

        selects = soup.find("select", {"id": "student_id"})

        students = selects.find_all_next("option")

        students_dict = {}

        for student in students:
            students_dict[student.text] = student["value"]

        return students_dict

    def rebuild_form_cache(self):
        """

        :return:
        """
        try:
            response = self.opener.open(self.edt_url)
        except urllib.error.URLError:
            return None

        soup = BeautifulSoup(response, "html.parser")
        form = soup.find("form", {"id": "selectGroupForm"})
        if form is None:
            raise ValueError('rebuild_form_cache error, form can\'t be None, check your login/password')
        selects = form.find_all_next("select")

        selects_dict = {}
        for select in selects:
            values = {}
            for option in select.find_all("option"):
                # inverted : key is week, value is option["value"]
                values[option.text.strip()] = option["value"]
            selects_dict[select["name"]] = copy.copy(values)

        self.selects_dict = selects_dict

    def get_group_edt(self, group_value, week):
        v_week = self.selects_dict["from_week_custom_id"][str(week)]
        s_dict = copy.copy(self.selects_dict)
        s_dict["from_week_custom_id"] = v_week
        s_dict["to_week_custom_id"] = v_week
        s_dict["student_id"] = "0"
        s_dict["student_grouping_id"] = group_value
        data = urllib.parse.urlencode(s_dict).encode("utf-8")

        try:
            response = self.opener.open(self.edt_url, data)
        except urllib.error.URLError:
            return None
        return response.read().decode(response.headers.get_content_charset())

    def get_student_edt(self, student_value, week):
        v_week = self.selects_dict["from_week_custom_id"][str(week)]
        s_dict = copy.copy(self.selects_dict)
        s_dict["from_week_custom_id"] = v_week
        s_dict["to_week_custom_id"] = v_week
        s_dict["student_id"] = student_value
        s_dict["student_grouping_id"] = "0"
        data = urllib.parse.urlencode(s_dict).encode("utf-8")

        try:
            response = self.opener.open(self.edt_url, data)
        except urllib.error.URLError:
            return None
        return response.read().decode(response.headers.get_content_charset())
