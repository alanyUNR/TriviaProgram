import asyncio
from copilot import CopilotClient
from copilot.session import PermissionHandler

def promptBuilder(topic) -> str:
    prompt: str = 'return a markdown document with 10 multiple choice trivia questions on ' + topic
    return prompt

def quizFixerPrompt(quizPath):
    prompt: str = 'return a new markdown document based on the file at '+quizPath+' with a template matching RobertPQuestions.md; keep the content the same'
    return prompt

async def queryer(prompt: str) -> str:
    print('starting Copilot SDK client...')
    client = CopilotClient()
    await client.start()
    session = await client.create_session(
        on_permission_request=PermissionHandler.approve_all,
        model="auto"
    )
    response = await session.send_and_wait(prompt)
    content: str = response.data.content
    await client.stop() 
    print('SDK client closed.')
    return content

# response: str = asyncio.run(queryer(promptBuilder('Reno Fun Facts')))
# with open(r'triviaProgram\TriviaProgram\renoQuestions.md', "w", encoding = 'utf-8') as file:
#     file.write(str(response))

response = asyncio.run(queryer(quizFixerPrompt('renoQuestions.md')))
with open(r'triviaProgram\TriviaProgram\renoQuestionsFixed.md', "w", encoding = 'utf-8') as file:
    file.write(str(response))
