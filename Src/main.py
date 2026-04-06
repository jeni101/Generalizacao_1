import os
import sys
import shutil
import re
import subprocess
import curses
import numpy as np
from pick import Picker
from colorama import init, Fore, Style

init(autoreset=True)

def limpar_tela():
    if os.name == 'nt':
        subprocess.run(['cls'], shell=True)
    else:
        subprocess.run(['clear'], shell=True)

def remover_cores(texto):
    return re.sub(r'\x1b\[[0-9;]*m', '', texto)

def centralizar(texto):
    try:
        largura = shutil.get_terminal_size().columns
    except:
        largura = 80
    texto_puro = remover_cores(texto)
    espacos = (largura - len(texto_puro)) // 2
    return " " * max(0, espacos) + texto

# --- Importações dos métodos ---
try:
    from minimos_quadrados.minimos_quadrados import perform_mq as minimos_quadrados
    from simpson13.simpson13_graph import perform_13 as simpson13
    from simpson38.simpson38_graph import perform38 as simpson38
    from trapezio.trapezio import plotar_trapezios as trapezio
except ImportError as e:
    print(f"Erro: Certifique-se de que as pastas possuem o arquivo __init__.py\n{e}")
    sys.exit(1)

ASCII_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⣶⣶⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⣰⣿⣿⠀⠀⢸⣿⣿⡉⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣦⠀⠙⢿⣿⣷⣄⠀⢠⣿⣿⠃⠀⠀⠈⣿⣿⣇⣀⣠⣤⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠟⠛⠋⠉⠉⠀⠀⠀⠙⢿⣿⣷⣼⣿⡟⠀⠀⠀⠀⢹⣿⣿⡿⠟⠛⠛⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⣀⣀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣧⣀⠀⠀⠀⠈⣿⣿⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣾⣿⠿⠿⠃⠀⠀⠀⠀⣾⣿⡟⠻⣿⣿⣦⡀⠀⠀⢹⣿⣿⣤⣴⣶⣶⣿⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣦⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠁⠀⠈⠻⣿⣿⣦⠀⠈⠿⠛⠛⠋⠉⠉
⠀⠀⠀⠀⣀⣀⣠⣤⣄⣀⠀⠀⠰⣿⣿⡿⠟⠛⠛⠉⠀⠀⠘⣿⣿⡟⢿⣿⣷⣄⠀⠹⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⣀⣠⣤⣤⣶⡄⢀⣿⡿⠏⠀⠀⠀⠀⠈⠉
⠀⢀⣴⣾⣿⠿⠿⠿⠿⠿⠄⠀⠀⣿⣿⣧⠀⠀⠀⢀⠀⠀⠀⢸⣿⣷⠈⠻⣿⣿⣦⡀⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠸⣿⡿⠿⠟⠛⠛⠉⠁
⣰⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣶⣾⣿⡿⠇⠀⠀⠈⣿⣿⡄⠀⠈⠻⣿⣿⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠇
⣿⣿⡏⠀⠀⢀⣤⣤⣶⣶⣷⡀⠀⠈⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⢻⣿⣧⠀⠀⠀⠘⠿⣿⣿⣿⠄
⢿⣿⣷⡀⠀⠀⠛⠋⠉⣿⣿⡇⠀⠀⢹⣿⣿⣀⣀⣀⣤⣤⡄⠀⠘⣿⣿⠄⠀⠀⠀⠀⠈⠉⠁
⠘⢿⣿⣷⣄⠀⠀⠀⢀⣹⣿⣿⡄⠀⠀⣿⣿⡿⠿⠿⠟⠛⠃
⠀⠈⠻⠿⣿⣿⣿⣿⣿⠿⠟⠋⠁
⠀⠀⠀⠀⠀⠀⠁
"""

def menu_com_curses(opcoes):
    """Exibe o menu com cores via curses e retorna (opcao, index)"""
    def _menu(stdscr):
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        # Define pares de cores
        curses.init_pair(1, curses.COLOR_CYAN, -1)     # Título / Art
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Item selecionado
        curses.init_pair(3, curses.COLOR_WHITE, -1)    # Item normal
        curses.init_pair(4, curses.COLOR_RED, -1)      # "Sair"
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_RED)   # "Sair" selecionado

        idx = 0
        while True:
            stdscr.clear()
            altura, largura = stdscr.getmaxyx()
            linha = 0

            # Imprime ASCII art em ciano
            for art_linha in ASCII_ART.split('\n'):
                if linha < altura - 1:
                    try:
                        stdscr.addstr(linha, 0, art_linha[:largura-1], curses.color_pair(1))
                    except curses.error:
                        pass
                linha += 1

            # Subtítulo
            subtitulo = "Use as setas para navegar e Enter para confirmar"
            x_sub = max(0, (largura - len(subtitulo)) // 2)
            if linha < altura - 1:
                try:
                    stdscr.addstr(linha, x_sub, subtitulo, curses.color_pair(1) | curses.A_DIM)
                except curses.error:
                    pass
            linha += 2

            # Opções
            for i, opcao in enumerate(opcoes):
                texto = f"  ➔  {opcao}  "
                x = max(0, (largura - len(texto)) // 2)
                eh_sair = (i == len(opcoes) - 1)

                if i == idx:
                    par = curses.color_pair(5) if eh_sair else curses.color_pair(2)
                    attr = par | curses.A_BOLD
                else:
                    par = curses.color_pair(4) if eh_sair else curses.color_pair(3)
                    attr = par

                if linha < altura - 1:
                    try:
                        stdscr.addstr(linha, x, texto[:largura-1], attr)
                    except curses.error:
                        pass
                linha += 1

            stdscr.refresh()

            tecla = stdscr.getch()
            if tecla == curses.KEY_UP:
                idx = (idx - 1) % len(opcoes)
            elif tecla == curses.KEY_DOWN:
                idx = (idx + 1) % len(opcoes)
            elif tecla in (curses.KEY_ENTER, ord('\n'), ord('\r')):
                return opcoes[idx], idx

    return curses.wrapper(_menu)


def main():
    AZUL     = Fore.BLUE + Style.BRIGHT
    CIANO    = Fore.CYAN + Style.BRIGHT
    VERMELHO = Fore.RED + Style.BRIGHT
    DIM      = Style.DIM
    RESET    = Style.RESET_ALL

    funcao_base = "np.sin(x)**2"
    a, b, n = 0, np.pi, 6

    opcoes = [
        '1. Simpson 1/3',
        '2. Simpson 3/8',
        '3. Trapezio Generalizado',
        '4. Minimos Quadrados',
        'Sair'
    ]

    while True:
        try:
            opcao_sel, index = menu_com_curses(opcoes)
        except Exception as e:
            print(f"Erro no menu: {e}")
            break

        if index == 4:
            limpar_tela()
            print("\n" * 5 + centralizar(f"{VERMELHO}Encerrando aplicacao...{RESET}"))
            break

        limpar_tela()
        print("\n" * 3)
        print(centralizar(f"{AZUL}>> EXECUTANDO: {opcoes[index].upper()}{RESET}"))
        print(centralizar(f"{DIM}Parametros: f(x)={funcao_base} | n={n}{RESET}"))
        print("\n" + centralizar(f"{DIM}-------------------------------------------{RESET}\n"))

        try:
            if index == 0: simpson13(funcao_base, a, b, n)
            elif index == 1: simpson38(funcao_base, a, b, n)
            elif index == 2: trapezio(funcao_base, a, b, n)
            elif index == 3: minimos_quadrados(funcao_base, a, b, n)

            print("\n" + centralizar(f"{CIANO}-------------------------------------------{RESET}"))
            input(centralizar("Pressione [ENTER] para voltar ao menu..."))
        except Exception as e:
            print("\n" + centralizar(f"{VERMELHO}ERRO: {e}{RESET}"))
            input("\n" + centralizar("Pressione Enter para retornar..."))

if __name__ == "__main__":
    main()