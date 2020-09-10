import React, { Component } from 'react'
import './App.css'
import FormularioCadastro from "./components/FormularioCadastro/FormularioCadastro"
import { validarCPF, validarSenha } from "./models/cadastro"
import ValidacoesCadastro from "./contexts/ValidacoesCadastro"
import { Container, Typography } from '@material-ui/core'
import 'fontsource-roboto'


class App extends Component {
  render() {
    return (
      <Container component="article" maxWidth="sm">
        <Typography variant="h3" align="center" component="h1" color="primary">
          Formulário de C115
        </Typography>
        <ValidacoesCadastro.Provider value={{ cpf: validarCPF, senha: validarSenha }}>
          <FormularioCadastro aoEnviar={aoEnviarForm} />
        </ValidacoesCadastro.Provider>
      </Container>
    );
  }
}

function aoEnviarForm(dados) {
  console.log(dados)
}

export default App;
