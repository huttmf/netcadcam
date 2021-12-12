# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

from pathlib import Path

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------
import click

from netcad.logger import get_logger
from netcad.cli.common_opts import opt_design
from netcad.config import netcad_globals
from netcad.design_services import load_design

# Private Module Imports

from .cli_netcad_main import cli


@cli.command(name="diagram")
@opt_design(required=True)
@click.option(
    "--save",
    "save_file",
    required=True,
    help="filepath to save diagram file",
    type=click.Path(path_type=Path),
)
def cli_diagram(design: str, save_file: Path):
    """render design diagram"""

    log = get_logger()

    load_design(design_name=design)

    design_config = netcad_globals.g_netcad_designs[design]
    design_mod = design_config["module"]
    if not (diagram_func := getattr(design_mod, "diagram")):
        log.error(f'{design}: Missing "diagram" function in design.')
        return

    diagram_func(design, design_config, save_file=save_file)