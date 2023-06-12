import './Time.css'

const Time = (props) => {
    const css1 = { backgroundColor: props.corSecundaria }
    const css2 = { borderColor: props.corPrimaria }
    return (
        
        <section className="time" style={ css1 }>
            <h3 style={ css2 }>{props.nome}</h3>
        </section>
    )
}

export default Time