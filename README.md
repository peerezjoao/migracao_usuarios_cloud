# Migração de Contas de Usuários On-Premises para a AWS.

## Introdução
<p>Migrar contas de usuários de um ambiente on-premises, ou C2C, para a AWS pode parecer uma tarefa árdua, especialmente quando envolve um grande número de usuários. Recentemente, enfrentei esse desafio ao precisar migrar diversas contas de usuários para a AWS, garantindo que cada um tivesse as permissões corretas e a autenticação por múltiplos fatores (MFA) ativada.</p> <p>Neste repositório, vou compartilhar como automatizei esse processo, as ferramentas que usei, e as lições que aprendi ao longo do caminho.</p>

## Contexto do Projeto
<p>O projeto exigia a migração de diversas contas de usuários on-premises para a AWS, com a aplicação de MFA para fortalecer a segurança. Devido ao volume de contas e à necessidade de precisão, era essencial evitar uma abordagem manual, que seria não só demorada, mas também propensa a erros.</p>

# Ferramentas Utilizadas
* Python

# Processo
<p>O primeiro passo, foi criar os grupos em que cada usuário estaria associado e realizar um De-Para na base de dados. Em cada grupo, foi atribuído uma política personalizada para que o usuário ative o MFA (Autenticação Multifator), isso garante que o acesso ao console seja liberado somente se o MFA estiver ativo. Além disso, após o primeiro login do usuário na console, ele é obrigado a escolher uma nova senha de acordo com o padrão que a organização estabeleceu. </p>
<p>Para utilizar os recursos do IAM, foi necessário criar um usuário programático e atribuir as politicas necessárias, sempre pensando no princípio do privilégio mínimo. 
Após isso, desenvolvi um script em python utilizando boto3, que faz a criação do usuário, depois, atribui uma senha a ele e adiciona-o ao seu grupo de destino.</p>
<p>Todos os códigos utilizados nesse projeto, estaram disponíveis neste repositório, assim como, alguns links que foram utilizados como base.</p>

# Conclusão
A automação não apenas acelerou o processo de migração, mas também, mitigou significativamente os erros, garantindo que cada usuário estivesse com as devidas permissões. A utilização do MFA, é uma prática recomendada

# Links relacionados
  * <a name="Autenticação multifator (MFA) para o IAM">https://aws.amazon.com/pt/iam/features/mfa/#:~:text=A%20autentica%C3%A7%C3%A3o%20multifator%20da%20AWS,nome%20de%20usu%C3%A1rio%20e%20senha.<a/>
  * <a name=“guia-mfa”><a/> Guia de Aplicação MFA
