const Voyage2 = ({time, changeColor}) => {
    return (
        <div>
            {time.map((obj, index) => (
                <div>
                    <h1 style={{textAlign: 'center', color: obj.Cor}} key={index}>{obj.Nome}</h1>
                    <button onClick={() => changeColor('green', obj.Nome)} >eae</button>
                </div>
                
            ))}
        </div>
    )
}

export default Voyage2;