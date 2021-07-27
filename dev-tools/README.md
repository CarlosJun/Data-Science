# Principais ferramentas para usar no terminal

## 1. Htop - Monitor de recursos e processos

O Htop é um avançado sistema interativo visualizador de processos. Escrito para Linux, o Htop mostra uma lista frequentemente atualizada de processos que rodam no computador, e utiliza-se de cores para facilitar a leitura de informações sobre o processador, swap, status da memória entre outros.

### Algumas vantagens e funcionalidades do Htop:
- Monitorar recursos visualmente: memória, processador e swap;
- O Htop suporta operações com o mouse;
- Matar processor sem precisar do PID (kill);
- Redefinir prioridade de processos (renice);
- No Htop você pode visualizar em listas horizontais e verticais todos os processos e suas linhas de comando, respectivamente.

### Exemplo de uso:
1.  Executar um um loop em Python que consome muita CPU
2.  Mostrar o uso de CPU em 100%
3.  Fazer um cópia e executar os dois códigos simultaneamente
4.  Mostrar o uso de duas CPUs em 100%
5.  Matar o processo em execução usando o comando Kill (F9) -> SIGTERM (Enter)
6.  Mudar o nível de prioridade do processo (F7 e F8)

## 2. Rsync - Sincronização de arquivos remotamente

### Sintaxe básica:

`rsync [modifcadores opcionais] [SRC] [DEST]`

### Principais modificadores:

Habilitar o modo arquivo:  
`-a, --archive`  
Mostrar o progresso do processo:  
`-v, --verbose`  
Comprimir os dados durante a transferência:  
`-z, --compress`  

### Mostrar o progresso dos arquivos transferidos:
`rsync -aP [SRC] [DEST]`

## Tmux - Multiplexador de terminal

Cheatsheet: https://tmuxcheatsheet.com/ 

### Principais comandos:

Iniciar uma nova sessão:  
`tmux`  
Iniciar uma nova sessão atribuindo um nome:  
`tmux new -s [nome]`  
Listar as sessões abertas:  
`tmux ls`  
Entrar na última sessão aberta:  
`tmux a`  
Entrar em uma sessão aberta especificando o nome:  
`tmux a -t [nome]`  
Finalizar uma sessão:  
`tmux kill-session -t [nome]`  

### Comandos internos:
Separar o painel horizontalmente:  
`crtl+b "`  
Separar o painel verticalmente:  
`crtl+b %`  
Navegar pelos os paineis:  
`crtl+b ↑`  
Sair da sessão sem desligar:  
`crtl+b d`  
Fechar um painel:  
`crtl+d`  
