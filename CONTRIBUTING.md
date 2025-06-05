# Como Contribuir para o Analisador Inteligente de Documentos Jurídicos

Ficamos muito felizes com o seu interesse em contribuir para o "AI-Powered Legal Document Analyzer"! Suas contribuições são valiosas para o crescimento e aprimoramento deste projeto.

Este documento fornece um guia sobre como você pode participar.

## Como Reportar um Problema (Issue)

Se você encontrou um bug, tem uma sugestão de melhoria ou gostaria de propor uma nova funcionalidade, por favor, abra uma issue em nosso repositório no GitHub.

Ao abrir uma issue:
* **Seja claro e conciso:** Descreva o problema ou a sugestão de forma direta.
* **Forneça detalhes:** Inclua passos para reproduzir o bug (se aplicável), mensagens de erro e o comportamento esperado.
* **Use um título descritivo:** Isso ajuda a entender o problema rapidamente.

## Como Contribuir com Código

Se você deseja contribuir com código, siga os passos abaixo:

1.  **Faça um Fork do Repositório:** Clique no botão "Fork" no canto superior direito da página do projeto no GitHub. Isso criará uma cópia do repositório em sua conta.
2.  **Clone o Repositório Forkado:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/Analisador-IA-Juridico.git](https://github.com/SEU_USUARIO/Analisador-IA-Juridico.git)
    cd Analisador-IA-Juridico
    ```
    (Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub.)
3.  **Crie uma Nova Branch:** Crie uma branch para a sua feature ou correção de bug. Use nomes descritivos.
    ```bash
    git checkout -b feature/sua-nova-funcionalidade
    # ou
    git checkout -b fix/correcao-do-bug
    ```
4.  **Desenvolva sua Contribuição:** Faça suas alterações e adicione seu código. Certifique-se de seguir as diretrizes de codificação do projeto (se houver).
5.  **Teste suas Alterações:** Execute testes para garantir que suas alterações não quebraram funcionalidades existentes e que a nova funcionalidade está funcionando como esperado.
6.  **Comite suas Alterações:** Faça commits atômicos com mensagens claras e descritivas.
    ```bash
    git add .
    git commit -m "feat: Adiciona nova funcionalidade X"
    # ou
    git commit -m "fix: Corrige bug de Y"
    ```
    * **Mensagens de Commit:** Comece com `feat:` para novas funcionalidades, `fix:` para correção de bugs, `docs:` para alterações na documentação, etc.
7.  **Envie as Alterações para o seu Fork:**
    ```bash
    git push origin feature/sua-nova-funcionalidade
    ```
8.  **Abra um Pull Request (PR):**
    * Vá para o seu repositório forkado no GitHub.
    * Você verá um botão ou uma opção para "Compare & pull request" ou "New pull request". Clique nele.
    * Compare sua branch com a branch `main` do repositório original.
    * Forneça um título claro e uma descrição detalhada das suas alterações no PR. Inclua referências a quaisquer issues relacionadas (ex: `Closes #123`).
    * Aguarde a revisão do seu PR. Podemos pedir alterações ou fazer perguntas.

## Diretrizes de Código (Exemplo, adapte conforme necessário)

* Siga o estilo de código Python PEP 8.
* Adicione comentários onde necessário para explicar lógicas complexas.
* Documente novas funções e classes com docstrings.
* Crie testes para novas funcionalidades sempre que possível.

Agradecemos suas contribuições! Juntos podemos fazer deste projeto uma ferramenta incrível.
