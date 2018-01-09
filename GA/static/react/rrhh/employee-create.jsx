class Position extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            shift: '',
            payRange: '',
            is_active: '',
            name: '',
            salary: '',
            start: '',
            end: ''
        };
    }

    render (){
        return (
            <div>
                <h2 className="text-center">Información Laboral</h2>
                <br />
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_shift"> Turno: </label>
                        <select id="id_shift" name="shift" className="custom-select">
                            <option value="D" selected> Diurno </option>
                            <option value="M"> Mixto </option>
                            <option value="N"> Nocturno </option>
                        </select>
                    </div>

                    <div className="col">
                        <label for="id_pay_range"> Tipo De Pago: </label>
                        <select id="id_pay_range" name="pay_range" className="custom-select">
                            <option value="S" selected> Semanal </option>
                            <option value="Q"> Quincenal </option>
                        </select>
                    </div>

                    <div className="col">
                        <label for="id_is_active"> Status: </label>
                        <input id="id_is_active" name="is_active" type="checkbox"/>
                    </div>
                </div>
                <br />
                <div className="text-center form-group row">
                    <div class="col">
                        <label for="id_name"> Cargo: </label>
                        <input id="id_name" name="name" className="form-control" required type="text" maxlength="128"/>
                    </div>

                    <div className="col">
                        <label for="id_base_salary"> Salario: </label>
                        <input id="id_base_salary" name="base_salary" className="form-control" step="any" required type="number" min="1"/>
                    </div>

                    <div className="col">
                        <label for="id_food_salary"> Cestaticket: </label>
                        <input id="id_food_salary" name="food_salary" className="form-control" step="any" required type="number" min="1" />
                    </div>

                    <div className="col">
                        <label for="id_start"> Inicio: </label>
                        <input id="id_start" name="start" className="custom-select" equired type="date"/>
                    </div>

                    <div className="col">
                        <label for="id_end"> Fin : </label>
                        <input id="id_end" name="end" className="form-control" required type="date"/>
                    </div>

                </div>
                <br />
                <div className="text-center form-group row">
                    <a className="btn btn-warning col" onClick={this.props.componentBack}>
                        <span style={{color: 'white'}}>Atras</span>
                    </a>
                    <a className="btn btn-primary col" onClick={()=>{}}>
                        <span style={{color: 'white'}}>Aceptar</span>
                    </a>
                </div>
            </div>
        );
    }
};

class Spawn extends React.Component {
    constructor (props){
        super(props);
        this.state = {
            name: '',
            lastName: '',
            birthdate: '',
            gender: ''
        };
    }

    render (){
        return (
            <div>
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_name"> Nombres: </label>
                        <input id="id_name" name="name" className="form-control" required type="text" maxlength="128"/>
                    </div>

                    <div className="col">
                        <label for="id_last_name"> Apellidos: </label>
                        <input id="id_last_name" name="last_name" className="form-control" required type="text" maxlength="128"/>
                    </div>

                    <div className="col">
                        <label for="id_birthdate"> Fecha De Nacimiento: </label>
                        <input id="id_birthdate" name="birthdate" className="form-control" required type="date"/>
                    </div>

                    <div className="col">
                        <label for="id_gender"> Sexo: </label>
                        <select id="id_gender" name="gender" className="custom-select">
                            <option value="M"> Masculino </option>
                            <option value="F" selected > Femenino </option>
                            <option value="O"> Otros </option>
                        </select>
                    </div>
                </div>
            </div>
        );
    }
};

class Spouse extends React.Component {
    constructor (props){
        super(props);
        this.spawns = [];

        this.state = {
            gender: '',
            birthDate: '',
            name: '',
            lastName: '',
            cedula: '',
            mobilePhone: '',
            spawns: this.spawns,
        }
    }

    addSpawn (){
        this.spawns.push(
            <Spawn />
        );
        this.setState({
            spawns: this.spawns
        });
    }

    removeSpawn (){
        this.spawns.pop();
        this.setState({
            spawns: this.spawns
        });
    }

    render (){
        return (
            <div>
                <h2 className="text-center"> Cónyuge</h2>
                <br />
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_name"> Nombres: </label>
                        <input id="id_name" name="name" className="form-control" required type="text" maxlength="128"/>
                    </div>

                    <div className="col">
                        <label for="id_last_name"> Apellidos: </label>
                        <input id="id_last_name" name="last_name" className="form-control" required type="text" maxlength="128"/>
                    </div>

                    <div className="col">
                        <label for="id_cedula"> Cedula: </label>
                        <input id="id_cedula" name="cedula" className="form-control" required type="number" min="1"/>
                    </div>
                </div>
                <br />
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_birthdate"> Fecha De Nacimiento: </label>
                        <input id="id_birthdate" name="birthdate" className="form-control" required type="date"/>
                    </div>

                    <div className="col">
                        <label for="id_gender"> Sexo: </label>
                        <select id="id_gender" name="gender" className="custom-select">
                            <option value="M"> Masculino </option>
                            <option value="F" selected > Femenino </option>
                            <option value="O"> Otros </option>
                        </select>
                    </div>

                    <div className="col">
                        <label for="id_home_phone">Telefono Movil:</label>
                        <input id="id_mobile_phone" name="mobile_phone" className="form-control" type="text" required maxlength="40"/>
                    </div>
                </div>
                <br />
                {this.state.spawns.length === 0 ? 
                        ''
                        : 
                        <h2 className="text-center">Hijos</h2>
                    }
                {
                    this.state.spawns
                }
                <br />

                <div className="text-center">
                    {this.state.spawns.length === 0 ? 
                        ''
                        : 
                        <a className="btn btn-danger" onClick={()=>{this.removeSpawn()}}>
                            <span style={{color: 'white'}}>-</span>
                        </a>
                    }
                    <a className="btn btn-dark" onClick={()=>{this.addSpawn()}}>
                        <span style={{color: 'white'}}>+</span>
                    </a>
                </div>
                <br />
                <div className="text-center row">
                    <a className="btn btn-warning col" onClick={this.props.componentBack}>
                        <span style={{color: 'white'}}>Atras</span>
                    </a>
                    <a className="btn btn-primary col" onClick={this.props.componentNext}>
                        <span style={{color: 'white'}}>Siguiente</span>
                    </a>
                </div>
            </div>
        );
    }
};

class Employee extends React.Component {
    constructor (props){
        super(props);
        this.state = {
            id: '',
            gender: '',
            birthDate: '',
            name: '',
            lastName: '',
            cedula: '',
            addres: '',
            civilStatus: '',
            homePhone: '',
            mobilePhone: ''
        }
    }

    preserveData(){
        this.id = document.getElementById("id_employee_id").value;
        this.setState({id: this.id});
        this.props.componentNext();
    }

    render (){
        return (
            <div>
                <h2 className="text-center"> Información Personal</h2>
                <br />
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_employee_id"> ID del Empleado: </label>
                        <input id="id_employee_id" name="employee_id" className="form-control" required type="number" min="1"/>
                    </div>
                
                    <div className="col">
                        <label for="id_gender"> Sexo: </label>
                        <select id="id_gender" name="gender" className="custom-select">
                            <option value="M" selected> Masculino </option>
                            <option value="F"> Femenino </option>
                            <option value="O"> Otros </option>
                        </select>
                    </div>
                </div>
                <br />
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_name"> Nombres: </label>
                        <input id="id_name" name="name" className="form-control" required type="text" maxlength="128"/>
                    </div>

                    <div className="col">
                        <label for="id_last_name"> Apellidos: </label>
                        <input id="id_last_name" name="last_name" className="form-control" required type="text" maxlength="128"/>
                    </div>

                    <div className="col">
                        <label for="id_cedula"> Cedula: </label>
                        <input id="id_cedula" name="cedula" className="form-control" required type="number" min="1"/>
                    </div>
                </div>
                <br />
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_birthdate"> Fecha De Nacimiento: </label>
                        <input id="id_birthdate" name="birthdate" className="form-control" required type="date"/>
                    </div>

                    <div className="col">
                        <label for="id_address"> Direccion: </label>
                        <input id="id_address" name="address" className="form-control" type="text" required maxlength="256"/>
                    </div>

                    <div className="col">
                        <label for="id_civil_status"> Estado Civil: </label>
                        <select id="id_civil_status" name="civil_status" className="custom-select">
                            <option value="S" selected> Soltero </option>
                            <option value="C"> Casado </option>
                            <option value="V"> Viudo </option>
                        </select>
                    </div>
                </div>
                <br />
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_home_phone">Telefono Hogar:</label>
                        <input id="id_home_phone" name="home_phone" className="form-control" type="text" required maxlength="40"/>
                    </div>

                    <div className="col">
                        <label for="id_home_phone">Telefono Movil:</label>
                        <input id="id_mobile_phone" name="mobile_phone" className="form-control" type="text" required maxlength="40"/>
                    </div>
                </div>
                <br />
                <div className="text-center row">
                    <a className="btn btn-block btn-primary" onClick={ this.preserveData.bind(this) }>
                        <span style={{color: 'white'}}>Siguiente</span>
                    </a>
                </div>
            </div> 
        );
    }
};

class EmployeeCreate extends React.Component {
    constructor (props){
        super(props);
        this.components = [
            <Employee key={1} componentBack={this.componentBack.bind(this)} componentNext={this.componentNext.bind(this)}/>,
            <Spouse key={2} componentBack={this.componentBack.bind(this)} componentNext={this.componentNext.bind(this)}/>,
            <Position key={3} componentBack={this.componentBack.bind(this)} componentNext={this.componentNext.bind(this)}/>
        ];

        this.state = {
            current: this.components[0],
            index: 0
        };
    }

    componentNext (){
        if (this.state.index === this.components.length) {
            this.setState({
                current: this.components[0]
            })
            
        } else {
            this.setState({
                current: this.components[this.state.index + 1],
                index: this.state.index + 1
            })
            
        }
    }

    componentBack (){
        if (this.state.index - 1 === 0) {
            this.setState({
                current: this.components[0],
                index: 0
            })
        } else {
            this.setState({
                current: this.components[this.state.index - 1],
                index: this.state.index - 1
            })
        }
    }

    render (){
        return (
            <div className="">
                {this.state.current}
                <br/>
                <a className="btn btn-block btn-danger" href="{% url 'rrhh:index' %}">
                    <span style={{ color: 'white' }}>Cancelar</span>
                </a>
            </div>
        );
    }
};

ReactDOM.render (
    <EmployeeCreate />,
    document.getElementById('root')
);