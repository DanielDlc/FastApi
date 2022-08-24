from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/')
async def index():
    conteudo = """
         <center>
            <h1>FastAPI Web na <u>DlcTecnologia</u></h1>
            <span>
              Para mais cursos, visite meu linkedln clicando 
                <a href="https://www.linkedin.com/in/daniel-louro-costa-dev/" 
                target="_blank">aqui
                </a>.
            </span>
         </center>
    """

    return HTMLResponse(content=conteudo)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0",
                port=8000, log_level="info", reload=True)
