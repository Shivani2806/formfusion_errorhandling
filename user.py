from submission import SubmitFormRequest, SubmitFormResponse
from query import (
    QueryFormRequest,
    QueryFormResponse,
)
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

ORGANISATION_ADDRESS = "agent1qv7ztxd9cgc8g9jlyenkptw3t63g0h2pjmqaz4qu3q5jn37m5kkvj93d5js"

user = Agent(
    name="user",
    port=8000,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(user.wallet.address())

Form_query = QueryFormRequest(
    body="",

    title="Internship Session",

)

# print(type(QueryFormRequest.title))

@user.on_interval(period=5.0, messages=QueryFormRequest)
async def interval(ctx: Context):
    completed = ctx.storage.get("completed")

    if not completed:
        # if QueryFormRequest.body!="" and QueryFormRequest.title!="":
        #     if type(QueryFormRequest.body)=='string' and type(QueryFormRequest.title)=="string":
        #         await ctx.send(ORGANISATION_ADDRESS, Form_query)
        # else:
       # ctx.logger.info("ERROR:Either have not provided a field or may be its not in the correct format")

        await ctx.send(ORGANISATION_ADDRESS, Form_query)

if __name__ == "__main__":
    user.run()
