# questionnaire.py

QUESTOES = [
    "O aprendizado é um processo de interação com as pessoas e coisas ao nosso redor.",
    "A pessoa humana é principalmente um sistema nervoso influenciado pela interação com o ambiente físico de acordo com princípios científicos.",
    "A educação deveria levar ao indivíduo à compreensão espiritual.",
    # Add more questions as needed
]

idealismo = [1, 2, 3]  # Adjust these indices based on your questions
realismo = [4, 5, 6]
pragmatismo = [7, 8, 9]
existencialismo = [10, 11, 12]

respostas = []
idealismo_soma = 0
realismo_soma = 0
pragmatismo_soma = 0
existencialismo_soma = 0

def validar_resposta(resposta):
    try:
        valor = int(resposta)
        return valor in [-2, -1, 0, 1, 2]
    except ValueError:
        return False

def calcular_somas():
    global idealismo_soma, realismo_soma, pragmatismo_soma, existencialismo_soma
    for i, (numero, resposta) in enumerate(respostas, start=1):
        if numero in idealismo:
            idealismo_soma += resposta
        elif numero in realismo:
            realismo_soma += resposta
        elif numero in pragmatismo:
            pragmatismo_soma += resposta
        else:
            existencialismo_soma += resposta

def mostrar_resultado():
    resultado = f"Idealismo: {idealismo_soma}\nRealismo: {realismo_soma}\nPragmatismo: {pragmatismo_soma}\nExistencialismo: {existencialismo_soma}"
    return resultado

def coletar_respostas():
    for i, questao in enumerate(QUESTOES, start=1):
        resposta = Element(f"resposta_{i}").element.value
        if validar_resposta(resposta):
            respostas.append((i, int(resposta)))
        else:
            return f"Erro: Resposta inválida para a pergunta {i}. Use valores entre -2 e 2."
    calcular_somas()
    return mostrar_resultado()

def criar_formulario():
    questionario_element = Element("questionario")
    html = ""
    for i, questao in enumerate(QUESTOES, start=1):
        html += f'<label for="resposta_{i}">{questao}</label><input type="text" id="resposta_{i}" name="resposta_{i}"><br>'
    html += '<button id="enviar">Enviar</button>'
    questionario_element.write(html)
    enviar_button = Element("enviar")
    enviar_button.element.onclick = lambda evt: Element("resultado").write(coletar_respostas())
