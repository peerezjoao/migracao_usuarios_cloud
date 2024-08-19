# Migração de Contas de Usuários On-Premises para a AWS.

## Introdução
Migrar contas de usuários de um ambiente on-premises, ou C2C, para a AWS pode parecer uma tarefa árdua, especialmente quando envolve um grande número de usuários. Recentemente, enfrentei esse desafio ao precisar migrar aproximadamente 100 contas de usuários para a AWS, garantindo que cada um tivesse as permissões corretas e a autenticação por múltiplos fatores (MFA) ativada. Neste artigo, vou compartilhar como automatizei esse processo, as ferramentas que usei, e as lições que aprendi ao longo do caminho.

## Contexto do Projeto
O projeto exigia a migração de 100 contas de usuários on-premises para a AWS, com a aplicação de MFA para fortalecer a segurança. Devido ao volume de contas e à necessidade de precisão, era essencial evitar uma abordagem manual, que seria não só demorada, mas também propensa a erros.

# Ferramentas Utilizadas
* AWS CLI
* GitBash
* Shell Script
