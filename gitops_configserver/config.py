from os import getenv, path
import logging
import logging.config
import yaml


def file_exists(fname):
    return path.isfile(fname)


def setup_logger():
    if file_exists(Config.LOGGER_CONFIG_FILE):
        with open(Config.LOGGER_CONFIG_FILE, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        if not path.isdir("logs"):
            os.makedirs("logs")
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename=datetime.now().strftime("logs/logs_%Y_%m_%d_%H_%M.log"),
            filemode="w",
        )
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(name)-12s: %(levelname)-8s %(message)s"
        )
        console.setFormatter(formatter)
        logging.getLogger("").addHandler(console)
    logger = logging.getLogger(__name__)
    logger.info("Started")


class Config:
    LOGS_VERBOSE = True

    LOGGER_CONFIG_FILE = getenv(
        "GITOPS_CONFIGSERVER__LOGGER_CONFIG_FILE",
        path.join("resources", "logger.yaml"),
    )
    CONFIG_DIR = getenv("GITOPS_CONFIGSERVER__CONFIG_DIR")
    TARGET_DIR = getenv("GITOPS_CONFIGSERVER__TARGET_DIR", "target")

    HOST = getenv("GITOPS_CONFIGSERVER__HOST", "0.0.0.0")
    PORT = getenv("GITOPS_CONFIGSERVER__PORT", "8002")
