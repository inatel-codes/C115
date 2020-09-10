import React, { useState, useContext } from 'react'
import { Button, TextField } from "@material-ui/core"
import ValidacoesCadastro from "../../contexts/ValidacoesCadastro"
import useErros from "../../hooks/useErros"


export default function DadosUsuario({ aoEnviar }) {
    const [email, setEmail] = useState("")
    const [senha, setSenha] = useState("")
    const validacao = useContext(ValidacoesCadastro)
    const[erros, validarCampos, possoEnviar] = useErros(validacao)   

    return (
        <form onSubmit={(event) => {
            event.preventDefault()
            if (possoEnviar())
                aoEnviar({ email, senha });
        }}>
            <TextField
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                id="email"
                label="E-mail"
                name="email"
                type="email"
                required
                variant="outlined"
                margin="normal"
                fullWidth
            />

            <TextField
                value={senha}
                onChange={(event) => setSenha(event.target.value)}
                onBlur={validarCampos}
                error={!erros.senha.valido}
                helperText={erros.senha.texto}
                id="senha"
                name="senha"
                label="Senha"
                type="password"
                required
                variant="outlined"
                margin="normal"
                fullWidth
            />

            <Button variant="contained" color="primary" type="submit">Próximo</Button>
        </form>
    )
}