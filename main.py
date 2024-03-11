from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from dataclasses import dataclass
from dotenv import load_dotenv
import glob, os, time
from tqdm import tqdm

load_dotenv()
llm = ChatOpenAI(
    temperature=0,
    model_name=os.getenv("MODEL_NAME"),
)


def resumir_texto(texto: str) -> str:
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(texto)

    return summary


def executar_programa(enderecos_pdf: list[str]) -> None:
    artigos = []
    for i in tqdm(enderecos_pdf):
        a = Artigo(i)

        artigos.append(a)

        with open(f"resumos/{a.titulo}.txt", "w") as f:
            f.write(
                f"""
                    TITULO:
                    
                    {a.titulo}
                    
                    TEXTO:
                    
                    {a.texto}
                    
                    
                    RESUMO:
                    
                    {a.resumo}
                    
                    """
            )


@dataclass
class Artigo:
    endereco: str
    titulo: str | None = None
    texto: str | None = None
    resumo: str | None = None

    def __post_init__(self) -> None:
        self.titulo = os.path.basename(self.endereco).replace(".pdf", "")
        loader = PyPDFLoader(self.endereco)
        self.texto = loader.load_and_split()
        self.resumo = resumir_texto(self.texto)


if __name__ == "__main__":
    enderecos_pdf = glob.glob("pdfs/*.pdf")

    executar_programa(enderecos_pdf)
