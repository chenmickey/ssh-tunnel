from app import create_app
from app.utils.autossh import AutoSsh
from app.utils.msg import Msg

app = create_app()
__dict__ = {app, AutoSsh, Msg}
