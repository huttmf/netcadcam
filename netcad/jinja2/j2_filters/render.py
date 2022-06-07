#  Copyright (c) 2021 Jeremy Schulman
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

from typing import Any

# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------

import jinja2


# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------


@jinja2.pass_context
def j2_render(ctx, obj: Any, render_target="render", **kwargs):
    from netcad.device import Device, DeviceInterface
    from netcad.device.device_interfaces import DeviceInterfaces

    if isinstance(obj, Device):
        ref_obj = obj
        call_meth_name = f"render_{render_target}"

    elif isinstance(obj, DeviceInterfaces):
        ref_obj = obj
        call_meth_name = "render"

    elif isinstance(obj, DeviceInterface):
        ref_obj = obj.device
        call_meth_name = f"render_interface_{render_target}"

    else:
        raise RuntimeError(f"Unexpected render object type: {type(obj)}")

    if call_meth := getattr(ref_obj, call_meth_name, None):
        return call_meth(ctx, **kwargs)

    raise RuntimeError(
        f"object {str(obj)} does not support redner method: {call_meth_name}"
    )
