from typing import Dict, Optional
from copy import deepcopy

from netcad.registry import Registry
from netcad.device import Device

from .design_service import DesignService


class Design(Registry, registry_name="designs"):
    """
    A `Design` instance is used to contain all conceptual elements related to a
    given design.  When a User invoke the netcad/netcam tools and refernces a
    design by name, it is a Design instance that is used to contain all aspects
    of that design.

    Attributes
    ----------
    services: dict
    devices: dict
    ipams: dict
    """

    def __init__(self, name: str, config: Optional[Dict] = None):
        # Register this design by designer designated name.  The name generally
        # comes from the name as defined in the netcad configuration file.

        self.registry_add(name=name, obj=self)

        # The config that originated from the netcad configuration file for this
        # specific design.

        self.config = deepcopy(config or {})

        # Caller designated named design services.  For example a designer could
        # call the VlanDesignService "vlans" or "my_vlans". The netcad system
        # does not hardcode any  speific names and leaves those decisions to the
        # designer.

        self.services: Dict[str, DesignService] = dict()

        self.devices: Dict[str, Device] = dict()

        self.ipams = dict()