def menuOpcoes():
    """
        Menu de opções inicial para o usuário poder navegar pelo sistema.
    """
    print(f"Bom dia, professor(a)! Seja bem-vindo ao sistema de gerenciamento de notas!")
    print(f"Escolha uma opção para continuar!")
    print(f"\n 1 - Adicionar alunos \n 2 - Remover alunos \n 3 - Adicionar notas \n 4 - Calcular média \n 5 - Exibir notas de um aluno específico \n 6 - Determinar melhor aluno pela média \n 7 - Determinar pior aluno pela média \n 8 - Encerrar o programa")
    opcao = int(input("Informe a opção desejada: "))
    return opcao

NotasAlunos = {}
#aluno = {}

while True:
    opcao = menuOpcoes()
    if opcao == 1:
        # Adicionar aluno individualmente
        rm = int(input("Informe o RM do aluno: "))
        if rm not in NotasAlunos:
            nome = input("Informe o nome do aluno: ")
            turma = input("Informe a turma do aluno: ")
            NotasAlunos[rm] = {"nome": nome, "turma": turma}
        else:
            print("O aluno já está cadastrado no nosso sistema!")
        print(NotasAlunos)
    elif opcao == 2:
        # Remover aluno individualmente pelo RM
        rm = int(input("Informe o RM do aluno que deseja remover: "))
        if rm in NotasAlunos:
            NotasAlunos.pop(rm)
        else:
            print("O RM informado não consta no sistema")
        print(NotasAlunos)
    elif opcao == 3:
        # Adicionar 4 notas do aluno
        rm = int(input("Informe o RM do aluno que deseja inserir notas: "))
        if rm in NotasAlunos:
            notas = []
            for i in range(4):
                nota = float(input("Informe a nota do aluno: "))
                notas.append(nota)
            NotasAlunos[rm]["notas"] = notas
        else:
            print("O RM informado não consta no nosso sistema!")
        print(NotasAlunos)
    elif opcao == 4:
        # Calcular média em base do RM informado
        rm = int(input("Informe o RM do aluno que deseja calcular média: "))
        aluno = NotasAlunos.get(rm)
        if aluno is not None:
            notas = aluno.get("notas")
            if notas is not None and len(notas) == 4:
                media = sum(notas) / 4
                print(f"A média do aluno de RM {rm} é de {media:.2f}")
            else:
                print("O aluno informado não possui notas cadastradas ou não há 4 notas registradas")
        else:
            print("O RM informado não consta no nosso sistema.")
    elif opcao == 5:
        # Ver notas de um aluno específico
        rm = int(input("Informe o RM do aluno que deseja ver as notas: "))
        if rm in NotasAlunos:
            if "notas" in NotasAlunos:
                print(f"O aluno de RM {rm} tem as notas de: {NotasAlunos['notas']}")
            else:
                print("O aluno informado não possui notas cadastradas")
        else:
            print("O RM informado não consta no nosso sistema!")
    elif opcao == 6:
        # Determinar melhor aluno
        melhor_aluno = None
        melhor_media = 0
        for rm, aluno_info in NotasAlunos.items():
            notas = aluno_info.get("notas")
            if notas is not None and len(notas) == 4:
                media = sum(notas) / 4
                if media > melhor_media:
                    melhor_aluno = rm
                    melhor_media = media
        if melhor_aluno is not None:
            print(f"O aluno de RM {melhor_aluno} é o melhor aluno com média {melhor_media:.2f}")
        else:
            print("Nenhum aluno possui notas cadastradas ou não há 4 notas registradas")
    elif opcao == 7:
        # Determinar pior aluno
        pior_aluno = None
        pior_media = float('inf')  # Inicializa com um valor infinito
        for rm, aluno_info in NotasAlunos.items():
            notas = aluno_info.get("notas")
            if notas is not None and len(notas) == 4:
                media = sum(notas) / 4
                if media < pior_media:
                    pior_aluno = rm
                    pior_media = media
        if pior_aluno is not None:
            print(f"O aluno de RM {pior_aluno} é o pior aluno com média {pior_media:.2f}")
        else:
            print("Nenhum aluno possui notas cadastradas ou não há 4 notas registradas")
    elif opcao == 8:
        # Encerrar o programa
        print("Obrigada por usar o nosso sistema!")
        break
    else:
        # Tratamento de erro caso opção inválida
        print("Opção inválida, tente novamente.")
