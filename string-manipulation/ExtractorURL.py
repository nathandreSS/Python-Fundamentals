import re


class ExtractorURL:
    def __init__(self, url):
        self.url = self.sanitizes_url(url)
        self.__validate_url()
        self.base_url = self.__extract_base_url()
        self.params = self.__extract_params()

    def __str__(self):
        return f'URL: {self.url}\n' \
               f'Base_URL: {self.base_url}\n' \
               f'Params: {self.params}'

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def sanitizes_url(url):
        if type(url):
            return url.strip()

    @staticmethod
    def string_to_params(string_params):
        params = string_params.split('&')
        params_dict = {}
        for param in params:
            [key, value] = param.split('=')
            params_dict[key] = value

        return params_dict

    def __validate_url(self):
        if not self.url:
            raise ValueError("Invalid URL")

        pattern = re.compile("(http(s)?://)?(www.)?[a-z]*.com(.br)?/[a-z]")
        match = pattern.match(self.url)
        if not match:
            raise ValueError("Invalid URL")

    def __extract_base_url(self):
        question_mark_index = self.url.find('?')
        return self.url[:question_mark_index]

    def __extract_params(self):
        question_mark_index = self.url.find('?')
        if '?' == -1:
            return ''

        return self.string_to_params(self.url[question_mark_index+1:])


