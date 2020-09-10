import React, { useState } from 'react'

export default function useErros(validacao) {

    const estadoInicial = criarEstadoInicial(validacao)
    const [erros, setErros] = useState(estadoInicial)

    function validarCampos(event) {
        const { name, value } = event.target
        const novoEstado = { ...erros }
        novoEstado[name] = validacao[name](value)
        setErros(novoEstado)
    }

    function possoEnviar() {
        for (let campo in erros) {
            if (!erros[campo].valido)
                return false
        }
        return true
    }

    return [erros, validarCampos, possoEnviar]

}

function criarEstadoInicial(validacao) {
    const estadoInicial = {}
    for (let campo in validacao)
        estadoInicial[campo] = { valido: true, texto: "" }

    return estadoInicial
}
