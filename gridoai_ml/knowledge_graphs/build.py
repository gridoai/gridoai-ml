import typing as t
import openai

openai.api_type = "azure"
openai.api_base = "https://gridoai.openai.azure.com/"
openai.api_version = "2023-07-01-preview"

INSTRUCTIONS = """
Dado um prompt, extrapole quantas relações forem possíveis e forneça uma lista de triplas para construir um grafo de conhecimento.
Todas as triplas devem ter exatamente 3 elementos e devem estar no formato ("primeira entidade", "relacionamento", "segunda entidade")
"""

EXAMPLES = [
    {
        "role": "user",
        "content": "Alice é colega de quarto do Bob e ela está muito feliz.",
    },
    {
        "role": "assistant",
        "content": '[("Alice", "colega de quarto", "Bob"),("Alice", "está", "muito feliz")]',
    },
]


def text2kg(text: str, retries: int = 3) -> t.List[t.Tuple[str, str, str]]:
    print("Building a graph based on given text...")
    completion = openai.ChatCompletion.create(
        engine="API",
        model="gpt-35-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": INSTRUCTIONS,
            },
            *EXAMPLES,
            {
                "role": "user",
                "content": text,
            },
        ],
        temperature=0.2,
    )
    triples_str = completion.choices[0].message.content.strip()

    try:
        triples: t.List[t.Tuple[str, str, str]] = eval(triples_str)
        assert isinstance(triples, list)
        for triple in triples:
            assert isinstance(triple, tuple)
            assert len(triple) == 3
        return triples
    except:
        print(f"Bad output: {triples_str}")
        if retries == 1:
            raise Exception("Model cannot generate a list of triples")
        print("retring...")
        return text2kg(text, retries - 1)


kg = text2kg(
    """GridoAI
Respostas inteligentes baseadas
nos seus documentosHá muita informação
decentralizada em
sistemas
ProblemaDesafioNegativas
Mais tempo é gasto buscandoAcessar o conhecimentoTomada de decisão mal
e lendo a informação erradacorreto para responder ainformada ou lentidão nas
do que a corretapergunta que importaentregasHá muita informação
concentrada em
pessoas
ProblemaDesafioNegativas
Informações cruciais emDar conhecimento aFuncionários chave ficam
indivíduos, não timesquem precisasobrecarregadosAtendimento ao cliente
é caro, lento e ineficaz
ProblemaDesafioNegativas
Alto volume, demora eResolver problemas,Churn, perda de leads e
custo treinando eresponder dúvidas edeterioração da imagem
atualizando atendentesconverter leadsda empresaChatGPT aumenta
sua produtividade, mas...
+40%
em produtividade
+18%
em qualidadeMas ele não tem o seu
contexto
Ele não tem acesso
aos seus documentos
E se você quer que o ChatGPT faça uma
tarefa pra você, mas ele não tem as
informações necessárias?
Ele alucina
nas respostas
Ocasionalmente o ChatGPT inventa informações
que não existem. E se ele respondesse
embasado em fatos?GridoAI
Uma poderosa inteligência artificial
que usa seus documentos para
fornecer respostas precisas e
contextualizadas
Você traz seus dados
Nós os processamos
Você/seu cliente perguntaRespostas baseadas
em dados. Sempre.
Grido usa seus dados para fornecer
respostas precisas e inteligentes.
Chega de suposições, apenas
respostas baseadas em dados.Sistema de
permissões.
Adicione usuários à sua
organização e gerencie
seu permissionamento.Integre no seu site.
Atenda clientes muito mais rápido,
com mais precisão e de forma
muito mais barata.Envie seus arquivos.
Experimente carregar seus arquivos na
plataforma e questionar a Grido sobre eles.
Suportamos arquivos PDF, PPTX, DOCX e TXT de até 30MB.Integrações de dados
instantâneas.
Carregue arquivos ou conecte-se com
provedores populares como o Google Drive.
GitHubNotionGoogle Drive
ConfluenceWebsitesMicrosoft OneDrive
Integrações de dados
sob demanda.
Cada empresa tem sua necessidade na hora
de armazenar conhecimento. Encomende uma
integração customizada com o sistema que
você usa.Execute ações
automaticamente.
Grido pode executar ações anteriormente
definidas como notificar pessoas, acionar
entregas, agendar compromissos etc.Caso de uso
Atendimento ao cliente
010203
O público quer tirar dúvidas sobre o produtoOs clientes querem mais agilidade paraOs clientes necessitam de um suporte
da sua empresa.acessar informações em plataformaseficiente e rápido para resolver problemas
Grido responde rapidamente,
aumentando a taxa de
conversão de leads.complexas.técnicos.
Grido responde, melhorando a
experiência do cliente.Grido resolve, liberando a
equipe para tarefas complexas.Caso de uso
Assistente de TI
010203
Achar informações técnicas é difícil para aFuncionários têm dúvidas sobre as políticasA equipe de TI sobrecarregada com
equipe de TI.de segurança.solicitações de suporte técnico repetitivas e
Grido responde, poupando
buscas em documentações
técnicas.Grido responde, deixando a
equipe em conformidade com
as políticas.de baixo nível.
Grido responde, liberando a
equipe para tarefas complexas.Caso de uso
Assistente de RH
010203
A equipe de RH fica sobrecarregada comRH tem dificuldade em fornecer treinamentoDificuldade em analisar e comparar perfis de
dúvidas frequentes dos funcionários.para os funcionários.candidatos.
Grido responde, liberando RH
para tarefas estratégicas.Grido responde perguntas
sobre o conteúdo do
treinamento.Grido fornece análises e
comparações de candidatos
para boas contratações.Caso de uso
Assistente jurídico
010203
Extensos documentos jurídicos dificultam aA equipe jurídica tem dificuldade em rastrear eIntegração ineficiente de novos membros da
localização de informações.gerenciar contratos e acordos.equipe jurídica.
Grido extrai informações
específicas de grandes
volumes de documentos.Grido integra-se a sistemas
para auxiliar com rastreio e
gestão de contratos.Grido responde dúvidas sobre
procedimentos e políticas
internas, otimizando a
integração.Caso de uso
Assistente executivo
010203
Executivos têm dificuldade em acessar dadosExecutivos tem barreiras técnicas para obterDificuldade em acompanhar tendências e
críticos para decisões estratégicas.informações de diferentes departamentos.oportunidades de mercado.
Grido busca e analisa dados
em tempo real para insights
valiosos.Grido responde sobre
informações de todos os
departamentos, sem expertise
técnica.Grido analisa dados de
mercado e relatórios setoriais
para fornecer insights
estratégicos.Uma plataforma,
infinitas possibilidades.
Nossa meta é fornecer um oráculo
de conhecimento corporativo.
Assistente de TI
Assistente de RH
Assistente jurídico
Assistente executivoLinha do tempo de funcionalidades
Agora
Sistema de permissões
Permissões granulares
Membro e administrador
Google Drive
Integrações
Confluence
Ingestão de arquivos
PDF
PPTX
DOCX
Interações do bot
Interfaces de chat
Texto
Responder sobre documentos
Interface própria
Aúdio
Páginas WEB
Vídeo
Atualizar documentos
Whatsapp"""
)

print(kg)
