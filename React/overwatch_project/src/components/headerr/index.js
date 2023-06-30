import './headerr.css'

const Header2 = (props) => {

    const Log = (event) => {
        props.aoAlterar(event.target.value)
        console.log(event.target.value)
    }


    return (
        <><header className="Header">
            <h1>Ola mundo</h1>
        </header><input value={props.valor}  onChange={Log}  placeholder="Coloque seu nome aqui">

        </input></>
    )
}

export default Header2