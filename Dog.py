# ===================================
# name: Dod
# meta developer: @weeldag
# requires: PIL requests io
# ===================================
import io
import requests

from PIL import Image
from .. import loader


@loader.tds
class DogModule(loader.Module):
    """Отпраляет случайно фото пёсика"""

    strings = {"name": "Dog"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.owner
    async def dogcmd(self, message):
        """- отправляет фото пёсика"""
        url = "https://api.thedogapi.com/v1/images/search"
        response = requests.get(url)
        if response.status_code == 200:
            img_url = response.json()[0]["url"]
            response = requests.get(img_url)
            img = Image.open(io.BytesIO(response.content))

            if img.mode == "P":
                img = img.convert("RGB")
            output = io.BytesIO()
            img.save(output, format="JPEG")
            output.seek(0)

            edited_message = await self.client.edit_message(message.to_id, message.id, "<emoji document_id=5341624476410846951>🐩</emoji><b> Ищем собачку...</b>")
            await self.client.send_file(message.to_id, output)

            await self.client.delete_messages(edited_message.chat_id, edited_message.id)