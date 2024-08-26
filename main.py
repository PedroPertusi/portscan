import socket
import tkinter as tk

def ler_portas_para_dict(caminho_arquivo):
    dicionario_portas = {}
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Dividir a linha em partes e remover espaços em branco
            partes = linha.strip().split(maxsplit=2)
            if len(partes) == 3:
                intervalo_porta, protocolo, nome_protocolo = partes

                # Verificar se o intervalo de portas contém um "-"
                if '-' in intervalo_porta:
                    inicio, fim = intervalo_porta.split('-')
                    for porta in range(int(inicio), int(fim) + 1):
                        dicionario_portas[porta] = f"{protocolo} {nome_protocolo}"
                else:
                    dicionario_portas[int(intervalo_porta)] = f"{protocolo} {nome_protocolo}"
    return dicionario_portas


def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()

def start_scan():
    host = entry_host.get()
    if not host:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Host inválido")
        return

    port_range = entry_ports.get().split('-')
    if len(port_range) != 2 or len(port_range) != 1: 
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Intervalo de portas inválido")
    start_port = int(port_range[0])
    if len(port_range) == 1:
        end_port = start_port
    else:
        end_port = int(port_range[1])
    results = []
    
    for port in range(start_port, end_port + 1):
        service = well_known_ports.get(port, "Serviço desconhecido")
        if scan_port(host, port):
            results.append(f"Porta {port} está aberta - ({service})")
        else:
            results.append(f"Port {port} está fechada - ({service})")
    
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, "\n".join(results))

def about():
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, 
        "Port Scan\n\n"
        "Desenvolvido por: Pedro Pertusi\n"
        "Versão: 1.0\n\n"
        "Este programa realiza a verificação de portas em um host especificado.\n"
        "Você pode fornecer um intervalo de portas (por exemplo, 20-80) ou uma única porta.\n"
        "O programa tentará se conectar a cada porta no intervalo especificado\n"
        "e retornará se a porta está aberta ou fechada.\n\n"
        "Além disso, para portas conhecidas, o programa fornecerá uma breve\n"
        "descrição do serviço associado. Caso a porta não esteja no banco de\n"
        "dados de portas conhecidas, o programa retornará 'Serviço desconhecido'.\n\n"
        "Como usar:\n"
        "- Insira o endereço do host no campo 'Host'.\n"
        "- Insira o intervalo de portas (por exemplo, 20-80) ou uma única porta\n"
        "  no campo 'Range de Portas'.\n"
        "- Clique no botão 'Começar Scan' para iniciar a verificação.\n\n"
        "O resultado será exibido na janela de saída, mostrando o status de\n"
        "cada porta e o serviço associado (se conhecido)."
    )


# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Port Scan")

tk.Label(root, text="Host:").grid(row=0, column=0)
entry_host = tk.Entry(root)
entry_host.grid(row=0, column=1)

tk.Label(root, text="Range de Portas (ex: 20-80):").grid(row=1, column=0)
entry_ports = tk.Entry(root)
entry_ports.grid(row=1, column=1)

button_scan = tk.Button(root, text="Começar Scan", command=start_scan)
button_scan.grid(row=2, column=0, columnspan=2)

button_about = tk.Button(root, text="Sobre", command=about)
button_about.grid(row=3, column=0, columnspan=2)

text_output = tk.Text(root, height=30, width=100)
text_output.grid(row=4, column=0, columnspan=2)

well_known_ports = ler_portas_para_dict("common-ports.txt")

root.mainloop()
