from datetime import datetime
from io import BytesIO
from urllib.parse import urljoin

import numpy as np
import traitlets
from ipyleaflet import WMSLayer
from matplotlib import cm
from matplotlib.colors import Normalize
from notebook import notebookapp
from notebook.base.handlers import IPythonHandler
from notebook.utils import url_path_join
from PIL import Image

from dask_geomodeling.core import Block


class GeomodelingWMSHandler(IPythonHandler):
    """This Tornado request handler adds a WMS functionality for displaying
    dask-geomodeling results in a notebook

    See:
    https://jupyter-notebook.readthedocs.io/en/stable/extending/handlers.html
    """

    def get(self):
        block = Block.from_json(self.get_query_argument("layers"))
        style = self.get_query_argument("styles")
        vmin = float(self.get_query_argument("vmin"))
        vmax = float(self.get_query_argument("vmax"))
        format = self.get_query_argument("format")
        if format.lower() != "image/png":
            self.set_status(400)
            self.finish("Only image/png is supported")
            return
        srs = self.get_query_argument("srs")
        height = int(self.get_query_argument("height"))
        max_cell_size = float(self.get_query_argument("maxcellsize"))
        time_isoformat = self.get_query_argument("time")
        if time_isoformat:
            time = datetime.strptime(time_isoformat, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            time = None
        width = int(self.get_query_argument("width"))
        bbox = [float(x) for x in self.get_query_argument("bbox").split(",")]

        # overload protection
        cell_size_x = (bbox[2] - bbox[0]) / width
        cell_size_y = (bbox[3] - bbox[1]) / height
        if cell_size_x > max_cell_size or cell_size_y > max_cell_size:
            self.set_status(400)
            self.finish("Too large area requested")
            return

        # get cmap
        data = block.get_data(
            mode="vals",
            bbox=bbox,
            height=height,
            width=width,
            projection=srs,
            start=time,
        )
        masked = np.ma.masked_equal(data["values"][0], data["no_data_value"])
        stream = BytesIO()

        normalized = Normalize(vmin=vmin, vmax=vmax, clip=True)(masked)
        img = cm.get_cmap(style)(normalized)
        img[normalized.mask, 3] = 0.0
        img_uint8 = (img * 255).astype(np.uint8)
        Image.fromarray(img_uint8).save(stream, format="png")
        raw = stream.getvalue()

        self.set_header("Content-Length", len(raw))
        self.set_header("Content-Type", "image/png")
        self.set_header("Pragma", "no-cache")
        self.set_header(
            "Cache-Control",
            "no-store, "
            "no-cache=Set-Cookie, "
            "proxy-revalidate, "
            "max-age=0, "
            "post-check=0, pre-check=0",
        )
        self.set_header("Expires", "Wed, 2 Dec 1837 21:00:12 GMT")
        self.write(raw)
        self.finish()


class GeomodelingLayer(WMSLayer):
    """Visualize a dask_geomodeling.RasterBlock on a ipyleaflet Map.

    :param block: a dask_geomodeling.RasterBlock instance to visualize
    :param url: The url of the jupyter server (e.g. https://localhost:8888)
    :param style: a valid matplotlib colormap
    :param vmin: the minimum value (for the colormap)
    :param vmax: the maximum value (for the colormap)

    Notes
    -----
    To use this ipyleaflet extension, you have to include this plugin into your
    Jupyter Notebook server by calling::

    $ jupyter notebook --NotebookApp.nbserver_extensions="{'dask_geomodeling.ipyleaflet_plugin':True}"

    Or, by adding this setting to the config file in ~/.jupyter, which can be
    generated by calling::

    $ jupyter notebook --generate-config

    This plugin extends the Jupyter notebook server with a server that responds
    with PNG images for WMS requests generated by ipyleaflet.
    """

    format = traitlets.Unicode("image/png").tag(sync=True, o=True)
    maxcellsize = traitlets.Float(10.0).tag(sync=True, o=True)
    time = traitlets.Unicode("").tag(sync=True, o=True)
    vmin = traitlets.Float(0.0).tag(sync=True, o=True)
    vmax = traitlets.Float(1.0).tag(sync=True, o=True)

    def __init__(self, block, url=None, **kwargs):
        if url is None:
            # just get the first URL one
            url = next(notebookapp.list_running_servers())["url"]
        self.layers = block.to_json()
        super().__init__(url=urljoin(url, "wms"), **kwargs)


def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = ".*$"
    route_pattern = url_path_join(web_app.settings["base_url"], "/wms")
    web_app.add_handlers(host_pattern, [(route_pattern, GeomodelingWMSHandler)])
