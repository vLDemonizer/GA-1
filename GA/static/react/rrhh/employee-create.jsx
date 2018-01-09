class Position extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            shift: this.props.position.shift,
            payRange: this.props.position.payRange,
            is_active: this.props.position.status,
            name: this.props.position.name,
            base_salary: this.props.position.base_salary,
            food_salary: this.props.position.food_salary,
            start: this.props.position.start,
            end: this.props.position.end
        };
    }

    render (){
        let shift = [];
        if (this.state.shift === "D" || this.state.shift === ""){
            shift.push(
                <option value="D" selected> Diurno </option>,
                <option value="M"> Mixto </option>,
                <option value="N"> Nocturno </option>
            );
        }
        else if (this.state.shift === "M"){
            shift.push(
                <option value="D"> Diurno </option>,
                <option value="M" selected> Mixto </option>,
                <option value="N"> Nocturno </option>
            );
        }
        else if (this.state.shift === "N"){
            shift.push(
                <option value="D"> Diurno </option>,
                <option value="M"> Mixto </option>,
                <option value="N" selected> Nocturno </option>
            );
        }

        let payRange = [];
        if (this.state.payRange === "S" || this.state.payRange === ""){
            payRange.push(
                <option value="S" selected> Semanal </option>,
                <option value="Q"> Quincenal </option>
            );
        }
        else if (this.state.payRange === "Q"){
            payRange.push(
                <option value="S"> Semanal </option>,
                <option value="Q" selected> Quincenal </option>
            );
        }

        return (
            <div>
                <h2 className="text-center">Información Laboral</h2>

                <br />
                {/* Shift, Pay Range and Status */}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_shift"> Turno: </label>
                        <select id="id_shift" name="shift" className="custom-select">
                            { shift }
                        </select>
                    </div>

                    <div className="col">
                        <label for="id_pay_range"> Tipo De Pago: </label>
                        <select id="id_pay_range" name="pay_range" className="custom-select">
                            { payRange }
                        </select>
                    </div>

                    <div className="col">
                        <label for="id_is_active"> Status: </label>
                        { this.state.is_active ? 
                            <input id="id_is_active" name="is_active" defaultChecked={true} type="checkbox"/> 
                            : 
                            <input id="id_is_active" name="is_active" type="checkbox"/>
                        }
                    </div>
                </div>

                <br />
                {/* Position Name, Base Salary, Food Salary, Start, End */}
                <div className="text-center form-group row">
                    <div class="col">
                        <label for="id_name"> Cargo: </label>
                        <input 
                            id="id_name" 
                            name="name" 
                            className="form-control" 
                            required 
                            type="text" 
                            maxlength="128"
                            defaultValue={ this.state.name }
                        />
                    </div>

                    <div className="col">
                        <label for="id_base_salary"> Salario: </label>
                        <input 
                            id="id_base_salary" 
                            name="base_salary" 
                            className="form-control" 
                            step="any" 
                            required 
                            type="number" 
                            min="1"
                            defaultValue={ this.state.base_salary }    
                        />
                    </div>

                    <div className="col">
                        <label for="id_food_salary"> Cestaticket: </label>
                        <input 
                            id="id_food_salary" 
                            name="food_salary" 
                            className="form-control" 
                            step="any" 
                            required 
                            type="number" 
                            min="1" 
                            defaultValue={ this.state.food_salary }    
                        />
                    </div>

                    <div className="col">
                        <label for="id_start"> Inicio: </label>
                        <input 
                            id="id_start" 
                            name="start" 
                            className="custom-select" 
                            required 
                            type="date"
                            defaultValue={ this.state.start }    
                        />
                    </div>

                    <div className="col">
                        <label for="id_end"> Fin : </label>
                        <input 
                            id="id_end" 
                            name="end" 
                            className="form-control" 
                            required 
                            type="date"
                            defaultValue={ this.state.end }
                        />
                    </div>

                </div>

                <br />
                {/* Back and Submit Button */}
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
            name: this.props.spawn.name,
            lastName: this.props.spawn.lastName,
            birthDate: this.props.spawn.birthDate,
            gender: this.props.spawn.gender
        };
    }

    handleChange(e, type){
        if (type === 'Name'){
            this.setState({ name: e.target.value });
        }
        else if (type === 'LastName'){
            this.setState({ lastName: e.target.value });
        }
        else if (type === 'Birthdate'){
            this.setState({ birthDate: e.target.value });
        }
        else if (type === 'Gender') {
            this.setState({ gender: e.target.value });
        }
    }

    preserveData(){
        return this.state;
    }

    render (){
        let gender = [];
        if(this.state.gender === "M" || this.state.gender === ""){
            gender.push(
                <option value="M" selected> Masculino </option>,
                <option value="F"> Femenino </option>,
                <option value="O"> Otros </option>
            );
        }
        else if (this.state.gender === "F"){
            gender.push(
                <option value="M"> Masculino </option>,
                <option value="F" selected> Femenino </option>,
                <option value="O"> Otros </option>
            );
        }
        else if (this.state.gender === "O"){
            gender.push(
                <option value="M"> Masculino </option>,
                <option value="F"> Femenino </option>,
                <option value="O" selected> Otros </option>
            );
        }

        return (
            <div>
                {/* Name, Last Name, Birthdate, Gender */}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_name"> Nombres: </label>
                        <input 
                            id="id_spawn_name" 
                            name="name" 
                            className="form-control" 
                            required 
                            type="text" 
                            maxlength="128"
                            defaultValue={ this.state.name }
                            onChange={this.handleChange("Name").bind(this)}
                        />
                    </div>

                    <div className="col">
                        <label for="id_last_name"> Apellidos: </label>
                        <input 
                            id="id_spawn_last_name" 
                            name="last_name" 
                            className="form-control" 
                            required 
                            type="text" 
                            maxlength="128"
                            defaultValue={ this.state.lastName }
                            onChange={this.handleChange("LastName").bind(this)}
                        />
                    </div>

                    <div className="col">
                        <label for="id_birthdate"> Fecha De Nacimiento: </label>
                        <input 
                            id="id_spawn_birthdate" 
                            name="birthdate" 
                            className="form-control" 
                            required 
                            type="date" 
                            defaultValue={this.state.birthDate}
                            onChange={this.handleChange("Birthdate").bind(this)}
                        />
                    </div>

                    <div className="col">
                        <label for="id_gender"> Sexo: </label>
                        <select id="id_spawn_gender" name="gender" className="custom-select" onChange={this.handleChange("Gender").bind(this)}>
                            { gender }
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
        this.props.spawns.map(spawn => {
            this.spawns.push(
                <Spawn spawn={ spawn }/>
            );
        });

        this.state = {
            gender: this.props.spouse.gender,
            birthDate: this.props.spouse.birthDate,
            name: this.props.spouse.name,
            lastName: this.props.spouse.lastName,
            cedula: this.props.spouse.cedula,
            mobilePhone: this.props.spouse.mobilePhone,
            spawns: this.spawns,
        }
    }

    addSpawn (){
        let spawn = {
            name: '',
            lastName: '',
            birthDate: '',
            gender: ''  
        }
        this.spawns.push(
            <Spawn spawn={ spawn }/>
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

    preserveData(){
        let spouse = {
            name: document.getElementById("id_name").value,
            lastName: document.getElementById("id_last_name").value,
            birthDate: document.getElementById("id_birthdate").value,
            gender: document.getElementById("id_gender").value,
            mobilePhone: document.getElementById("id_mobile_phone").value
        };

        let spawns = [];

        let data = {
            spouse: spouse,
            spawn: spawns
        }
    }

    render (){
        let gender = [];
        if(this.state.gender === "M" || this.state.gender === ""){
            gender.push(
                <option value="M" selected> Masculino </option>,
                <option value="F"> Femenino </option>,
                <option value="O"> Otros </option>
            );
        }
        else if (this.state.gender === "F"){
            gender.push(
                <option value="M"> Masculino </option>,
                <option value="F" selected> Femenino </option>,
                <option value="O"> Otros </option>
            );
        }
        else if (this.state.gender === "O"){
            gender.push(
                <option value="M"> Masculino </option>,
                <option value="F"> Femenino </option>,
                <option value="O" selected> Otros </option>
            );
        }

        return (
            <div>
                <h2 className="text-center"> Cónyuge</h2>

                <br />
                {/* Name, Last Name and Cedula*/}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_name"> Nombres: </label>
                        <input 
                            id="id_name" 
                            name="name" 
                            className="form-control" 
                            required 
                            type="text" 
                            maxlength="128"
                            defaultValue={ this.state.name }
                        />
                    </div>

                    <div className="col">
                        <label for="id_last_name"> Apellidos: </label>
                        <input 
                            id="id_last_name" 
                            name="last_name" 
                            className="form-control" 
                            required 
                            type="text" 
                            maxlength="128"
                            defaultValue={ this.state.lastName }
                        />
                    </div>

                    <div className="col">
                        <label for="id_cedula"> Cedula: </label>
                        <input 
                            id="id_cedula" 
                            name="cedula" 
                            className="form-control" 
                            required 
                            type="number" 
                            min="1"
                            defaultValue={ this.state.cedula }
                        />
                    </div>
                </div>

                <br />
                {/* Birthdate, Gender, Mobile Phone*/}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_birthdate"> Fecha De Nacimiento: </label>
                        <input 
                            id="id_birthdate" 
                            name="birthdate" 
                            className="form-control" 
                            required 
                            type="date" 
                            defaultValue={this.state.birthDate}
                        />
                    </div>

                    <div className="col">
                        <label for="id_gender"> Sexo: </label>
                        <select id="id_gender" name="gender" className="custom-select">
                            { gender }
                        </select>
                    </div>

                    <div className="col">
                        <label for="id_home_phone">Teléfono Móvil:</label>
                        <input 
                            id="id_mobile_phone" 
                            name="mobile_phone" 
                            className="form-control" 
                            type="text" 
                            required 
                            maxlength="40"
                            defaultValue={ this.state.mobilePhone }
                        />
                    </div>
                </div>

                <br />

                {/* Row Control for Spawns*/}
                {this.state.spawns.length === 0 ? 
                        ''
                        : 
                        <h2 className="text-center">Hijos</h2>
                }
                {
                    this.state.spawns
                }
                
                <br />
                {/* Remove and Add Sapwn Buttons*/}
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

                {/* Back and Next Button*/}
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
            id: this.props.employee.employeeID,
            gender: this.props.employee.gender,
            birthDate: this.props.employee.birthDate,
            name: this.props.employee.name,
            lastName: this.props.employee.lastName,
            cedula: this.props.employee.cedula,
            addres: this.props.employee.address,
            civilStatus: this.props.employee.civilStatus,
            homePhone: this.props.employee.homePhone,
            mobilePhone: this.props.employee.mobilePhone
        }
    }

    preserveData(){
        let data = {
            employeeID: document.getElementById("id_employee_id").value,
            gender: document.getElementById("id_gender").value,
            name: document.getElementById("id_name").value,
            lastName: document.getElementById("id_last_name").value,
            cedula: document.getElementById("id_cedula").value,
            birthDate: document.getElementById("id_birthdate").value,
            civilStatus: document.getElementById("id_civil_status").value,
            address: document.getElementById("id_address").value,
            homePhone: document.getElementById("id_home_phone").value,
            mobilePhone: document.getElementById("id_mobile_phone").value
        }

        this.props.componentNext(data, "Employee");
    }

    render (){
        let gender = [];
        if(this.state.gender === "M" || this.state.gender === ""){
            gender.push(
                <option value="M" selected> Masculino </option>,
                <option value="F"> Femenino </option>,
                <option value="O"> Otros </option>
            );
        }
        else if (this.state.gender === "F"){
            gender.push(
                <option value="M"> Masculino </option>,
                <option value="F" selected> Femenino </option>,
                <option value="O"> Otros </option>
            );
        }
        else if (this.state.gender === "O"){
            gender.push(
                <option value="M"> Masculino </option>,
                <option value="F"> Femenino </option>,
                <option value="O" selected> Otros </option>
            );
        }

        let civilStatus = [];
        if(this.state.civilStatus === "S" || this.state.civilStatus === ""){
            civilStatus.push(
                <option value="S" selected> Soltero </option>,
                <option value="C"> Casado </option>,
                <option value="V"> Viudo </option>
            );
        }
        else if (this.state.civilStatus === "C"){
            civilStatus.push(
                <option value="S"> Soltero </option>,
                <option value="C" selected> Casado </option>,
                <option value="V"> Viudo </option>
            );
        }
        else if (this.state.civilStatus === "V"){
            civilStatus.push(
                <option value="S"> Soltero </option>,
                <option value="C"> Casado </option>,
                <option value="V" selected> Viudo </option>
            );
        }

        return (
            <div>
                <h2 className="text-center"> Información Personal</h2>

                <br />
                {/* Employee ID and Gender */}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_employee_id"> ID del Empleado: </label>
                        <input 
                            id="id_employee_id" 
                            name="employee_id" 
                            className="form-control" 
                            required 
                            type="number" 
                            min="1" 
                            defaultValue={ this.state.id }
                        />
                    </div>
                
                    <div className="col">
                        <label for="id_gender"> Sexo: </label>
                        <select id="id_gender" name="gender" className="custom-select">
                            { gender }
                        </select>
                    </div>
                </div>

                <br />
                {/* Name, Last Name and Cedula*/}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_name"> Nombres: </label>
                        <input 
                            id="id_name" 
                            name="name" 
                            className="form-control" 
                            required 
                            type="text" 
                            maxlength="128"
                            defaultValue={ this.state.name }
                        />
                    </div>

                    <div className="col">
                        <label for="id_last_name"> Apellidos: </label>
                        <input 
                            id="id_last_name" 
                            name="last_name" 
                            className="form-control" 
                            required 
                            type="text" 
                            maxlength="128"
                            defaultValue={ this.state.lastName }
                        />
                    </div>

                    <div className="col">
                        <label for="id_cedula"> Cedula: </label>
                        <input 
                            id="id_cedula" 
                            name="cedula" 
                            className="form-control" 
                            required 
                            type="number" 
                            min="1"
                            defaultValue={ this.state.cedula }
                        />
                    </div>
                </div>

                <br />
                {/* Birthdate, Address, Civil Status */}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_birthdate"> Fecha De Nacimiento: </label>
                        <input 
                            id="id_birthdate" 
                            name="birthdate" 
                            className="form-control" 
                            required 
                            type="date" 
                            defaultValue={this.state.birthDate}
                        />
                    </div>

                    <div className="col">
                        <label for="id_address"> Dirección: </label>
                        <input 
                            id="id_address" 
                            name="address" 
                            className="form-control" 
                            type="text" 
                            required 
                            maxlength="256"
                            defaultValue={ this.state.addres }
                        />
                    </div>

                    <div className="col">
                        <label for="id_civil_status"> Estado Civíl: </label>
                        <select id="id_civil_status" name="civil_status" className="custom-select">
                            { civilStatus }
                        </select>
                    </div>
                </div>

                <br />
                {/* Home Phone and Mobile Phone */}
                <div className="text-center form-group row">
                    <div className="col">
                        <label for="id_home_phone">Teléfono de Contacto:</label>
                        <input 
                            id="id_home_phone" 
                            name="home_phone" 
                            className="form-control" 
                            type="text" 
                            required 
                            maxlength="40"
                            defaultValue={ this.state.homePhone }
                        />
                    </div>

                    <div className="col">
                        <label for="id_home_phone">Teléfono Móvil:</label>
                        <input 
                            id="id_mobile_phone" 
                            name="mobile_phone" 
                            className="form-control" 
                            type="text" 
                            required 
                            maxlength="40"
                            defaultValue={ this.state.mobilePhone }
                        />
                    </div>
                </div>

                <br />
                {/* Next Button*/}
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
        this.state = {
            current: <Employee 
                key={ 1 }
                employee={ this.props.data.employee } 
                componentBack={ this.componentBack.bind(this) } 
                componentNext={ this.componentNext.bind(this) }
            />,
            index: 0,
            data: {
                employee: this.props.data.employee,
                spouse: this.props.data.spouse,
                spawn: this.props.data.spawn,
                position: this.props.data.position
            }
        };
        
        this.components = [
            <Employee 
                key={ 1 }
                employee={ this.state.data.employee } 
                componentBack={ this.componentBack.bind(this) } 
                componentNext={ this.componentNext.bind(this) }
            />,
            <Spouse 
                key={2}
                spouse={ this.state.data.spouse }
                spawns= { this.state.data.spawn} 
                componentBack={this.componentBack.bind(this)} 
                componentNext={this.componentNext.bind(this)}
            />,
            <Position 
                key={3}
                position={ this.state.data.position } 
                componentBack={this.componentBack.bind(this)} 
                componentNext={this.componentNext.bind(this)}
            />
        ];
        
    }

    componentNext (data, type){
        if ( type === 'Employee'){
            let aux = {
                employee: data,
                spouse: this.state.data.spouse,
                spawn: this.state.data.spawn,
                position: this.state.data.position
            };
            if (this.state.index === this.components.length) {
                this.setState({
                    current: this.components[0],
                    data: aux
                })
            } else {
                this.setState({
                    current: this.components[this.state.index + 1],
                    index: this.state.index + 1,
                    data: aux
                })
            }
        }
        else if (type === 'Spouse'){
            let aux = {
                employee: this.state.employee,
                spouse: data.spouse,
                spawn: data.spawn,
                position: this.state.data.position
            };
            if (this.state.index === this.components.length) {
                this.setState({
                    current: this.components[0],
                    data: aux
                })
            } else {
                this.setState({
                    current: this.components[this.state.index + 1],
                    index: this.state.index + 1,
                    data: aux
                })
            }
        }
        else if (type === 'Position'){
            let aux = {
                employee: this.state.dataemployee,
                spouse: this.state.data.spouse,
                spawn: this.state.data.spawn,
                position: data
            };
            if (this.state.index === this.components.length) {
                this.setState({
                    current: this.components[0],
                    data: aux
                })
            } else {
                this.setState({
                    current: this.components[this.state.index + 1],
                    index: this.state.index + 1,
                    data: aux
                })
            }
        }
    }

    componentBack (data, type){
        if ( type === 'Employee'){
            let aux = {
                employee: data,
                spouse: this.state.data.spouse,
                spawn: this.state.data.spawn,
                position: this.state.data.position
            };
            if (this.state.index - 1 === 0) {
                this.setState({
                    current: this.components[0],
                    index: 0,
                    data: aux
                })
            } else {
                this.setState({
                    current: this.components[this.state.index - 1],
                    index: this.state.index - 1,
                    data: aux
                })
            }
        }
        else if (type === 'Spouse'){
            let aux = {
                employee: this.state.employee,
                spouse: data.spouse,
                spawn: data.spawn,
                position: this.state.data.position
            };
            if (this.state.index - 1 === 0) {
                this.setState({
                    current: this.components[0],
                    index: 0,
                    data: aux
                })
            } else {
                this.setState({
                    current: this.components[this.state.index - 1],
                    index: this.state.index - 1,
                    data: aux
                })
            }
        }
        else if (type === 'Position'){
            let aux = {
                employee: this.state.dataemployee,
                spouse: this.state.data.spouse,
                spawn: this.state.data.spawn,
                position: data
            };
            if (this.state.index - 1 === 0) {
                this.setState({
                    current: this.components[0],
                    index: 0,
                    data: aux
                })
            } else {
                this.setState({
                    current: this.components[this.state.index - 1],
                    index: this.state.index - 1,
                    data: aux
                })
            }
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