class First_Name extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      value: '',
      limit: 30,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if(!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
  }

  render(){
    return (
      <div className="form-group">
        <label>First Name: <small className="text-from text-muted">Character limit {this.state.current} of 30.</small></label>
        <input
          id="id_first_name"
          name="first_name"
          type="text"
          className="form-control"
          placeholder="Enter your First Name"
          value={this.state.value}
          onChange={this.handleChange}
          required
        />
      </div>
    );
  }
};

class Last_Name extends First_Name{
  constructor(props){
    super(props);
  }

  render(){
    return (
      <div className="form-group">
        <label>Last Name:
          <small className="text-from text-muted"> Character limit {this.state.current} of 30.</small></label>
        <input
          id="id_last_name"
          name="last_name"
          type="text"
          className="form-control"
          placeholder="Enter your Last Name"
          value={this.state.value}
          onChange={this.handleChange}
          required
        />
      </div>
    );
  }
};

class Email_Address extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      value: '',
      limit: 254,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    var value = event.target.value
    if(!(current > this.state.limit) )
      this.setState({
        value: event.target.value,
        current: current
      });
  }

  render(){
    return (
      <div className="form-group">
        <label>Email Address:
          <small className="text-from text-muted"> Character limit {this.state.current} of 254.</small></label>
        <input
          id="id_email"
          name="email"
          type="email"
          className="form-control"
          placeholder="Email here"
          value={this.state.value}
          onChange={this.handleChange}
          required
        />
      </div>
    );
  }
};

class UserName extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      value: '',
      limit: 150,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if(!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
  }

  render(){
    return (
      <div className="form-group">
        <label>Username:
          <small className="text-from text-muted"> Character limit {this.state.current} of 150.</small></label>
        <input
          id="id_username"
          name="username"
          type="text"
          className="form-control"
          placeholder="Enter your Username"
          value={this.state.value}
          onChange={this.handleChange}
          required
        />
      </div>
    );
  }
};

class Password extends React.Component{
  constructor(props){
    super(props);

    this.handleOnChange1 = this.handleOnChange1.bind(this);
    this.handleOnChange2 = this.handleOnChange2.bind(this);
  }

  handleOnChange1(evt){
    this.props.propshandleOnChange1(evt);
  }

  handleOnChange2(evt){
    this.props.propshandleOnChange2(evt);
  }

  render(){
    return (
      <div className="form-group">
        <div className="form-group">
          <label>Password:</label>
          <input
            id="id_password"
            name="password"
            type="password"
            className="form-control"
            value={this.props.value1}
            onChange={this.handleOnChange1}
            required
          />
        </div>
        <div className="form-group">
        <label>Password (Confirm):</label>
          <input
            type="password"
            className="form-control"
            value={this.props.value2}
            onChange={this.handleOnChange2}
            required
          />
        </div>
      </div>
    );
  }
};

class Enterprise_Info extends React.Component{
    render(){
      return (
        <div className="form-group">
          <label>Enterprise</label>
          <input
            id="id_enterprise"
            name="enterprise"
            type="text"
            className="form-control"
            readOnly="True"
            value="Grupo Alcars"
          />
          <label>Country</label>
          <input
            id="id_country"
            name="country"
            type="text"
            className="form-control"
            readOnly="True"
            value="Venezuela"
          />
          <label>City</label>
          <input
            id="id_city"
            name="city"
            type="text"
            className="form-control"
            readOnly="True"
            value="Puerto La Cruz"
          />
          <label>Designation</label>
          <input
            id="id_designation"
            name="designation"
            type="text"
            className="form-control"
          />
          <label>Admin Access</label>
          <input
            id="id_admin"
            name="admin"
            type="checkbox"
            className="form-control"
          />
        </div>
      );
    }
};

class CreateUserForm extends React.Component{
    constructor(props){
        super(props);
        this.state = {
          value1: '',
          value2: '',
          flag: false,
        };

        this.handleOnChange1 = this.handleOnChange1.bind(this);
        this.handleOnChange2 = this.handleOnChange2.bind(this);
        this.checkPassword = this.checkPassword.bind(this);
    }

    handleOnChange1(evt){
      this.setState({
        value1: evt.target.value,
      });
    }

    handleOnChange2(evt){
      this.setState({
        value2: evt.target.value,
      });
    }

    checkPassword(e){
      if (this.state.flag) {
        this.setState({flag: false});
      }
      if (this.state.value1.localeCompare(this.state.value2) == 0){
        document.getElementById('id_form').submit()
      } else {
        e.preventDefault()
        this.setState({
          flag: true,
        });
      }
    }


    render(){
      let error = (
        <p style={{color: 'red'}}> Password dont match</p>
      );
      return (
        <div className="container-fluid">
          <div className="container-fluid">
            <First_Name />
            <Last_Name />
            <Email_Address />
            <UserName />
            {this.state.flag ? error : ''}
            <Password
              value1={this.state.value1}
              value2={this.state.value2}
              propshandleOnChange1={this.handleOnChange1}
              propshandleOnChange2={this.handleOnChange2}
            />
            <Enterprise_Info />
          </div>
          <div className="text-center">
            <input
              className="btn btn-primary btn-lg"
              type="submit"
              value="Submit"
              onClick={this.checkPassword}
            />
          </div>
        </div>
      );
    }
};


ReactDOM.render(
  <CreateUserForm />,
  document.getElementById('root')
);
