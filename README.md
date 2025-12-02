# Prompts-Allconnect

Este repositório contém prompts, contextos e scripts utilizados pelos agentes de IA da Allconnect / Alltech Tools.

## Estrutura do Repositório

### Agentes e Contextos

- **Oncall/**: Contém o prompt para o agente **Edson**, especialista técnico do Canal OnCall.
    - `Prompt Oncall.md`: Prompt detalhado com instruções de atendimento e suporte técnico.
- **SDR/**: Contém o prompt para a agente **Renata** (SDR).
    - `SDR.md`: Prompt principal da Renata SDR.

### Arquivos na Raiz

- **Tasks.md**: Lista de tarefas e planejamento de prompts (ex: funções futuras).
- **TokenCount.py**: Script utilitário em Python para contagem de tokens.

## Utilização

Os arquivos `.md` servem como base de conhecimento e instruções de comportamento (System Prompts) para os respectivos agentes. O script `TokenCount.py` auxilia no monitoramento do tamanho dos prompts.
