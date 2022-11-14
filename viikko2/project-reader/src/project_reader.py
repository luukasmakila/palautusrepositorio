import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_content = toml.loads(content)
        print(toml_content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = toml_content["tool"]["poetry"]["name"]
        description = toml_content["tool"]["poetry"]["description"]
        dependencies = toml_content["tool"]["poetry"]["dependencies"]
        dev_dependencies = toml_content["tool"]["poetry"]["dev-dependencies"]
        return Project(name=name, description=description,
                       dependencies=dependencies,
                       dev_dependencies=dev_dependencies)
