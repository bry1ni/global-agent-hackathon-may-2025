from agno.playground import Playground, serve_playground_app

from src.agents.sentivisor import sentivisor

app = Playground(
        agents=[sentivisor],
        teams=[],
    ).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)