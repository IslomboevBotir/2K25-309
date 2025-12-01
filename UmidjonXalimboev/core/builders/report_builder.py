class ReportBuilder:
    def __init__(self):
        self.parts = []

    def add_header(self, text):
        self.parts.append('== ' + text + ' ==')
        return self

    def add_section(self, title, body):
        self.parts.append(f'-- {title} --')
        self.parts.append(body)
        return self

    def add_footer(self, text):
        self.parts.append('** ' + text + ' **')
        return self

    def build(self):
        return '\n'.join(self.parts)
