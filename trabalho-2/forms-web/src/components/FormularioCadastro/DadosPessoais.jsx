import React, { useState, useContext } from 'react';
import { Button, TextField, Switch, FormControlLabel } from "@material-ui/core"
import ValidacoesCadastro from "../../contexts/ValidacoesCadastro"
import useErros from "../../hooks/useErros"


export default function DadosPessoais({ aoEnviar }) {
    const [nome, setNome] = useState("")
    const [sobrenome, setSobrenome] = useState("")
    const [cpf, setCPF] = useState("")
    const [promocoes, setPromocoes] = useState(true)
    const [novidades, setNovidades] = useState(true)
    const validacao = useContext(ValidacoesCadastro)

    const [erros, validarCampos, possoEnviar] = useErros(validacao)

    return (
        <form
            onSubmit={(event) => {
                event.preventDefault();
                if (possoEnviar())
                    aoEnviar({ nome, sobrenome, cpf, novidades, promocoes })
            }}
        >
            <TextField
                value={nome}
                onChange={(event) => setNome(event.target.value)}
                id="nome"
                label="Nome"
                name="nome"
                required
                variant="outlined"
                margin="normal"
                fullWidth
            />

            <TextField
                value={sobrenome}
                onChange={(event) => setSobrenome(event.target.value)}
                id="sobrenome"
                label="Sobrenome"
                name="sobrenome"
                required
                variant="outlined"
                margin="normal"
                fullWidth
            />

            <TextField
                value={cpf}
                onChange={(event) => setCPF(event.target.value)}
                onBlur={validarCampos}
                error={!erros.cpf.valido}
                helperText={erros.cpf.texto}
                id="CPF"
                name="cpf"
                label="CPF"
                required
                variant="outlined"
                margin="normal"
                fullWidth
            />

            <FormControlLabel
                label="Promoções"
                control={
                    <Switch
                        onChange={(event) => setPromocoes(event.target.checked)}
                        checked={promocoes}
                        name="promocoes"
                        color="primary"
                    />}

            />
            <FormControlLabel
                label="Novidades"
                control={
                    <Switch
                        onChange={(event) => setNovidades(event.target.checked)}
                        checked={novidades}
                        name="novidades"
                        color="primary"
                    />}

            />

            <Button variant="contained" color="primary" type="submit">Próximo</Button>

        </form>
    )
}