import React from 'react'

const ValidacoesCadastro = React.createContext({ cpf: semValidacao, senha: semValidacao })

function semValidacao(dados) {
    return { valido: true, texto: "" }
}

export default ValidacoesCadastro