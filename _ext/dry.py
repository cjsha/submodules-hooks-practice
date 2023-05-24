"""Do Not Repeat Yourself"""

from __future__ import annotations

from sphinx.application import Sphinx
from sphinx.util import logging

import glob
import os
import shutil

logger = logging.getLogger(__name__)

__all__ = ()


def change_root_and_use_template(app, config):
    """

    :param_:
    :param config:
    :return:
    """

    # root_doc_dry = config.dry_dir + "/" + config.config_values['master_doc'][0].split('/')[-1]
    #
    # config.config_values['master_doc'] = (root_doc_dry,
    #                                       config.config_values['master_doc'][1],
    #                                       config.config_values['master_doc'][2])
    # print(config.config_values['master_doc'])

    # app.config_values['master_doc'] = (root_doc_dry,
    #                                       app.config_values['master_doc'][1],
    #                                       app.config_values['master_doc'][2])
    # print(app.config_values['master_doc'])

    pwd = os.path.dirname(__file__) + "/../"

    if not os.path.exists(pwd + "dry"):
        os.makedirs(pwd + "dry")

    shutil.copy(pwd + "source/index.rst", pwd + "dry/index.rst")
    shutil.copy(pwd + "source/404.rst", pwd + "dry/404.rst")

    for template_key in config.dry_json:
        if os.path.isdir(pwd + "source/" + template_key):
            for product_key in config.dry_json[template_key]:
                if os.path.exists(pwd + "dry/" + product_key):
                    shutil.rmtree(pwd + "dry/" + product_key)
                shutil.copytree(pwd + "source/" + template_key, pwd + "dry/" + product_key)
                for filename in glob.glob(pwd + "dry/" + product_key + "/**/*.rst", recursive=True):
                    with open(filename, "r") as file:
                        data = file.read()
                        for keyword_key in config.dry_json[template_key][product_key]:
                            data = data.replace(":dry:`" + keyword_key + "`",
                                                config.dry_json[template_key][product_key][keyword_key])
                    with open(filename, "w") as file:
                        file.write(data)
        else:
            print(template_key + " is not a folder")
    return


def setup(app: Sphinx) -> None:
    """

    :param app:
    :return:
    """
    app.connect('config-inited', change_root_and_use_template)
    app.add_config_value('dry_json', None, 'env')
    app.add_config_value('dry_dir', None, 'env')
    return
