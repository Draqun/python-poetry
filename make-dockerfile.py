import argparse
import logging

import jinja2


def main(python: str, poetry: str, suffix: str | None) -> None:
    logging.info(f"Start building Dockerfile for python {python} and poetry {poetry}.")
    if suffix == "":
        suffix = None
    if suffix:
        logging.info(f"Using base image 'python:{python}{suffix}'!")
    else:
        logging.info(f"Using base image 'python:{python}'!")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    logging.debug("Loading template file.")
    template = env.get_template('Dockerfile.jinja')
    logging.debug("Rendering Dockerfile.")
    with open("Dockerfile", "wt") as file_handler:
        file_handler.write(template.render(python=python, poetry=poetry, suffix=suffix))
    logging.info(f"Dockerfile rendered.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--python")
    parser.add_argument("--poetry")
    parser.add_argument("--suffix")
    args = parser.parse_args()
    main(args.python, args.poetry, args.suffix)
