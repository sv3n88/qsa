# coding: utf8

import click
from flask import Flask
from pathlib import Path

from qsa.config import Config
from qsa.api.projects import projects
from qsa.api.symbology import symbology


class QSA:
    def __init__(self, cfg):
        self.app = Flask(__name__)
        self.app.config["CONFIG"] = Config(cfg)
        self.app.register_blueprint(projects, url_prefix="/api/projects")
        self.app.register_blueprint(symbology, url_prefix="/api/symbology")

    def run(self):
        self.app.run(host="0.0.0.0")


@click.command()
@click.argument("cfg")
def run(cfg):
    QSA(Path(cfg)).run()