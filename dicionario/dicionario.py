professor = {
    "id": 1,
    "nome": "Linnek Rocha"
}

turma = {
    "id": 1,
    "curso":"enfermagem",
    "codigo_turma": "ENF261N",
    "turno": "noturno"
}

disciplina = {
    "id" : 1,
    "nome" : "Anatomia"
}

sala = {
    "id" : 1,
    "identificacao" : "Sala 5"
}

alocacao = {
    "id" : 1,
    "professor": professor,
    "turma": turma,
    "disciplina": disciplina,
    "sala": sala,
    "data_inicio": "26/08/2026",
    "data_fim": "10/09/2026"
}

solicitacao ={
    "id" : 1,
    "alocacao": alocacao,
    "problema": "Ar-condicionado",
    "horario_de_abertura" : "18:35",
    "horario_de_atendimento": None,
    "horario_de_conclusao": None,
    "status": "AGUARDANDO"
}
#estrutura de dicionários para consulta de dados
print (professor["nome"])
print (turma["codigo_turma"])
print (disciplina["nome"])
print (sala["identificacao"])

print ("=== ALOCAÇÕES ===")
print (alocacao["id"])
print (alocacao["professor"]["nome"]) #exibe as informações fazendo a consulta de um dicionário através de outro dicionário
print (alocacao["turma"]["codigo_turma"])
print (alocacao["disciplina"]["nome"])
print (alocacao["sala"]["identificacao"])
print (alocacao["data_inicio"])
print (alocacao["data_fim"])

print ("=== SOLICITAÇÃO ===")
print (solicitacao["id"])
print (solicitacao ["alocacao"]["id"])
print (solicitacao ["alocacao"]["professor"]["nome"])
print (solicitacao ["alocacao"]["turma"]["codigo_turma"])
print (solicitacao ["alocacao"]["disciplina"]["nome"])
print (solicitacao ["alocacao"]["sala"]["identificacao"])
print (solicitacao ["alocacao"]["data_inicio"])
print (solicitacao ["alocacao"]["data_fim"])
print (solicitacao ["problema"])
print (solicitacao ["horario_de_abertura"])
print (solicitacao ["horario_de_atendimento"])
print (solicitacao ["horario_de_conclusao"])
print (solicitacao ["status"])

#solicitacao ["status"] = "CONCLUÍDO"

if solicitacao ["status"] == "AGUARDANDO":
    solicitacao ["status"] = "EM ATENDIMENTO"
    solicitacao ["horario_de_atendimento"] = "18:38"
    print ("=== APÓS ACEITAR ===")
    print (solicitacao["id"])
    print (solicitacao ["alocacao"]["id"])
    print (solicitacao ["alocacao"]["professor"]["nome"])
    print (solicitacao ["alocacao"]["turma"]["codigo_turma"])
    print (solicitacao ["alocacao"]["disciplina"]["nome"])
    print (solicitacao ["alocacao"]["sala"]["identificacao"])
    print (solicitacao ["alocacao"]["data_inicio"])
    print (solicitacao ["alocacao"]["data_fim"])
    print (solicitacao ["problema"])
    print (solicitacao ["horario_de_abertura"])
    print (solicitacao ["horario_de_atendimento"])
    print (solicitacao ["horario_de_conclusao"])
    print (solicitacao ["status"])
else:
    print ("Não é possível aceitar essa solicitação")
    print (f"Status da solicitação: {solicitacao['status']}")