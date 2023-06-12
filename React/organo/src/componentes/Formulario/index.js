import './Formulario.css'
import ListaSuspensa from '../ListaSuspensa'
import Botao from '../Botao'
import { useState } from 'react'

const Formulario = (props) => {

    const [time, setTime] = useState('')


    

    const aoSalvar = (evento) => {
        evento.preventDefault()
        console.log('oi')
        console.log('Form foi submetido ' + props.nome, props.cargo, props.imagem, time)
        props.aoColaboradorCadastrado({
            nome: props.nome,
            cargo: props.cargo,
            imagem: props.imagem,
            time: time
        })
    }


    return (
    <section className="Formulario">
        <form onSubmit={aoSalvar}>
        <h1 className="h1">Preencha os dados para criar o card do colaborador.</h1>
        {props.children}
        <ListaSuspensa label="Time"
         obrigatorio={true}
         itens={props.times}
         valor={time}
         aoAlterado={valor => setTime(valor)}
         ></ListaSuspensa>
        <Botao>
            Criar Card
        </Botao>
        </form>
    </section>
    )
}

export default Formulario