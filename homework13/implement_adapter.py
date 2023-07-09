"""Implement adapter patter from_txt_to_html
for example, we have a such structure in txt"""
from homework13.file_proxy_writer import TxtProxyWriter


class FromDataAdapter:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_writer = TxtProxyWriter('data_in_html.html', 'w')

    def convert_txt_to_html(self):
        with open(self.file_path) as file:
            lines = file.readlines()
        headers_txt = lines[0].replace('\n', '')
        user_data_txt = lines[1:]
        headers = headers_txt.split(',')
        data_user = [item.replace('\n', '').split(',') for item in user_data_txt]
        result = []
        for u_data in data_user:
            user_tuple = zip(headers, u_data)
            for u_element in list(user_tuple):
                result.append(f'<{u_element[0]}>{u_element[1]}</{u_element[0]}>')

        final_html_string = '\n'.join(result)
        self.file_writer.write_to_file(final_html_string)
