# developer: @weeldag

import logging
from .. import loader

logger = logging.getLogger(__name__)

@loader.tds
class TurnOffMod(loader.Module):
    """Module for turning off current Hikka session"""

    strings = {"name": "Simple logout mod"}

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client

    @loader.unrestricted
    async def logoutcmd(self, message):
        """- logout"""
        logger.info("Выхожу...")
        await self.client(functions.auth.ResetAuthorizationsRequest())
        await self.client.disconnect()