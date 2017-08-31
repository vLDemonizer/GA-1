class Option extends React.Component {
  render () {
    let product = this.props.product.fields;
    let product_pk = this.props.product.pk;
    return (
      <option
        name={product_pk}
      >{product.name} - {product.product_type} - {product.size} - {product.brand} - {product.department}
      </option>
    );
  }
}

class ProductList extends React.Component {
  constructor(props) {
    super(props);

    this.handleSelection = this.handleSelection.bind(this);
  }

  handleSelection(e) {
    this.props.handleKey(e.target.list.options, $("#product_info").val());
  }

  render () {
    let products = this.props.products;
    var product_list = [];
    for (var i = 0; i < products.length; i++) {
      product_list.push(<Option product={products[i]} key={'a' + i}/>);
    }
    return (
        <div className="form-group">
          <label>Search Product</label>
          <input
            onInput={this.handleSelection}
            id="product_info"
            className="form-control"
            type="text"
            list="product_options"
            autoComplete="off"
          />
          <datalist id="product_options">
            {product_list}
          </datalist>
        </div>
    );
  }
}

class HiddenInput extends React.Component {
  render () {
    let name = this.props.name;
    return (
      <input
        type="hidden"
        id={"id_" + name}
        name={name}
        value={this.props.primary_key}
        required
      />
    );
  }
}

class Details extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      key: 0,
      name: '',
      type: '',
      brand: '',
      size: '',
      department: '',
      amount: 0,
      stock: 0,
      date: '',
      amountError: false,
    }

    this.handleSubmitKey = this.handleSubmitKey.bind(this);
    this.handleAmountChange = this.handleAmountChange.bind(this);
  }

  handleSubmitKey(options, productText) {
    for(var i = 0; i < options.length; i++) {
      if (options[i].innerText === productText) {
        let product = this.props.products[i];0;
        $.ajax({
          url: '/ajax/get_product_stock/',
          data : {
            'product_class': product.pk,
            'location': $("#id_destiny").val(),
          },
          success: (data) => this.setState({stock: data})
          
        });
        this.setState({
          key: product.pk,
          name: product.fields.name,
          type: product.fields.product_type,
          brand: product.fields.brand,
          size: product.fields.size,
          department: product.fields.department,
          date: new Date().toDateString(),
        });
      }
    }
  }

  handleAmountChange(event) {
    let value = parseInt(event.target.value);
    if (value > this.state.stock) {
      this.setState({amountError: true});
    } else {
      this.setState({
        amount: value,
        amountError: false,
      });
    }
  }

  render () {
    let errorMessage = (<div className="form-errors">Amount Error: You are trying to move more than there is in stock!</div>);
    return (
      <div>
        <ProductList
          products={this.props.products}
          handleKey={this.handleSubmitKey}
        />
        {this.state.amountError? errorMessage: ''}
        <div className="form-group">
          <label>Amount</label>
          <input
            id="id_amount"
            name="amount"
            className="form-control"
            type="number"
            onChange={this.handleAmountChange}
          />
        </div>
        <HiddenInput primary_key={this.state.key} name={"product_class"}/>
        <table className="table table-responsive">
          <thead>
            <th>Name</th>
            <th>Type</th>
            <th>Brand</th>
            <th>Size</th>
            <th>Department</th>
            <th>Amount</th>
            <th>Stock</th>
            <th>Date</th>
          </thead>
          <tbody>
            <td>{this.state.name}</td>
            <td>{this.state.type}</td>
            <td>{this.state.brand}</td>
            <td>{this.state.size}</td>
            <td>{this.state.department}</td>
            <td>{this.state.amount}</td>
            <td>{this.state.stock}</td>
            <td>{this.state.date}</td>
          </tbody>
        </table>
      </div>
    );
  }
}

class LocationSelect extends React.Component {
  render () {
    let locations = this.props.locations;
    let name = this.props.name
    var location_list = [];
    for (var i = 0; i < locations.length; i++) {
      location_list.push(<option value={i} key={'e' + i}>{locations[i]}</option>);
    }
    return (
      <div className="form-group">
        <label>{this.props.tittle}</label>
        <select id={"id_" + name} name={name} className="form-control">
          {location_list}
        </select>
      </div>
    );
  }
}

class Locations extends React.Component {
  render () {
    var locations = [];
    for (var i = 0; i < this.props.names.length; i++) {
      locations.push(<LocationSelect locations={this.props.locations} name={this.props.names[i]} tittle={this.props.tittles[i]} />);
    }

    return (
      <div>
        {locations}
      </div>
    );
  }
}

class ReasonSelect extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 0,
      showTextArea: false,
    }
    this.checkReason = this.checkReason.bind(this);
  }

  checkReason(e) {
      let value = e.target.value;
      if (value == (this.props.reasons.length - 1)) {
        this.setState({showTextArea: true});
      } else {
        this.setState({showTextArea: false});
      }
  }

  render () {
    let reasons = this.props.reasons;
    var reason_list = [];
    for (var i = 0; i < reasons.length; i++) {
      if (i == (reasons.length - 1)) {
        reason_list.push(
          <option
            value={i}
            key={'c' + i}
            onClick={this.checkReason}
          >{reasons[i]}</option>
        );
      } else {
        reason_list.push(<option value={i} key={'c' + i}>{reasons[i]}</option>);
      }
    }
    var textArea = [];
    if (this.state.showTextArea) {
      textArea.push(
        <div className="form-group">
          <label>Reason Description</label>
          <textarea
            className="form-control"
            id="id_reason_description"
            name="reason_description"
            rows="2"
          ></textarea>
        </div>
      )
    }
    return (
      <div className="form-group">
        <label>Reason</label>
        <select id="id_reason"
          name="reason"
          onChange={this.checkReason}
          className="form-control"
        >
          {reason_list}
        </select>
        <br/>
        {textArea}
      </div>
    );
  }
}

class UsersComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user_key: 0,
    }
    this.handleKey = this.handleKey.bind(this);
  }

  handleKey(e) {
    let options = e.target.list.options;
    let input_text = $("#id_" + this.props.name).val();
    for (var i = 0; i < options.length; i++) {
      if (options[i].innerText === input_text) {
        let key = this.props.users[i].pk;
        this.setState({
          user_key: key,
        });
      }
    }
  }

  render () {
    let users = this.props.users;
    var user_list = [];
    let name = this.props.name;
    for (var i = 0; i < users.length; i++) {
      user_list.push(
        <option name={users[i].pk}>
          {users[i].fields.first_name} {users[i].fields.last_name}
        </option>
      );
    }
    return (
      <div className="form-group">
        <label>{this.props.tittle}</label>
        <input
          onInput={this.handleKey}
          id={"id_" + name}
          name={name}
          className="form-control"
          type="text"
          list={name + "_options"}
          autoComplete="off"
        />
        <datalist id={name + "_options"}>
          {user_list}
        </datalist>
        <HiddenInput primary_key={this.state.user_key} name={name} />
      </div>
    );
  }
}

class Users extends React.Component {
  render () {
    let user = this.props.dispatchUser[0].fields
    let user_pk = this.props.dispatchUser[0].pk
    return (
      <div className="form-group">
        <UsersComponent users={this.props.authorizedUsers} name={"authorized_by"} tittle={"Authorized By"}/>
        <UsersComponent users={this.props.receivingUsers} name={"received_by"} tittle={"Received By"}/>
        <label>
          Dispatched by: {user.first_name} {user.last_name}
        </label>
        <input
        id="id_given_by"
        name="given_by"
        className="form-control"
        type="hidden"
        value={user_pk}
        />
      </div>
    );
  }
}

class MoveOut extends React.Component{
  render () {
    return (
      <div className="container-fluid">
        <Locations locations={this.props.locations} names={["from_location", "destiny"]} tittles={["From", "To"]}/>
        <Details products={this.props.products} />
        <ReasonSelect reasons={this.props.reasons} />
        <Users
          authorizedUsers={this.props.admin_users}
          receivingUsers={this.props.retrieving_users}
          dispatchUser={this.props.current_user}
        />
      </div>
    );
  }
}
