# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

from typing import AnyStr, Iterable, KeysView

# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------

from httpx import Response

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from netcad.config import netcad_globals
from netcad.igather import as_completed
from netcad.logger import get_logger
from netcad.origin import OriginDeviceType, OriginDeviceTypeInterfaceSpec

from .devices import NetboxDevices
from .netbox_origin import NetboxOrigin

# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------

__all__ = ["NetboxOriginDeviceType"]


# -----------------------------------------------------------------------------
#
#                                 CODE BEGINS
#
# -----------------------------------------------------------------------------


class NetboxOriginDeviceType(OriginDeviceType, NetboxOrigin):
    def __init__(self, *vargs, **kwargs):
        super(NetboxOriginDeviceType, self).__init__(*vargs, **kwargs)
        self._if_name2obj = {
            iface["name"]: iface for iface in self.origin_spec["interfaces"]
        }

    # -------------------------------------------------------------------------
    #
    #                OriginDeviceType ABC Implementations
    #
    # -------------------------------------------------------------------------

    @property
    def product_model(self) -> str:
        return self.origin_spec["device_type"]["model"]

    @property
    def interface_names(self) -> KeysView:
        return self._if_name2obj.keys()

    def get_interface(self, if_name: str) -> OriginDeviceTypeInterfaceSpec:
        if_obj = self._if_name2obj[if_name]
        return OriginDeviceTypeInterfaceSpec(
            if_name=if_name,
            if_type=if_obj["type"]["value"],
            if_type_label=if_obj["type"]["label"],
        )

    # -------------------------------------------------------------------------
    #
    #                     OriginDeviceType Class Methods
    #
    # -------------------------------------------------------------------------

    @classmethod
    async def get(cls, product_models: Iterable[AnyStr]):
        """
        This function is used to fetch the specified device-types given the list
        of provided `product_models`.  Each of these device-type definitons will
        be stored in the Userss cache-directory as:

        $NETCAD_CACHEDIR/device-types/<porduct-modulel>.json

        Parameters
        ----------
        product_models:
            expected Sequences of strings used for the purpose of fetching the
            device-type definitions from the origin.
        """
        log = get_logger()
        dt_dir = netcad_globals.g_netcad_cache_dir.joinpath("device-types")
        dt_dir.mkdir(exist_ok=True)

        nb: NetboxDevices
        async with NetboxDevices() as nb:
            tasks = {
                nb.fetch_device_template(model=model): model for model in product_models
            }

            task_results: Response

            async for orig_coro, model_payload in as_completed(tasks):
                model = tasks[orig_coro]

                if not model_payload:
                    log.error(f"Execpted device-type {model} not found in Netbox")
                    continue

                model_payload["netcad.origin"] = cls.origin_name
                log.info(f"Saving {cls.origin_name} device-type: {model}")

                o_dt = cls(origin_spec=model_payload)
                await o_dt.save()