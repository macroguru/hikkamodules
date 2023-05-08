# requires: openai
# developer: @weeldag                                    
import openai
from .. import loader, utils
from telethon.tl.types import Message


@loader.tds
class FuckGPTMod(loader.Module):
    """Module for interacting with GPT different prompts"""
    strings = {
        "name": "FuckGPT",
        "wait": "<emoji document_id=5443038326535759644>💬</emoji><b> GPT is generating answer, wait</b>",
        "wait_aim": "<emoji document_id=5443038326535759644>💬</emoji><b> AIM is generating answer, wait</b>",
        "quest_k": "\n\n\n<emoji document_id=5260341314095947411>👀</emoji><b> Your question to Kelvin was:</b> {args}",
        "quest": "\n\n\n<emoji document_id=5260341314095947411>👀</emoji><b> Your question to GPT was:</b> {args}",
        "quest_aim": "\n\n\n<emoji document_id=5260341314095947411>👀</emoji><b> Your question to AIM was:</b> {args}",
        "args_err": "<emoji document_id=5260342697075416641>❌</emoji><b> You didn't ask a question GPT</b>",
        "conf_err": "<emoji document_id=5260342697075416641>❌</emoji><b> You didn't provide an api key. Specify it in .config FuckGPT</b>",
        "limit_err": "<emoji document_id=5260342697075416641>❌</emoji><b> The limit of requests has been reached. Repeat the question in 20 seconds</b>",
    }
    strings_ru = {
        "wait": "<emoji document_id=5443038326535759644>💬</emoji><b> GPT генерирует ответ, подождите</b>",
        "wait_aim": "<emoji document_id=5443038326535759644>💬</emoji><b> AIM генерирует ответ, подождите</b>",
        "quest_k": "\n\n\n<emoji document_id=5260341314095947411>👀</emoji><b> Ваш вопрос к Кельвину был:</b> {args}",
        "quest": "\n\n\n<emoji document_id=5260341314095947411>👀</emoji><b> Ваш вопрос GPT был:</b> {args}",
        "quest_aim": "\n\n\n<emoji document_id=5260341314095947411>👀</emoji><b> Ваш вопрос AIM был:</b> {args}",
        "args_err": "<emoji document_id=5260342697075416641>❌</emoji><b> Вы не задали вопрос GPT</b>",
        "conf_err": "<emoji document_id=5260342697075416641>❌</emoji><b> Вы не указали api key. Укажите его в .config FuckGPT</b>",
        "limit_err": "<emoji document_id=5260342697075416641>❌</emoji><b> Достигнут лимит запросов в минуту. Повторите вопрос через 20 секунд</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "api_key",
                None,
                lambda: "Api key for GPT",
                validator=loader.validators.Hidden(),
            ),
        )
        
        
    async def gptcmd(self, message: Message):
        """<question> - question for ChatGPT"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args_err"))
            return
        if self.config["api_key"] is None:
            await utils.answer(message, self.strings("conf_err"))
            return
        await utils.answer(message, self.strings("wait").format(args=args))
        openai.api_key = self.config["api_key"]
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": args}
                ]
            )
            response = completion.choices[0].message.content
            await utils.answer(message, f"<code>{response}</code>" + self.strings("quest").format(args=f"<code>{args}</code>"))
        except openai.error.RateLimitError:
            await utils.answer(message, self.strings("limit_err"))
       
    async def aimgptcmd(self, message: Message):
        """<question> - question for AIM"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args_err"))
            return
        if self.config["api_key"] is None:
            await utils.answer(message, self.strings("conf_err"))
            return
        await utils.answer(message, self.strings("wait_aim").format(args=args))
        openai.api_key = self.config["api_key"]
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": args}
                ]
            )
            response = completion.choices[0].message.content
            await utils.answer(message, f"<code>{response}</code>" + self.strings("quest").format(args=f"<code>{args}</code>"))
        except openai.error.RateLimitError:
            await utils.answer(message, self.strings("limit_err"))
        
    async def kgptcmd(self, message: Message):
        """<question> - question for Kelvin"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args_err"))
            return
        if self.config["api_key"] is None:
            await utils.answer(message, self.strings("conf_err"))
            return
        await utils.answer(message, self.strings("wait").format(args=args))
        openai.api_key = self.config["api_key"]
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": args}
                ]
            )
            response = completion.choices[0].message.content
            await utils.answer(message, f"<code>{response}</code>" + self.strings("quest").format(args=f"<code>{args}</code>"))
        except openai.error.RateLimitError:
            await utils.answer(message, self.strings("limit_err"))